// Mide los renglones del cuerpo de texto (huecos entre palabras, ríos, último renglón) y, con ?opt, busca para cada bloque
// la interletra y el espaciado mínimos que los mejoran sin cambiar la cantidad de renglones. Uso: copiar index.html a
// _medir.html con <script src="tools/medir-texto.js"> antes de </body>, abrir con Chrome headless --dump-dom y leer <pre id="medida">.
// Mide renglones de los bloques de cuerpo: espacios entre palabras (en múltiplos del espacio normal), ríos y último renglón.
const cv = document.createElement('canvas').getContext('2d');
function analizar(el) {
    const page = el.closest('.page').id.slice(1);
    const cs = getComputedStyle(el);
    const k = el.getBoundingClientRect().width / el.offsetWidth || 1;
    cv.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
    const sp = cv.measureText(' ').width * k;
    const rects = [];
    const tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let n; (n = tw.nextNode());) {
      const t = n.data; const re = /[^\s]+/g; let m;
      while ((m = re.exec(t))) {
        const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
        for (const q of r.getClientRects()) if (q.width > 0.5) rects.push({ x0: q.left, x1: q.right, y: q.top, h: q.height, w: m[0] });
      }
    }
    // renglones por altura
    rects.sort((a, b) => a.y - b.y || a.x0 - b.x0);
    const lines = [];
    for (const r of rects) {
      let L = lines.find((l) => Math.abs(l.y - r.y) < r.h * 0.5);
      if (!L) lines.push(L = { y: r.y, rs: [] });
      L.rs.push(r);
    }
    // columnas: por la posición x dentro del bloque (column-count del CSS)
    const ncol = parseInt(cs.columnCount) || 1, box = el.getBoundingClientRect();
    const colW = box.width / ncol;
    const colOf = (s) => Math.min(ncol - 1, Math.floor((s.rs[0].x0 - box.left + sp) / colW));
    const segs = [];
    for (const L of lines) {
      L.rs.sort((a, b) => a.x0 - b.x0);
      const by = {};
      for (const r of L.rs) (by[Math.min(ncol - 1, Math.floor((r.x0 - box.left + sp) / colW))] ??= []).push(r);
      for (const c in by) segs.push({ y: L.y, rs: by[c] });
    }
    segs.sort((a, b) => colOf(a) - colOf(b) || a.y - b.y);
    const width = Math.max(...segs.map((s) => s.rs.at(-1).x1 - s.rs[0].x0));
    const info = segs.map((s, i) => {
      const gaps = [];
      for (let j = 1; j < s.rs.length; j++) { const g = s.rs[j].x0 - s.rs[j - 1].x1; if (g > 0.3 * sp) gaps.push({ x: (s.rs[j].x0 + s.rs[j - 1].x1) / 2, a: s.rs[j - 1].x1, b: s.rs[j].x0, r: g / sp }); }
      const words = gaps.length + 1;
      return { col: colOf(s), gaps, words, fill: (s.rs.at(-1).x1 - s.rs[0].x0) / width, text: s.rs.map((r) => r.w).join(' ').replace(/­/g, '').slice(0, 60) };
    });
    const last = info.at(-1);
    const body = info.slice(0, -1).filter((l, i) => !(info[i + 1] && info[i + 1].col !== l.col && false));
    // ríos: huecos ≥1,6 espacios que se tocan en renglones seguidos (cadena de 3 o más)
    const rivers = [];
    for (let i = 0; i < info.length - 2; i++) {
      for (const g of info[i].gaps) {
        if (g.r < 1.6) continue;
        let chain = [g], prev = g, j = i + 1;
        while (j < info.length - 1 && info[j].col === info[i].col) {
          const n = info[j].gaps.find((h) => h.r >= 1.6 && h.b > prev.a - sp * 0.3 && h.a < prev.b + sp * 0.3);
          if (!n) break; chain.push(n); prev = n; j++;
        }
        if (chain.length >= 3) rivers.push({ from: i + 1, len: chain.length, avg: +(chain.reduce((s, c) => s + c.r, 0) / chain.length).toFixed(2) });
      }
    }
    const loose = info.slice(0, -1).map((l, i) => ({ n: i + 1, max: +Math.max(0, ...l.gaps.map((g) => g.r)).toFixed(2), avg: l.gaps.length ? +(l.gaps.reduce((s, g) => s + g.r, 0) / l.gaps.length).toFixed(2) : 0, big: l.gaps.filter((g) => g.r >= 2).length, text: l.text }))
      .filter((l) => l.max >= 2.2 || l.big >= 2);
    const maxGap = Math.max(0, ...info.slice(0, -1).flatMap((l) => l.gaps.map((g) => g.r)));
    // líneas flojas: suma de lo que excede 2 espacios en cada hueco
    const exceso = info.slice(0, -1).reduce((s, l) => s + l.gaps.reduce((t, g) => t + Math.max(0, g.r - 2) ** 2, 0), 0);
    const viuda = last.words <= 2 && last.fill < 0.35 ? 1 : 0;
    const cls = el.className ? el.className.split(' ')[0] : el.parentElement.className.split(' ')[0] + ' > p:nth-of-type(' + ([...el.parentElement.children].filter((c) => c.tagName === 'P').indexOf(el) + 1) + ')';
    return { page, cls, lines: info.length, lastWords: last.words, lastFill: +last.fill.toFixed(2), last: last.text, loose, rivers, maxGap: +maxGap.toFixed(2), exceso: +exceso.toFixed(2), viuda };
}
const SEL = '.page .body:not(:has(> p)), .page .body > p, .page [class*="p006__text"], .page [class*="p007__text"]';
const nota = (a) => a.viuda * 100 + a.exceso * 3 + a.rivers.length * 2 + Math.max(0, a.maxGap - 2.2) * 4;
function medir() {
  const out = [];
  for (const el of document.querySelectorAll(SEL)) {
    const a0 = analizar(el);
    if (!location.search.includes('opt') || (nota(a0) < 3)) { out.push(a0); continue; }
    let best = { ls: 0, a: a0, n: nota(a0) };
    const R = a0.viuda ? 0.0241 : 0.0161;
    for (const hy of ['', 'none']) for (let ls = -R + 0.0001; ls <= R; ls += 0.002) for (const ws of [0, -0.02, 0.02, 0.04, 0.06]) {
      el.style.letterSpacing = ls.toFixed(3) + 'em'; el.style.wordSpacing = ws + 'em'; el.style.hyphens = hy;
      const a = analizar(el);
      if (a.lines !== a0.lines) continue;
      const n = nota(a) + Math.abs(ls) * 60 + Math.abs(ws) * 10 + (hy ? 3 : 0);
      if (n < best.n - 0.5) best = { ls: +ls.toFixed(3), ws, hy, a, n };
    }
    el.style.letterSpacing = ''; el.style.wordSpacing = ''; el.style.hyphens = '';
    out.push({ ...best.a, antes: { viuda: a0.viuda, maxGap: a0.maxGap, exceso: a0.exceso, rios: a0.rivers.length, last: a0.last }, ls: best.ls, ws: best.ws || 0, hy: best.hy || '' });
  }
  const pre = document.createElement('pre'); pre.id = 'medida'; pre.textContent = JSON.stringify(out); document.body.append(pre);
}
Promise.all([...document.fonts].map((f) => f.load())).then(() => document.fonts.ready).then(() => setTimeout(medir, 500));
