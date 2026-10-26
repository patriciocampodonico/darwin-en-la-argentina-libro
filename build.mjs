// Arma index.html con las páginas de pages/ y cuida las páginas aprobadas.
//   node build.mjs               arma el libro y revisa los bloqueos
//   node build.mjs shot 002      captura PNG + PDF de una página en salida/ (002-003 = PNG de la doble)
//   node build.mjs pdf           PDF del libro completo en salida/
//   node build.mjs approve 001   bloquea una página aprobada
import { readFileSync, writeFileSync, readdirSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';
import { guionesEnHtml } from './tools/silabas.mjs';

const ROOT = dirname(fileURLToPath(import.meta.url));
const PRIMERA = 2, ULTIMA = 105; // 001 = carilla de cortesía en blanco · 106–108 = guardas finales en blanco (108 páginas, múltiplo de 4)
const LOCK = join(ROOT, 'approved.lock');
const [cmd, arg] = process.argv.slice(2);

const hash = (s) => createHash('sha256').update(s.replace(/\r\n/g, '\n')).digest('hex');
const pad = (n) => String(n).padStart(3, '0');
const pageFile = (id) => join(ROOT, 'pages', `${id}.html`);
const lock = existsSync(LOCK) ? JSON.parse(readFileSync(LOCK, 'utf8')) : {};

if (cmd === 'approve') {
  if (!arg || !existsSync(pageFile(arg))) throw new Error(`No existe la página ${arg}`);
  lock[arg] = { sha256: hash(readFileSync(pageFile(arg), 'utf8')), fecha: new Date().toISOString().slice(0, 10) };
  writeFileSync(LOCK, JSON.stringify(lock, null, 2) + '\n');
  console.log(`🔒 ${arg} aprobada y bloqueada`);
}

// Marcas de apertura de parada (15 oct. 2026, corrección de la profesora: que se note cada capítulo nuevo).
// 1 · número de parada grande en un bloque azul, a sangre en la esquina superior de afuera (en el margen de arriba);
// 2 · la línea de las 15 paradas, como en la tapa, con la parada de la apertura llena;
const marcasApertura = (n) => {
  const L = 150, x0 = 6, x1 = L - 6, paso = (x1 - x0) / 14; // en mm: «01» · línea · «15», de la columna 2 a la 6
  const puntos = Array.from({ length: 15 }, (_, i) => i + 1 === n
    ? `<circle class="apertura__actual" cx="${(x0 + i * paso).toFixed(2)}" cy="2" r="1.25"/>`
    : `<circle class="apertura__otra" cx="${(x0 + i * paso).toFixed(2)}" cy="2" r="0.75"/>`).join('');
  return `  <div class="apertura" aria-hidden="true">
    <div class="apertura__numero"><span>${String(n).padStart(2, '0')}</span></div>
    <div class="apertura__recorrido"><svg viewBox="0 0 ${L} 4"><line class="apertura__linea" x1="${x0}" y1="2" x2="${x1}" y2="2"/>${puntos}<text x="0" y="2.82">01</text><text x="${L}" y="2.82" text-anchor="end">15</text></svg></div>
  </div>
`;
};

// Páginas existentes; par = izquierda, impar = derecha (la 001 es la carilla de cortesía, a la derecha)
const pages = {};
for (const f of readdirSync(join(ROOT, 'pages')).filter((f) => /^\d{3}\.html$/.test(f)).sort()) {
  const id = f.slice(0, 3);
  const src = readFileSync(pageFile(id), 'utf8');
  if (lock[id] && lock[id].sha256 !== hash(src)) console.warn(`⚠️  La página ${id} está APROBADA y su archivo cambió desde el ${lock[id].fecha}.`);
  const side = Number(id) % 2 ? 'right' : 'left';
  const section = src.match(/data-section="([^"]*)"/)?.[1];
  // Folio + sección: solo en las páginas que declaran data-section
  const folio = section ? `  <div class="page__folio"><b>${id}</b><span>${section}</span></div>\n` : '';
  // Apertura de parada (la página que lleva el número en .stopline): número grande y recorrido
  const parada = src.match(/class="[^"]*\bstopline\b[^"]*"><b>(\d\d)<\/b>/)?.[1];
  const apertura = parada && src.includes("t-opening") ? marcasApertura(Number(parada)) : '';
  pages[id] = src.replace('class="page"', `class="page page--${side}" id="p${id}"`).replace(/<\/section>\s*$/, `${apertura}${folio}</section>\n`)
    // <!--include ruta--> inserta un archivo (mapas SVG generados por tools/mapas.mjs)
    .replace(/<!--include (\S+)-->/g, (_, file) => readFileSync(join(ROOT, file), 'utf8').trim())
    // Cuerpo de texto (clase body, y los párrafos de la introducción): guiones opcionales para el justificado
    .replace(/<(p|div) class="[^"]*(?:\bbody\b|p00[67]__text)[^"]*">[\s\S]*?<\/\1>/g, (bloque) => guionesEnHtml(bloque));
}

const slot = (n) => pages[pad(n)] ?? `<div class="slot--empty">${pad(n)} · pendiente</div>`;
const guard = (side, id) => `<section class="page page--guard page--${side}" id="${id}"></section>`;
// Tapa y contratapa: se toman de tapa/tapa.html (una sola fuente para el desplegado y el libro)
const tapaSrc = readFileSync(join(ROOT, 'tapa', 'tapa.html'), 'utf8');
const cover = (pieza, side, id) => tapaSrc.match(new RegExp(`<section class="${pieza}">[^]*?</section>`))[0]
  .replace(`class="${pieza}"`, `class="page page--cover page--${side} ${pieza}" id="${id}"`);
const spreads = [`<div class="spread"><div class="slot--empty"></div>${cover('front', 'right', 'ptapa')}</div>`,
  `<div class="spread"><div class="slot--empty"></div>${guard('right', 'p001')}</div>`];
for (let n = PRIMERA; n <= ULTIMA; n += 2) spreads.push(`<div class="spread">${slot(n)}${slot(n + 1)}</div>`);
spreads.push(`<div class="spread">${guard('left', 'p106')}${guard('right', 'p107')}</div>`,
  `<div class="spread">${guard('left', 'p108')}<div class="slot--empty"></div></div>`,
  `<div class="spread">${cover('back', 'left', 'pcontratapa')}<div class="slot--empty"></div></div>`);

// Sello de versión de los estilos: obliga al navegador a bajar los CSS nuevos cuando cambian (sin esperar su caché)
const sello = createHash('sha256').update(['styles', 'tapa'].flatMap((d) => readdirSync(join(ROOT, d)).filter((f) => f.endsWith('.css')).sort()
  .map((f) => readFileSync(join(ROOT, d, f), 'utf8'))).join('')).digest('hex').slice(0, 8);

// Sello de versión de cada imagen: si el archivo cambia, cambia su dirección y el navegador baja la nueva
// (sin esto, una imagen reemplazada con el mismo nombre se sigue viendo vieja hasta que vence la caché)
const selloImg = (ruta) => existsSync(join(ROOT, ruta)) ? `${ruta}?v=${createHash('sha256').update(readFileSync(join(ROOT, ruta))).digest('hex').slice(0, 8)}` : ruta;
const conSello = (html) => html.replace(/assets\/(?:images|maps)\/[\w.-]+\.(?:jpg|png|svg|webp)/g, selloImg);

writeFileSync(join(ROOT, 'index.html'), conSello(`<!doctype html>
<!-- GENERADO por build.mjs — no editar a mano. Editar pages/NNN.html y styles/. -->
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1280">
<title>Darwin en la Argentina — libro</title>
<link rel="stylesheet" href="styles/tokens.css?v=${sello}">
<link rel="stylesheet" href="styles/typography.css?v=${sello}">
<link rel="stylesheet" href="styles/grid.css?v=${sello}">
<link rel="stylesheet" href="styles/components.css?v=${sello}">
<link rel="stylesheet" href="styles/pages.css?v=${sello}">
<link rel="stylesheet" href="styles/maps.css?v=${sello}">
<link rel="stylesheet" href="styles/paradas.css?v=${sello}">
<link rel="stylesheet" href="styles/registros.css?v=${sello}">
<link rel="stylesheet" href="styles/tramo-03.css?v=${sello}">
<link rel="stylesheet" href="styles/tramo-04-05.css?v=${sello}">
<link rel="stylesheet" href="styles/tramo-05-07.css?v=${sello}">
<link rel="stylesheet" href="styles/tramo-07-10.css?v=${sello}">
<link rel="stylesheet" href="styles/tramo-10-15.css?v=${sello}">
<link rel="stylesheet" href="styles/fotos.css?v=${sello}">
<link rel="stylesheet" href="tapa/tapa.css?v=${sello}">
<link rel="stylesheet" href="styles/medida.css?v=${sello}">
<link rel="stylesheet" href="styles/aperturas.css?v=${sello}">
<link rel="stylesheet" href="styles/texto.css?v=${sello}">
<link rel="stylesheet" href="styles/notas.css?v=${sello}">
<link rel="stylesheet" href="styles/print.css?v=${sello}">
</head>
<body>
${spreads.join('\n')}
<script>
  const q = new URLSearchParams(location.search);
  if (q.has('grid')) document.body.classList.add('show-grid');
  if (q.get('p')) { document.body.classList.add('single'); for (const id of q.get('p').split('-')) document.getElementById('p' + id)?.classList.add('is-target'); }
  addEventListener('keydown', (e) => { if (e.key === 'g') document.body.classList.toggle('show-grid'); });
  // Pantalla: la doble página entra completa en la ventana al abrir (444 × 184 mm con el marco = 1678 × 695 px).
  // En el teléfono el viewport es de 1280 px (entra en cualquier pantalla) y esta escala hace el resto.
  // Se calcula en píxeles físicos para que el zoom del navegador siga acercando de verdad.
  const dpr0 = devicePixelRatio, raiz = document.documentElement;
  const encajar = () => {
    const k = devicePixelRatio / dpr0, w = Math.min(raiz.clientWidth, innerWidth) * k, h = innerHeight * k;
    if (w > 0 && h > 0) raiz.style.setProperty('--fit', Math.min(1, w / 1678, h / 695).toFixed(4));
  };
  encajar(); addEventListener('resize', encajar);
</script>
</body>
</html>
`));
console.log(`Libro armado: ${Object.keys(pages).length}/${ULTIMA - PRIMERA + 1} páginas · ${Object.keys(lock).length} aprobadas`);

if (cmd === 'shot' || cmd === 'pdf') {
  const chrome = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
  const url = pathToFileURL(join(ROOT, 'index.html')).href;
  const out = (name) => join(ROOT, 'salida', name);
  const run = (args) => execFileSync(chrome, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--virtual-time-budget=4000', ...args], { stdio: 'ignore' });
  if (cmd === 'pdf') {
    run([`--print-to-pdf=${out('libro.pdf')}`, '--no-pdf-header-footer', url]);
  } else {
    for (const g of ['', '-grilla'])
      run([`--screenshot=${out(`${arg}${g}.png`)}`, `--window-size=${794 * arg.split('-').length},605`, '--force-device-scale-factor=3', `${url}?p=${arg}${g ? '&grid=1' : ''}`]);
    if (!arg.includes('-')) run([`--print-to-pdf=${out(`${arg}.pdf`)}`, '--no-pdf-header-footer', `${url}?p=${arg}`]);
  }
  console.log(`Salida en salida/`);
}
