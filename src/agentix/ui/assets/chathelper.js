/* Maintained UI only: editor buffers are data; no generated JavaScript is evaluated. */
(() => {
  const fields = {'applications-tool-code': 'code', 'applications-widget-code': 'widget', 'applications-tool-tests': 'tool_tests', 'applications-widget-tests': 'widget_tests'};
  const suffixes = {code: '_code.py', widget: '_widget.py', tool_tests: '_tests.py', widget_tests: '_widget_tests.py'};
  const selectedFile = () => (document.querySelector('#applications-files input')?.value || '').trim();
  const fileLabel = pane => {
    const selected = selectedFile();
    const base = selected.replace(/_(widget_tests|widget|code|tests)\.py$/, '');
    return base ? base + suffixes[pane] : selected;
  };
  const paintFile = popup => {
    const label = document.getElementById('chathelper-file');
    if (!label) return;
    const name = popup.dataset.pane ? fileLabel(popup.dataset.pane) : '';
    popup.dataset.filename = name;
    label.textContent = name || 'No file selected';
  };
  const setValue = (id, value) => {
    const input = document.querySelector('#' + id + ' textarea, #' + id + ' input');
    if (!input) return false;
    Object.getOwnPropertyDescriptor(Object.getPrototypeOf(input), 'value').set.call(input, value);
    input.dispatchEvent(new Event('input', {bubbles: true})); return true;
  };
  document.addEventListener('contextmenu', event => {
    const editor = event.target.closest('[id] .cm-editor');
    if (!editor) return;
    const component = editor.closest('[id^="applications-"]');
    if (!component || !fields[component.id]) return;
    event.preventDefault(); document.getElementById('chathelper-menu')?.remove();
    const menu = document.createElement('button'); menu.id = 'chathelper-menu'; menu.textContent = 'Ask about this code';
    menu.style.left = Math.min(event.clientX, innerWidth - 190) + 'px'; menu.style.top = Math.min(event.clientY, innerHeight - 50) + 'px';
    document.body.appendChild(menu);
    menu.onclick = () => {
      if (!setValue('chathelper-pane', fields[component.id])) return;
      const popup = document.getElementById('chathelper-window');
      popup.classList.add('chathelper-open'); popup.classList.remove('chathelper-minimized');
      popup.dataset.pane = fields[component.id]; paintFile(popup); menu.remove();
      document.querySelector('#chathelper-question textarea')?.focus();
    };
  });
  document.addEventListener('pointerdown', event => {
    const menu = document.getElementById('chathelper-menu');
    if (menu && !menu.contains(event.target)) menu.remove();
    const title = event.target.closest('#chathelper-title');
    if (!title || event.target.closest('button')) return;
    const popup = document.getElementById('chathelper-window');
    const box = popup.getBoundingClientRect(), x = event.clientX, y = event.clientY;
    event.preventDefault(); title.setPointerCapture(event.pointerId);
    const move = current => {popup.style.left = Math.max(0, Math.min(innerWidth - 100, box.left + current.clientX - x)) + 'px'; popup.style.top = Math.max(0, Math.min(innerHeight - 40, box.top + current.clientY - y)) + 'px';};
    title.addEventListener('pointermove', move);
    const stop = () => title.removeEventListener('pointermove', move);
    title.addEventListener('pointerup', stop, {once: true}); title.addEventListener('pointercancel', stop, {once: true});
  });
  document.addEventListener('click', event => {
    const popup = document.getElementById('chathelper-window');
    if (event.target.closest('#chathelper-close')) popup?.classList.remove('chathelper-open');
    if (event.target.closest('#chathelper-minimize')) popup?.classList.toggle('chathelper-minimized');
  });
  for (const type of ['change', 'input']) document.addEventListener(type, event => {
    if (!event.target.closest('#applications-files')) return;
    const popup = document.getElementById('chathelper-window');
    if (popup?.classList.contains('chathelper-open')) paintFile(popup);
  });
  document.addEventListener('keydown', event => {if (event.key === 'Escape') {document.getElementById('chathelper-menu')?.remove(); document.getElementById('chathelper-window')?.classList.remove('chathelper-open');}});
})();
