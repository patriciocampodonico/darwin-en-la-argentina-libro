// Genera los mapas vectoriales del recorrido (assets/maps/general.svg y detalle.svg)
// a partir de coordenadas geográficas (lat, lon). Proyección equirrectangular simple.
// Cartografía: Natural Earth 1:10m (assets/maps/geo.json, preparado por tools/geodatos.py):
// costa, límite internacional, ríos y lagos reales. Las Malvinas van como parte de la Argentina.
// Paradas y recorrido: lugares que nombra el diario, en su posición actual. Uso: node tools/mapas.mjs
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const OUT = join(dirname(fileURLToPath(import.meta.url)), '..', 'assets', 'maps');
const GEO = JSON.parse(readFileSync(join(OUT, 'geo.json'), 'utf8'));

// ── Paradas: lugar actual de cada punto del diario ───────────
const P = {
  '01': [-54.8, -65.23],   // bahía Buen Suceso
  '02': [-40.8, -62.99],   // Carmen de Patagones
  '03': [-39.5, -62.68],   // paso del río Colorado (campamento de Rosas)
  '04': [-39.12, -62.47],  // camino del Colorado a Bahía Blanca (punto medio del tramo)
  '05': [-38.8, -62.17],   // entre el fuerte de Bahía Blanca y Punta Alta
  '06': [-38.07, -61.98],  // sierra de la Ventana
  '07': [-36.35, -60.02],  // Tapalqué (travesía de las Pampas)
  '08': [-34.6, -58.38],   // Buenos Aires
  '09': [-32.95, -60.65],  // Rosario
  '10': [-31.63, -60.7],   // Santa Fe
  '11': [-31.73, -60.53],  // Bajada (Paraná)
  '13': [-47.75, -65.9],   // Puerto Deseado
  '14': [-49.31, -67.73],  // Puerto San Julián
  '15': [-50.02, -68.52],  // río Santa Cruz (fondeadero)
};
const REGISTRO = ['01', '05', '09', '13', '14']; // paradas con página de registro, inventario o especie en el v2

const TIERRA = [ // a caballo, posta por posta según el diario: 02 → 10
  P['02'], P['03'], P['04'], [-38.72, -62.27] /* fuerte de Bahía Blanca */, P['05'],
  [-38.5, -61.8] /* posta del río Sauce */, P['06'], [-37.75, -61.35], [-36.95, -60.35] /* sierra Tapalguen */, P['07'],
  [-35.44, -58.81] /* Guardia del Monte */, P['08'],
  [-34.57, -59.11] /* Luján */, [-34.25, -59.47] /* Areco */, [-34.06, -60.1] /* río Arrecifes */, [-33.33, -60.22] /* San Nicolás */,
  P['09'], [-31.97, -60.92] /* Coronda */, P['10'],
];
const SANTA_CRUZ = GEO.general.rios['Santa Cruz'].flat().filter(([lon]) => lon > -71.3 && lon < -68.6)
  .sort((a, b) => b[0] - a[0]).map(([lon, lat]) => [lat, lon]); // remontada por el cauce real; se detiene antes de la Cordillera
const AGUA = [ // cruce a Bajada · regreso por el Paraná · navegación a Patagonia · río Santa Cruz
  [P['10'], P['11']],
  [P['11'], [-32.2, -60.6], [-32.95, -60.58], [-33.3, -60.15], [-33.7, -59.55], [-34.05, -59.05], [-34.42, -58.58] /* Las Conchas */, P['08']],
  [P['08'], [-34.95, -57.5], [-35.5, -56.4], [-36.6, -55.9], [-38.5, -57.0], [-40.6, -60.2], [-43.0, -63.0], [-45.5, -65.0], [-47.3, -65.3], P['13']],
  [P['13'], [-48.3, -65.8], [-49.0, -67.0], P['14']],
  [P['14'], [-49.7, -67.45], [-50.13, -68.3], P['15']],
  [P['15'], ...SANTA_CRUZ],
];

// ── Dibujo ─────────────────────────────────────────────────────
const f = (n) => n.toFixed(2);

function mapa({ nombre, latN, latS, lonW, W, H, gratLat, gratLon, etiquetas, extra }) {
  const k = H / (latN - latS);
  const lat0 = (latN + latS) / 2;
  const kx = k * Math.cos((lat0 * Math.PI) / 180);
  const lonE = lonW + W / kx;
  const xy = ([lat, lon]) => [(lon - lonW) * kx, (latN - lat) * k];
  const suave = (pts, cerrar = false) => {
    const q = pts.map(xy);
    let d = `M${f(q[0][0])} ${f(q[0][1])}`;
    for (let i = 0; i < q.length - 1; i++) {
      const p0 = q[i - 1] || q[i], p1 = q[i], p2 = q[i + 1], p3 = q[i + 2] || p2;
      d += `C${f(p1[0] + (p2[0] - p0[0]) / 6)} ${f(p1[1] + (p2[1] - p0[1]) / 6)} ${f(p2[0] - (p3[0] - p1[0]) / 6)} ${f(p2[1] - (p3[1] - p1[1]) / 6)} ${f(p2[0])} ${f(p2[1])}`;
    }
    return d + (cerrar ? 'Z' : '');
  };
  const recta = (pts) => pts.map(xy).map(([x, y], i) => `${i ? 'L' : 'M'}${f(x)} ${f(y)}`).join('');
  const G = GEO[nombre];
  const traza = (lineas, cerrar) => lineas.map((l) => l.map(([lon, lat]) => xy([lat, lon])).map(([x, y], i) => `${i ? 'L' : 'M'}${f(x)} ${f(y)}`).join('') + (cerrar ? 'Z' : '')).join('');
  const o = [];
  o.push(`<svg class="map" viewBox="0 0 ${f(W)} ${f(H)}" aria-hidden="true">`);
  o.push(`<defs><clipPath id="clip-${W | 0}"><rect width="${f(W)}" height="${f(H)}"/></clipPath></defs>`);
  o.push(`<g clip-path="url(#clip-${W | 0})">`);
  // tierra: países vecinos en tono más claro, la Argentina en el tono del sistema
  o.push(`<path class="map__land map__land--otro" d="${traza(G.otros, true)}"/>`);
  o.push(`<path class="map__land" d="${traza(G.arg, true)}"/>`);
  // retícula
  for (const lat of gratLat) { const [, y] = xy([lat, lonW]); o.push(`<path class="map__grat" d="M0 ${f(y)}H${f(W)}"/>`); }
  for (const lon of gratLon) { const [x] = xy([latN, lon]); o.push(`<path class="map__grat" d="M${f(x)} 0V${f(H)}"/>`); }
  // ríos, lagos, costa y límite internacional
  for (const rio of Object.values(G.rios)) o.push(`<path class="map__river" d="${traza(rio)}"/>`);
  for (const lago of Object.values(G.lagos)) o.push(`<path class="map__lake" d="${traza(lago, true)}"/>`);
  o.push(`<path class="map__limit" d="${traza(G.limite)}"/>`);
  o.push(`<path class="map__coast" d="${traza(G.costa)}"/>`);
  // recorridos
  o.push(`<path class="route--land" d="${suave(TIERRA)}"/>`);
  for (const tramo of AGUA) o.push(`<path class="route--water" d="${suave(tramo)}"/>`);
  o.push('</g>');
  // rótulos de la retícula
  for (const lat of gratLat) { const [, y] = xy([lat, lonW]); o.push(`<text class="map__gratlabel" x="${f(W - 1)}" y="${f(y - 0.7)}" text-anchor="end">${-lat}° S</text>`); }
  for (const lon of gratLon) { const [x] = xy([latN, lon]); o.push(`<text class="map__gratlabel" x="${f(x + 0.7)}" y="${f(H - 1)}">${-lon}° O</text>`); }
  // paradas
  for (const [id, pos] of Object.entries(P)) {
    const [x, y] = xy(pos);
    if (x < 0 || x > W || y < 0 || y > H) continue;
    o.push(`<circle class="map__stop" cx="${f(x)}" cy="${f(y)}" r="${etiquetas.r}"/>`);
    const e = etiquetas[id];
    if (!e) continue;
    const dx = e.lado === 'izq' ? -1.7 : 1.7;
    o.push(`<text class="map__label" x="${f(x + dx)}" y="${f(y + 0.85 + (e.dy || 0))}"${e.lado === 'izq' ? ' text-anchor="end"' : ''}>${e.texto || id}</text>`);
    if (REGISTRO.includes(id)) {
      const rx = x - dx * 1.25, ry = y + (e.ry || 0), s = 0.85;
      o.push(`<path class="map__reg" d="M${f(rx)} ${f(ry - s)}L${f(rx + s)} ${f(ry)}L${f(rx)} ${f(ry + s)}L${f(rx - s)} ${f(ry)}Z"/>`);
    }
  }
  if (extra) o.push(extra({ xy, f }));
  o.push(`<rect class="map__border" x="0.125" y="0.125" width="${f(W - 0.25)}" height="${f(H - 0.25)}"/>`);
  o.push('</svg>');
  return { svg: o.join('\n'), lonE, xy };
}

// Detalle: de Carmen de Patagones a Santa Fe (3 columnas × 28 líneas)
const DET = { latN: -31, latS: -41.3, lonW: -65.6, W: 92.34, H: 126 };
const detalle = mapa({
  nombre: 'detalle', ...DET, gratLat: [-32, -34, -36, -38, -40], gratLon: [-64, -62, -60, -58],
  etiquetas: {
    r: 0.8,
    '02': { lado: 'izq' }, '03': { lado: 'izq' }, '04': { lado: 'izq' }, '05': { lado: 'izq', dy: -0.6, ry: 0.3 },
    '06': { lado: 'der' }, '07': { lado: 'der' }, '08': { lado: 'der', texto: '08 · 12' },
    '09': { lado: 'izq' }, '10': { lado: 'izq', dy: -0.5 }, '11': { lado: 'der', dy: 0.6 },
  },
  extra: ({ xy, f }) => { // la navegación sigue fuera del recuadro, hacia la parada 13
    const [x, y] = xy([-40.6, -59.7]);
    return `<text class="map__note" x="${f(x)}" y="${f(y)}">hacia 13</text>`;
  },
});

// General: todo el recorrido (2 columnas × 28 líneas), con el recuadro del detalle
const general = mapa({
  nombre: 'general', latN: -30.5, latS: -55.6, lonW: -72.5, W: 60.34, H: 126,
  gratLat: [-35, -40, -45, -50, -55], gratLon: [-70, -65, -60],
  etiquetas: { r: 0.6, '01': { lado: 'der' }, '13': { lado: 'der' }, '14': { lado: 'der', dy: -0.4 }, '15': { lado: 'der', dy: 1.2 } },
  extra: ({ xy, f }) => {
    const [x0, y0] = xy([DET.latN, DET.lonW]);
    const [x1, y1] = xy([DET.latS, detalle.lonE]);
    return `<rect class="map__frame" x="${f(x0)}" y="${f(y0)}" width="${f(x1 - x0)}" height="${f(y1 - y0)}"/>` +
      `<text class="map__note" x="${f(x1 - 0.6)}" y="${f(y1 + 3)}" text-anchor="end">02–12 · ver detalle</text>`;
  },
});

writeFileSync(join(OUT, 'general.svg'), general.svg + '\n');
writeFileSync(join(OUT, 'detalle.svg'), detalle.svg + '\n');
console.log('Mapas generados: general.svg (lon', -72.5, 'a', general.lonE.toFixed(1) + ') · detalle.svg (lon', DET.lonW, 'a', detalle.lonE.toFixed(1) + ')');
