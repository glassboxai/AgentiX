/* Maintained parent bridge: a right-clicked widget opens its style window. */
(() => {
  let frame = null;
  const setup = () => {
    const next = document.querySelector('#applications-frame iframe');
    if (next) frame = next;
  };
  addEventListener('message', event => {
    if (!frame || event.source !== frame.contentWindow) return;
    const data = event.data;
    if (!data || data.type !== 'agentix-widget-style' || typeof data.tool !== 'string') return;
    if (!/^[a-z][a-z0-9_]{0,63}$/.test(data.tool)) return;
    const field = document.querySelector('#applications-widget-style-tool textarea, #applications-widget-style-tool input');
    const button = document.getElementById('applications-widget-style-open');
    if (!field || !button) return;
    Object.getOwnPropertyDescriptor(Object.getPrototypeOf(field), 'value').set.call(field, data.tool);
    field.dispatchEvent(new Event('input', {bubbles: true}));
    button.click();
  });
  new MutationObserver(setup).observe(document.documentElement, {subtree: true, childList: true});
  setup();

  // Apply a saved stylesheet to the live preview. The hidden field carries the
  // merged CSS from the save handler; polling is used because Gradio updates the
  // textarea value through a property setter that fires no attribute mutation.
  let last = '';
  const applyField = () => document.querySelector('#applications-widget-style-apply textarea, #applications-widget-style-apply input');
  const push = payload => {
    if (!frame || !frame.contentWindow) return;
    frame.contentWindow.postMessage({type: 'agentix-widget-style-apply', ...payload}, '*');
  };
  setInterval(() => {
    const field = applyField();
    if (!field || field.value === last) return;
    last = field.value;
    if (!last) return;
    try {
      const payload = JSON.parse(last);
      if (typeof payload.tool === 'string' && typeof payload.css === 'string') push(payload);
    } catch (_) { /* ignore a non-payload value */ }
  }, 250);
  // A reload of the preview keeps the last applied style for this session.
  addEventListener('message', event => {
    if (frame && event.source === frame.contentWindow && event.data === 'agentix-widget-style-ready') {
      if (!last) return;
      try { push(JSON.parse(last)); } catch (_) { /* ignore */ }
    }
  });

  // Drag by the title bar. The overlay's left/top are !important, so the position
  // is driven through the custom properties the stylesheet resolves instead of
  // inline left/top, which would lose and leave the box stuck at its centre.
  let drag = null;
  const dialog = () => document.getElementById('agentix-widget-style-dialog');
  const clamp = (value, low, high) => Math.min(Math.max(value, low), high);
  const place = (box, left, top) => {
    box.style.setProperty('--agentix-widget-style-left', left + 'px');
    box.style.setProperty('--agentix-widget-style-top', top + 'px');
    box.style.setProperty('--agentix-widget-style-shift', 'none');
  };
  document.addEventListener('pointerdown', event => {
    const box = dialog();
    const title = document.getElementById('agentix-widget-style-title');
    if (!box || !title || !title.contains(event.target)) return;
    if (event.button !== 0) return;
    const rect = box.getBoundingClientRect();
    drag = {x: event.clientX, y: event.clientY, left: rect.left, top: rect.top, box};
    place(box, rect.left, rect.top);
    box.style.cursor = 'grabbing';
    event.preventDefault();
  }, true);
  document.addEventListener('pointermove', event => {
    if (!drag) return;
    const width = drag.box.offsetWidth;
    const height = drag.box.offsetHeight;
    place(
      drag.box,
      clamp(drag.left + event.clientX - drag.x, 0, Math.max(0, innerWidth - width)),
      clamp(drag.top + event.clientY - drag.y, 0, Math.max(0, innerHeight - height))
    );
  }, true);
  const release = () => {
    if (!drag) return;
    drag.box.style.cursor = '';
    drag = null;
  };
  document.addEventListener('pointerup', release, true);
  document.addEventListener('pointercancel', release, true);
})();
