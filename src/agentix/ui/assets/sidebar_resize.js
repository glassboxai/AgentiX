/* V7-068: maintained resize behavior for the three native Gradio sidebars.
   Geometry stays in CSS custom properties so Gradio's inline width/offset cannot
   win on re-render; no generated code, storage or network access is involved. */
(() => {
  const MINIMUM = 280;
  const KEYBOARD_STEP = 16;
  const ATTEMPTS = 20;
  const RETRY_MS = 250;
  const widths = new Map();

  /* V7-070: the shared left model sidebar keeps Gradio's fixed width and is not
     resizable; only the two tab panels expose the maintained handle. */
  const panels = () => [
    {id: 'tools-sidebar', side: 'right', fallback: 420},
    {id: 'applications-sidebar', side: 'right', fallback: 380},
  ];

  /* V7-068-D6: only a minimum is enforced; the user may widen a panel freely. */
  const clamp = value => Math.round(Math.max(value, MINIMUM));

  /* V7-069/V7-070: all three panels share one `.sidebar-parent`, so a single
     global overlap let the last mounted panel pad the left sidebar's work area.
     The left panel is fixed width, so it alone owns that padding, computed with
     Gradio's own formula and 30 px gutter to keep the workspace edge clear. */
  const syncOverlap = () => {
    const element = document.getElementById('agentix-sidebar');
    const parent = element?.closest('.sidebar-parent');
    if (!parent) return;
    const width = element.getBoundingClientRect().width;
    const offset = parent.getBoundingClientRect().left;
    parent.style.setProperty('--overlap-amount', Math.max(0, width - offset + 30) + 'px');
  };

  const apply = (element, width) => {
    widths.set(element.id, width);
    element.style.setProperty('--agentix-sidebar-width', width + 'px');
    /* The containing column owns the workspace padding, so it must inherit the
       resized width; custom properties do not propagate upwards. */
    if (element.parentElement) {
      element.parentElement.style.setProperty('--agentix-sidebar-width', width + 'px');
    }
    const handle = element.querySelector('.agentix-sidebar-resizer');
    if (handle) handle.setAttribute('aria-valuenow', String(width));
  };

  const current = (element, fallback) => widths.get(element.id) || fallback;

  const resize = (element, width) => apply(element, clamp(width));

  const start = (event, element, side) => {
    if (event.button !== undefined && event.button !== 0) return;
    event.preventDefault();
    const handle = event.currentTarget;
    handle.classList.add('agentix-resizing');
    handle.setPointerCapture?.(event.pointerId);
    const move = pointer => {
      const width = side === 'right' ? innerWidth - pointer.clientX : pointer.clientX;
      resize(element, width);
    };
    const stop = () => {
      handle.classList.remove('agentix-resizing');
      handle.removeEventListener('pointermove', move);
      handle.removeEventListener('pointerup', stop);
      handle.removeEventListener('pointercancel', stop);
    };
    handle.addEventListener('pointermove', move);
    handle.addEventListener('pointerup', stop);
    handle.addEventListener('pointercancel', stop);
  };

  const key = (event, element, side, fallback) => {
    const width = current(element, fallback);
    const grow = side === 'right' ? 'ArrowLeft' : 'ArrowRight';
    const shrink = side === 'right' ? 'ArrowRight' : 'ArrowLeft';
    if (event.key === grow) resize(element, width + KEYBOARD_STEP);
    else if (event.key === shrink) resize(element, width - KEYBOARD_STEP);
    else if (event.key === 'Home') resize(element, fallback);
    else return;
    event.preventDefault();
  };

  const mount = (element, side, fallback) => {
    const existing = element.querySelector('.agentix-sidebar-resizer');
    if (existing && element.dataset.agentixResizable === 'true') {
      apply(element, current(element, fallback));
      return;
    }
    element.dataset.agentixResizable = 'true';
    if (existing) existing.remove();
    const handle = document.createElement('div');
    handle.className = 'agentix-sidebar-resizer';
    handle.id = element.id + '-resizer';
    handle.setAttribute('role', 'separator');
    handle.setAttribute('aria-orientation', 'vertical');
    handle.setAttribute('aria-label', 'Resize panel');
    handle.setAttribute('aria-valuemin', String(MINIMUM));
    handle.tabIndex = 0;
    handle.addEventListener('pointerdown', event => start(event, element, side));
    handle.addEventListener('keydown', event => key(event, element, side, fallback));
    handle.addEventListener('dblclick', () => resize(element, fallback));
    element.appendChild(handle);
    apply(element, current(element, fallback));
    /* Gradio rewrites the inline width on toggle; reassert the owned geometry. */
    new MutationObserver(() => apply(element, current(element, fallback))).observe(element, {
      attributes: true,
      attributeFilter: ['class'],
    });
  };

  const scan = () => {
    let pending = false;
    syncOverlap();
    /* The native toggle rewrites the panel class and inline width; keep the
       left panel's overlap correct without exposing a resize handle. */
    const left = document.getElementById('agentix-sidebar');
    if (left && left.dataset.agentixOverlap !== 'true') {
      left.dataset.agentixOverlap = 'true';
      new MutationObserver(syncOverlap).observe(left, {
        attributes: true,
        attributeFilter: ['class', 'style'],
      });
    }
    for (const panel of panels()) {
      const element = document.getElementById(panel.id);
      if (!element) {
        pending = true;
        continue;
      }
      mount(element, panel.side, panel.fallback);
    }
    return pending;
  };

  let remaining = ATTEMPTS;
  const attempt = () => {
    if (!scan() || remaining-- <= 0) return;
    setTimeout(attempt, RETRY_MS);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', attempt, {once: true});
  else attempt();

  /* Gradio may replace a sidebar subtree after a callback; restore the handle and
     the owner's width instead of leaving the panel at its stylesheet default. */
  let pending = 0;
  new MutationObserver(() => {
    clearTimeout(pending);
    pending = setTimeout(scan, 120);
  }).observe(document.body, {childList: true, subtree: true});

  addEventListener('resize', () => {
    syncOverlap();
    for (const panel of panels()) {
      const element = document.getElementById(panel.id);
      if (element) resize(element, current(element, panel.fallback));
    }
  });
})();
