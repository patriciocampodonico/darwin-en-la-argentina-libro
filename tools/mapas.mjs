// Genera los mapas vectoriales del recorrido (assets/maps/general.svg y detalle.svg)
// a partir de coordenadas geográficas (lat, lon). Proyección equirrectangular simple.
// PROVISORIO: la costa es un trazado esquemático hecho con puntos de referencia
// (ciudades, cabos, desembocaduras), no un contorno cartográfico oficial.
// Las paradas son orientativas. Uso: node tools/mapas.mjs
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const OUT = join(dirname(fileURLToPath(import.meta.url)), '..', 'assets', 'maps');

// ── Geografía (lat, lon) ───────────────────────────────────────
const COSTA_NORTE = [ // Río de la Plata (orilla norte) → costa bonaerense → río Negro → golfo San Matías
  [-34.88, -56.0], [-34.9, -56.2], [-34.78, -56.36], [-34.7, -56.75], [-34.43, -57.35], [-34.47, -57.85],
  [-34.0, -58.29], [-33.88, -58.42], [-34.2, -58.5], [-34.42, -58.58], [-34.6, -58.37], [-34.72, -58.25],
  [-34.82, -57.97], [-35.07, -57.52], [-35.27, -57.23], [-35.43, -57.13], [-35.75, -57.38], [-36.0, -57.35],
  [-36.3, -56.93], [-36.36, -56.72], [-36.72, -56.68], [-37.11, -56.86], [-37.26, -56.97], [-37.74, -57.42],
  [-38.03, -57.53], [-38.28, -57.84], [-38.58, -58.72], [-38.86, -60.08], [-38.99, -61.3], [-39.0, -61.55],
  [-38.9, -62.05], [-38.79, -62.27], [-38.85, -62.45], [-39.05, -62.3], [-39.25, -62.05], [-39.45, -62.05],
  [-39.85, -62.1], [-40.2, -62.3], [-40.55, -62.23], [-40.85, -62.3], [-41.03, -62.78], [-41.13, -63.3],
  [-41.12, -64.0], [-40.9, -64.6], [-40.75, -64.95], [-40.95, -65.15], [-41.3, -65.1],
];
const COSTA_SUR = [ // golfo San Matías → Patagonia → estrecho de Magallanes
  [-41.5, -65.02], [-42.0, -65.07], [-42.2, -64.6], [-42.08, -63.77], [-42.77, -63.63], [-42.6, -64.3],
  [-42.77, -65.03], [-42.95, -64.6], [-42.97, -64.32], [-43.33, -65.05], [-44.05, -65.22], [-44.8, -65.72],
  [-44.92, -65.53], [-45.13, -66.53], [-45.87, -67.48], [-46.44, -67.52], [-46.75, -67.0], [-47.2, -65.75],
  [-47.75, -65.9], [-48.05, -65.93], [-48.4, -66.45], [-48.9, -67.2], [-49.3, -67.72], [-49.75, -67.75],
  [-50.12, -68.38], [-50.95, -69.15], [-51.6, -68.98], [-52.33, -68.35], [-52.4, -69.2], [-52.5, -69.6],
  [-52.65, -70.3], [-52.75, -70.75], [-53.15, -70.92], [-53.6, -70.95], [-53.9, -71.3], [-53.6, -72.5],
];
const TIERRA_DEL_FUEGO = [
  [-52.66, -68.6], [-53.1, -68.25], [-53.3, -68.2], [-53.78, -67.7], [-54.0, -67.3], [-54.28, -66.7],
  [-54.5, -66.0], [-54.65, -65.12], [-54.82, -65.25], [-54.95, -65.9], [-55.0, -66.6], [-54.82, -68.3],
  [-54.9, -69.5], [-54.6, -70.5], [-54.3, -70.9], [-53.9, -70.3], [-53.3, -70.37], [-52.9, -70.1], [-52.75, -69.5],
];
const ISLAS = [
  [[-54.72, -64.7], [-54.7, -64.0], [-54.78, -63.8], [-54.88, -64.3], [-54.85, -64.72]],                       // de los Estados
  [[-51.3, -60.6], [-51.35, -59.6], [-51.75, -59.5], [-52.2, -60.0], [-52.1, -60.9], [-51.6, -61.2]],           // Gran Malvina
  [[-51.3, -59.0], [-51.35, -57.8], [-51.7, -57.75], [-52.3, -58.6], [-52.2, -59.4], [-51.8, -59.2]],           // Soledad
];
const RIOS = {
  parana: [[-30.5, -59.6], [-30.74, -59.65], [-31.73, -60.6], [-32.95, -60.6], [-33.33, -60.18], [-33.68, -59.62], [-34.1, -59.0], [-34.3, -58.55]],
  colorado: [[-37.77, -67.72], [-38.8, -64.9], [-39.02, -64.08], [-39.5, -62.68], [-39.85, -62.1]],
  negro: [[-38.95, -68.06], [-39.27, -65.67], [-40.1, -64.45], [-40.8, -62.98], [-41.03, -62.78]],
  santaCruz: [[-50.25, -72.1], [-50.2, -71.0], [-50.25, -70.0], [-49.98, -68.91], [-50.12, -68.38]],
};

// ── Paradas (orientativas) ─────────────────────────────────────
const P = {
  '01': [-54.8, -65.25], '02': [-40.8, -62.98], '03': [-39.5, -62.68], '04': [-39.15, -62.45], '05': [-38.8, -62.17],
  '06': [-38.13, -61.95], '07': [-36.35, -60.02], '08': [-34.6, -58.38], '09': [-32.95, -60.65], '10': [-31.63, -60.72],
  '11': [-31.73, -60.5], '13': [-47.75, -65.9], '14': [-49.31, -67.73], '15': [-50.02, -68.52],
};
const REGISTRO = ['01', '05', '09', '13', '14']; // paradas con página de registro, inventario o especie en el v2

const TIERRA = [ // a caballo: 02 → 10
  P['02'], P['03'], P['04'], P['05'], P['06'], P['07'], [-35.44, -58.8], P['08'],
  [-34.57, -59.1], [-34.25, -59.47], [-33.33, -60.28], P['09'], [-31.97, -60.92], P['10'],
];
const AGUA = [ // cruce a Bajada · regreso por el Paraná · navegación a Patagonia · río Santa Cruz
  [P['10'], P['11']],
  [P['11'], [-32.2, -60.45], [-32.95, -60.48], [-33.3, -60.05], [-33.7, -59.5], [-34.1, -58.88], [-34.35, -58.48], P['08']],
  [P['08'], [-35.0, -57.5], [-35.6, -56.7], [-37.3, -56.5], [-39.5, -58.5], [-42.5, -62.5], [-45.5, -64.8], [-47.4, -65.4], P['13']],
  [P['13'], [-48.5, -66.0], [-49.2, -67.3], P['14']],
  [P['14'], [-49.7, -67.4], P['15']],
  [P['15'], [-49.98, -68.91], [-50.25, -70.0], [-50.2, -71.0], [-50.2, -71.3]], // se detiene antes de la Cordillera
];

// ── Dibujo ─────────────────────────────────────────────────────
const f = (n) => n.toFixed(2);

function mapa({ latN, latS, lonW, W, H, gratLat, gratLon, etiquetas, extra }) {
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
  const costa = [...COSTA_NORTE, ...COSTA_SUR];
  const o = [];
  o.push(`<svg class="map" viewBox="0 0 ${f(W)} ${f(H)}" aria-hidden="true">`);
  o.push(`<defs><clipPath id="clip-${W | 0}"><rect width="${f(W)}" height="${f(H)}"/></clipPath></defs>`);
  o.push(`<g clip-path="url(#clip-${W | 0})">`);
  // tierra: costa + cierre por el oeste y el norte
  o.push(`<path class="map__land" d="${suave(costa)}${recta([[-60, -80], [-25, -80], [-25, -50], [-34.88, -50]]).replace('M', 'L')}Z"/>`);
  o.push(`<path class="map__land" d="${suave(TIERRA_DEL_FUEGO, true)}"/>`);
  for (const isla of ISLAS) o.push(`<path class="map__land" d="${suave(isla, true)}"/>`);
  // retícula
  for (const lat of gratLat) { const [, y] = xy([lat, lonW]); o.push(`<path class="map__grat" d="M0 ${f(y)}H${f(W)}"/>`); }
  for (const lon of gratLon) { const [x] = xy([latN, lon]); o.push(`<path class="map__grat" d="M${f(x)} 0V${f(H)}"/>`); }
  // costa y ríos
  o.push(`<path class="map__coast" d="${suave(costa)}"/>`);
  o.push(`<path class="map__coast" d="${suave(TIERRA_DEL_FUEGO, true)}"/>`);
  for (const isla of ISLAS) o.push(`<path class="map__coast" d="${suave(isla, true)}"/>`);
  for (const r of Object.values(RIOS)) o.push(`<path class="map__river" d="${suave(r)}"/>`);
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
  ...DET, gratLat: [-32, -34, -36, -38, -40], gratLon: [-64, -62, -60, -58],
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
  latN: -30.5, latS: -55.6, lonW: -72.5, W: 60.34, H: 126,
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
