/* Maintained editor: numeric geometry only; original Gradio nodes stay mounted. */
(() => {
  'use strict';
  let initialized = false;
  const boot = async () => {
    const paused = document.getElementById('application_paused');
    const canvas = document.querySelector('.application-canvas');
    const edit = document.getElementById('application_edit');
    if (initialized || (!paused && (!canvas || !edit))) return;
    initialized = true;
    let state;
    try {
      const response = await fetch('/_agentix/layout', {cache: 'no-store'});
      if (!response.ok) throw Error('Layout unavailable');
      state = await response.json();
    } catch (_) { initialized = false; return; }
    const post = async (action, data = {}) => {
      const response = await fetch('/_agentix/' + action, {
        method: 'POST', headers: {'Content-Type': 'application/json', 'X-Agentix-Token': state.token},
        body: JSON.stringify(data)
      });
      if (!response.ok) throw Error('Operation rejected');
    };
    const play = document.getElementById('application_execute');
    const close = document.getElementById('application_stop');
    const refresh = document.getElementById('application_refresh');
    if (refresh) {
      // Reload the same validated loopback page so a layout saved from another
      // browser tab is read again; no host route or new capability is involved.
      refresh.setAttribute('aria-label', 'Reload application');
      refresh.addEventListener('click', event => {
        event.preventDefault(); event.stopImmediatePropagation();
        location.reload();
      }, true);
    }
    if (close) {
      close.setAttribute('aria-label', 'Close application');
      close.addEventListener('click', async event => {
        event.preventDefault(); event.stopImmediatePropagation();
        close.disabled = true;
        try { await post('close'); }
        catch (_) { close.disabled = false; }
      }, true);
    }
    if (paused) {
      play.setAttribute('aria-label', 'Resume application');
      play.addEventListener('click', async () => {
        play.disabled = true; play.textContent = 'Starting…';
        try { await post('restart'); location.reload(); }
        catch (_) { play.disabled = false; play.textContent = 'Retry start'; }
      });
      return;
    }
    let editing = false;
    let geometry = state.layout.positions;
    let hidden = new Set(Array.isArray(state.layout.hidden) ? state.layout.hidden : []);
    const allowed = /^(application_(input|result|words_result|vowels_result|status)|application_(words|vowels)(_[2-9]|_[1-9][0-9]+)?_(input|output|execute))$/;
    const declared = Array.isArray(state.controls) ? new Set(state.controls) : null;
    const nodes = [...canvas.querySelectorAll('[id]')].filter(node => declared ? declared.has(node.id) : allowed.test(node.id));
    const notify = document.createElement('span');
    notify.className = 'application-layout-notice'; notify.setAttribute('role', 'status');
    document.body.appendChild(notify);
    const toggles = new Map();
    const groups = state.groups && typeof state.groups === 'object' ? state.groups : {};
    const palette = new Map();
    const colorFor = id => {
      const key = groups[id];
      if (!key) return null;
      if (!palette.has(key)) palette.set(key, 'hsl(' + Math.floor(Math.random()*360) + ' 70% 45%)');
      return palette.get(key);
    };
    canvas.addEventListener('dblclick', event => {
      const node = nodes.find(candidate => candidate.contains(event.target));
      const tool = node && groups[node.id];
      if (!tool || tool === 'application_status' || tool.startsWith('application_input_')) return;
      event.preventDefault();
      parent.postMessage({type: 'agentix-widget-selection', tool}, '*');
    });
    // Right-click opens the style window only while the layout editor is active.
    canvas.addEventListener('contextmenu', event => {
      if (!editing) return;
      const node = nodes.find(candidate => candidate.contains(event.target));
      const tool = node && groups[node.id];
      if (!tool || tool === 'application_status' || tool.startsWith('application_input_')) return;
      event.preventDefault();
      parent.postMessage({type: 'agentix-widget-style', tool}, '*');
    });
    // Apply a saved stylesheet to the live widget instances of one tool.
    // The preview's own sheet forces background and radius with !important at
    // specificity (0,4,0), which no injected rule can outrank reliably. Inline
    // declarations marked important win over every author stylesheet, so the live
    // copy is applied directly to the widget nodes; the saved file keeps its
    // reviewed, plain form.
    const applyInline = (css, tool, id) => {
      const scoped = css.split('application_' + tool + '_').join('application_' + id + '_');
      for (const [, selector, body] of scoped.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
        if (selector.includes(':hover')) continue;
        const plain = selector.replace(/:where\((\[id\^="[^"]+"\])\)/g, '$1').trim();
        let nodes;
        try {
          nodes = [...document.querySelectorAll(plain)];
        } catch (_) {
          continue;
        }
        for (const node of nodes) {
          for (const part of body.split(';')) {
            const separator = part.indexOf(':');
            if (separator < 1) continue;
            const name = part.slice(0, separator).trim();
            const value = part.slice(separator + 1).trim();
            if (!name || !value) continue;
            node.style.setProperty(name, value, 'important');
            // Form controls do not inherit font from their container, and the
            // caption text lives in a span that Gradio styles directly, so both
            // need the declaration. Layout grips are excluded: they are buttons
            // inside the widget and must keep their own fixed glyph size.
            if (name === 'font-family' || name === 'font-size') {
              // A Gradio label can wrap the input itself. Caption rules may
              // reach only its text, or they overwrite the value's font.
              const caption = /(?:\slabel|\s\.label-wrap)$/.test(plain);
              const controls = node.querySelectorAll(caption ? 'span' :
                'input:not(.application-visibility-toggle), textarea, select, ' +
                'button:not(.application-layout-handle), label span, .label-wrap span');
              for (const control of controls) {
                control.style.setProperty(name, value, 'important');
              }
            }
          }
        }
      }
    };
    addEventListener('message', event => {
      if (event.source !== parent) return;
      const data = event.data;
      if (!data || data.type !== 'agentix-widget-style-apply') return;
      if (typeof data.tool !== 'string' || typeof data.css !== 'string') return;
      if (!/^[a-z][a-z0-9_]{0,63}$/.test(data.tool) || data.css.length > 16384) return;
      const ids = (Array.isArray(data.ids) ? data.ids : []).filter(
        id => typeof id === 'string' && /^[a-z][a-z0-9_]{0,63}$/.test(id)
      );
      if (!ids.length) return;
      for (const id of ids) applyInline(data.css, data.tool, id);
    });
    parent.postMessage('agentix-widget-style-ready', '*');
    const paintHandles = on => {
      for (const node of nodes) {
        const handle = node.querySelector('.application-layout-handle.move');
        if (!handle) continue;
        if (!on) { handle.style.removeProperty('--application-handle-color'); continue; }
        const color = colorFor(node.id);
        if (color) handle.style.setProperty('--application-handle-color', color);
      }
    };
    let legend = null;
    const legendLabel = key => key === 'application_status' ? 'Status'
      : key.startsWith('application_input_') ? 'Input: ' + key.slice('application_input_'.length)
      : key;
    const paintLegend = on => {
      if (legend) legend.remove();
      legend = null;
      if (!on) return;
      legend = document.createElement('aside');
      legend.id = 'application-color-legend';
      legend.setAttribute('aria-label', 'Tools');
      const caption = document.createElement('p');
      caption.className = 'application-legend-title'; caption.textContent = 'Tools';
      legend.appendChild(caption);
      const seen = new Set();
      for (const node of nodes) {
        const key = groups[node.id];
        if (!key || seen.has(key)) continue;
        seen.add(key);
        const row = document.createElement('div');
        row.className = 'application-legend-row';
        const swatch = document.createElement('span');
        swatch.className = 'application-legend-swatch';
        swatch.style.background = colorFor(node.id);
        const text = document.createElement('span');
        text.className = 'application-legend-name'; text.textContent = legendLabel(key);
        row.append(swatch, text); legend.appendChild(row);
      }
      canvas.appendChild(legend);
    };
    const apply = () => {
      canvas.classList.add('application-layout-active');
      let bottom = 120;
      for (const node of nodes) {
        const box = geometry[node.id];
        if (!box) continue;
        Object.assign(node.style, {position: 'absolute', left: box.x+'px', top: box.y+'px', width: box.width+'px', height: box.height+'px', minWidth: '0', margin: '0'});
        const toggle = toggles.get(node.id);
        if (toggle) Object.assign(toggle.style, {left: (box.x + box.width - 20)+'px', top: (box.y + 2)+'px'});
        bottom = Math.max(bottom, box.y + box.height + 30);
      }
      canvas.style.minHeight = bottom+'px';
    };
    const applyVisibility = () => {
      for (const node of nodes) {
        const off = hidden.has(node.id) && !editing;
        node.classList.toggle('application-hidden-control', off);
        node.style.display = off ? 'none' : '';
      }
    };
    const capture = () => {
      const parent = canvas.getBoundingClientRect();
      const captured = {};
      for (const node of nodes) {
        const box = node.getBoundingClientRect();
        captured[node.id] = {x: Math.max(0, Math.round(box.left-parent.left)), y: Math.max(0, Math.round(box.top-parent.top)), width: Math.max(48, Math.min(4096, Math.round(box.width))), height: Math.max(32, Math.min(4096, Math.round(box.height)))};
      }
      geometry = captured;
    };
    if (Object.keys(geometry).length) apply();
    for (const node of nodes) {
      node.classList.add("application-editable-element");
      node.style.overflow = "visible";
      const toggle = document.createElement('input');
      toggle.type = 'checkbox'; toggle.className = 'application-visibility-toggle';
      toggle.checked = !hidden.has(node.id);
      toggle.setAttribute('aria-label', 'visible '+node.id);
      toggle.title = 'Keep this control visible outside Edit';
      for (const type of ['click', 'pointerdown']) toggle.addEventListener(type, event => event.stopPropagation());
      toggle.addEventListener('change', () => {
        if (toggle.checked) hidden.delete(node.id); else hidden.add(node.id);
      });
      toggles.set(node.id, toggle);
      canvas.appendChild(toggle);
      for (const kind of ['move', 'resize']) {
        const handle = document.createElement('button');
        handle.type = 'button'; handle.className = 'application-layout-handle '+kind;
        handle.setAttribute('aria-label', kind+' '+node.id);
        handle.textContent = kind === 'move' ? '⠿' : '◢';
        node.appendChild(handle);
        // Moving an action button must not also invoke its Gradio callback.
        handle.addEventListener('click', event => { event.preventDefault(); event.stopPropagation(); });
        handle.addEventListener('pointerdown', event => {
          if (!editing) return;
          event.preventDefault(); event.stopPropagation();
          handle.setPointerCapture(event.pointerId);
          const start = {...geometry[node.id]}, x = event.clientX, y = event.clientY;
          const update = move => {
            const dx = Math.round(move.clientX-x), dy = Math.round(move.clientY-y);
            geometry[node.id] = kind === 'move' ? {...start, x: Math.min(10000, Math.max(0, start.x+dx)), y: Math.min(10000, Math.max(0, start.y+dy))} : {...start, width: Math.min(4096, Math.max(48, start.width+dx)), height: Math.min(4096, Math.max(32, start.height+dy))};
            apply();
          };
          handle.addEventListener('pointermove', update);
          handle.addEventListener('pointerup', () => handle.removeEventListener('pointermove', update), {once: true});
          handle.addEventListener('pointercancel', () => handle.removeEventListener('pointermove', update), {once: true});
        });
        handle.addEventListener('keydown', event => {
          if (!editing || !['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(event.key)) return;
          event.preventDefault();
          const box = geometry[node.id], horizontal = ['ArrowLeft','ArrowRight'].includes(event.key);
          const key = kind === 'move' ? (horizontal ? 'x' : 'y') : (horizontal ? 'width' : 'height');
          const delta = ['ArrowLeft','ArrowUp'].includes(event.key) ? -10 : 10;
          const minimum = key === 'width' ? 48 : key === 'height' ? 32 : 0;
          box[key] = Math.min(kind === 'move' ? 10000 : 4096, Math.max(minimum, box[key]+delta)); apply();
        });
      }
    }
    apply();
    applyVisibility();
    edit.disabled = !state.editable;
    edit.setAttribute('aria-label', 'Edit application layout');
    edit.addEventListener('click', async event => {
      event.preventDefault(); event.stopImmediatePropagation();
      if (!editing) { editing = true; palette.clear(); applyVisibility(); capture(); apply(); paintHandles(true); paintLegend(true); }
      else {
        edit.disabled = true; notify.textContent = 'Saving layout...';
        try {
          await post('layout', {version: 1, positions: geometry, hidden: [...hidden]});
          editing = false; applyVisibility(); paintHandles(false); paintLegend(false); notify.textContent = 'Layout saved';
        }
        catch (_) { notify.textContent = 'Layout could not be saved. Retry.'; }
        finally { edit.disabled = false; }
      }

      canvas.classList.toggle('application-layout-editing', editing);
      edit.setAttribute('aria-pressed', String(editing));
    }, true);
    if (play) play.addEventListener('click', async event => {
      const status = document.querySelector('#application_status textarea, #application_status input');
      if (status && status.value === 'Running') {
        event.preventDefault(); event.stopImmediatePropagation();
        play.disabled = true;
        try { await post('cancel'); location.reload(); }
        catch (_) { notify.textContent = 'Stop failed; close the application.'; play.disabled = false; }
      }
    }, true);
    const timer = setInterval(() => {
      if (!play || !document.contains(play)) {clearInterval(timer); return;}
      const status = document.querySelector('#application_status textarea, #application_status input');
      const running = status && status.value === 'Running';
      play.classList.toggle('application-running', !!running);
      play.setAttribute('aria-label', running ? 'Stop running application' : 'Run application');
    }, 250);
  };
  const observer = new MutationObserver(() => { void boot(); });
  observer.observe(document.documentElement, {childList: true, subtree: true});
  void boot();
})();
