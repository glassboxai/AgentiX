/* Three source panes share a user-adjustable height and independent widths. */
(() => {
  const setup = () => {
    const row = document.getElementById('applications-tool-panes');
    if (!row || row.dataset.sizingReady) return;
    const columns = [...row.children].filter(node => node.classList.contains('column'));
    if (columns.length !== 3) return;
    row.dataset.sizingReady = 'true'; let height = 540; const widths = [1, 1, 1];
    const layout = () => {
      if (!row.getBoundingClientRect().width) return;
      row.style.height = height + 'px'; row.style.flexWrap = 'nowrap';
      const available = row.clientWidth - 20, total = widths.reduce((a,b) => a+b, 0);
      columns.forEach((column, i) => {
        column.style.flex = '0 0 ' + (available * widths[i] / total) + 'px'; column.style.height = (height-18) + 'px';
        column.querySelectorAll('.cm-editor').forEach(editor => {
          const top = editor.getBoundingClientRect().top - row.getBoundingClientRect().top;
          if (editor.offsetParent) editor.style.height = Math.max(100, height - top - 35) + 'px';
        });
      });
      [...row.querySelectorAll('.review-column-split')].forEach((handle, i) => {
        handle.style.left = (columns[i].offsetLeft + columns[i].offsetWidth + 1) + 'px';
      });
    };
    for (let i = 0; i < 2; i++) {
      const handle = document.createElement('button'); handle.type = 'button'; handle.className = 'review-column-split'; handle.setAttribute('aria-label', 'Resize code column ' + (i+1)); row.appendChild(handle);
      handle.onpointerdown = event => {
        event.preventDefault(); handle.setPointerCapture(event.pointerId);
        const startX = event.clientX, left = widths[i], right = widths[i+1], total = widths.reduce((a,b) => a+b, 0);
        const move = point => {const delta = (point.clientX-startX) * total / (row.clientWidth-20); widths[i] = Math.max(.35, Math.min(left+right-.35,left+delta)); widths[i+1] = left+right-widths[i]; layout();};
        handle.addEventListener('pointermove', move); handle.addEventListener('pointerup', () => handle.removeEventListener('pointermove', move), {once:true});
      };
      handle.onkeydown = event => {if (!['ArrowLeft','ArrowRight'].includes(event.key)) return; event.preventDefault(); const delta = event.key === 'ArrowRight' ? .1 : -.1; if (widths[i]+delta >= .35 && widths[i+1]-delta >= .35) {widths[i]+=delta; widths[i+1]-=delta; layout();}};
    }
    const bottom = document.createElement('button'); bottom.type = 'button'; bottom.className = 'review-height-resize'; bottom.setAttribute('aria-label', 'Resize code pane height'); row.appendChild(bottom);
    bottom.onpointerdown = event => {event.preventDefault(); bottom.setPointerCapture(event.pointerId); const y=event.clientY,start=height; const move=point=>{height=Math.max(300,Math.min(1200,start+point.clientY-y));layout();}; bottom.addEventListener('pointermove',move);bottom.addEventListener('pointerup',()=>bottom.removeEventListener('pointermove',move),{once:true});};
    bottom.onkeydown = event => {if (['ArrowUp','ArrowDown'].includes(event.key)) {event.preventDefault();height=Math.max(300,Math.min(1200,height+(event.key==='ArrowDown'?20:-20)));layout();}};
    new ResizeObserver(layout).observe(row); row.addEventListener('click', () => requestAnimationFrame(layout)); layout();
  };
  new MutationObserver(setup).observe(document.documentElement,{subtree:true,childList:true}); setup();
})();
