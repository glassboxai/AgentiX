/* V7-075 agentix-mermaid-render: render fenced Mermaid blocks inside the read-only code-help transcript only. */
(() => {
  const HOST = '#chathelper-transcript';
  const BLOCK =
    'pre > code.language-mermaid:not(.mermaid-failed), div.mermaid:not([data-processed]):not(.mermaid-failed)';
  const ATTEMPTS = 3;
  const ATTEMPT_MS = 1500;
  const pending = new WeakSet();
  let sequence = 0;

  const restore = (host, source) => {
    const pre = document.createElement('pre');
    const code = document.createElement('code');
    code.className = 'language-mermaid mermaid-failed';
    code.textContent = source;
    pre.appendChild(code);
    host.replaceWith(pre);
  };

  /* Mermaid serialises renders through an internal queue that can strand the first
     task when it is pushed while the queue is draining at page load. A bounded
     retry pushes a fresh task, which drains the queue and settles. */
  const draw = async source => {
    let lastError;
    for (let attempt = 0; attempt < ATTEMPTS; attempt += 1) {
      const id = 'agentix-mermaid-' + (++sequence);
      try {
        return await Promise.race([
          window.mermaid.render(id, source),
          new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), ATTEMPT_MS))
        ]);
      } catch (error) {
        lastError = error;
      }
    }
    throw lastError;
  };

  const render = async () => {
    const root = document.querySelector(HOST);
    if (!root || !window.mermaid) return;
    const blocks = [...root.querySelectorAll(BLOCK)].filter(code => !pending.has(code));
    if (!blocks.length) return;
    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'strict',
      theme: 'dark',
      fontFamily: 'Inter, sans-serif'
    });
    for (const node of blocks) {
      pending.add(node);
      const source = node.textContent;
      let host = node;
      if (node.tagName !== 'DIV') {
        host = document.createElement('div');
        host.className = 'mermaid';
        (node.closest('pre') || node).replaceWith(host);
      }
      try {
        const drawn = await draw(source);
        host.innerHTML = drawn.svg;
        host.setAttribute('data-processed', 'true');
        drawn.bindFunctions?.(host);
      } catch (error) {
        restore(host, source);
      }
    }
  };

  let scheduled = false;
  const schedule = () => {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => { scheduled = false; render().catch(() => {}); });
  };

  const observe = () => {
    const root = document.querySelector(HOST);
    if (!root) { requestAnimationFrame(observe); return; }
    new MutationObserver(schedule).observe(root, {childList: true, subtree: true});
    schedule();
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', observe);
  else observe();
})();
