/* Maintained parent bridge: a double-clicked widget selects its reviewed source file. */
(() => {
  let frame = null;
  const setup = () => {
    const next = document.querySelector('#applications-frame iframe');
    if (next) frame = next;
  };
  addEventListener('message', event => {
    if (!frame || event.source !== frame.contentWindow) return;
    const data = event.data;
    if (!data || data.type !== 'agentix-widget-selection' || typeof data.tool !== 'string') return;
    if (!/^[a-z][a-z0-9_]{0,63}$/.test(data.tool)) return;
    const field = document.querySelector('#applications-widget-selection textarea, #applications-widget-selection input');
    const button = document.getElementById('applications-widget-select');
    if (!field || !button) return;
    Object.getOwnPropertyDescriptor(Object.getPrototypeOf(field), 'value').set.call(field, data.tool);
    field.dispatchEvent(new Event('input', {bubbles: true}));
    button.click();
  });
  new MutationObserver(setup).observe(document.documentElement, {subtree: true, childList: true});
  setup();
})();
