// Mapa de tramo de la parada 01: aproximación a la bahía del Buen Suceso (página 013).
// Genera assets/maps/tramo-01.svg. Costa real: Natural Earth 1:10m (assets/maps/geo.json,
// tools/geodatos.py); los topónimos son los que nombra Darwin el 17 de diciembre de 1832.
// Uso: node tools/tramo01.mjs
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const OUT = join(dirname(fileURLToPath(import.meta.url)), '..', 'assets', 'maps', 'tramo-01.svg');
const W = 188, H = 76.5;                 // 6 columnas × 17 líneas de base
const latN = -54.35, latS = -55.05, lonW = -66.65;
const k = H / (latN - latS);
const kx = k * Math.cos(((latN + latS) / 2) * Math.PI / 180);
const f = (n) => n.toFixed(2);
const xy = ([lat, lon]) => [(lon - lonW) * kx, (latN - lat) * k];

const G = JSON.parse(readFileSync(join(dirname(OUT), 'geo.json'), 'utf8')).tramo01;
const traza = (lineas, cerrar) => lineas.map((l) => l.map(([lon, lat]) => xy([lat, lon])).map(([x, y], i) => `${i ? 'L' : 'M'}${f(x)} ${f(y)}`).join('') + (cerrar ? 'Z' : '')).join('');
const RUTA = [[-54.3, -64.62], [-54.5, -64.88], [-54.62, -64.96], [-54.72, -65.02], [-54.79, -65.12], [-54.8, -65.215]];
const BAHIA = [-54.8, -65.225];

const suave = (pts, cerrar) => {
  const q = pts.map(xy);
  let d = `M${f(q[0][0])} ${f(q[0][1])}`;
  for (let i = 0; i < q.length - 1; i++) {
    const p0 = q[i - 1] || q[i], p1 = q[i], p2 = q[i + 1], p3 = q[i + 2] || p2;
    d += `C${f(p1[0] + (p2[0] - p0[0]) / 6)} ${f(p1[1] + (p2[1] - p0[1]) / 6)} ${f(p2[0] - (p3[0] - p1[0]) / 6)} ${f(p2[1] - (p3[1] - p1[1]) / 6)} ${f(p2[0])} ${f(p2[1])}`;
  }
  return d + (cerrar ? 'Z' : '');
};
const texto = (cls, pos, t, extra = '') => { const [x, y] = xy(pos); return `<text class="${cls}" x="${f(x)}" y="${f(y)}"${extra}>${t}</text>`; };

const o = [];
o.push(`<svg class="map" viewBox="0 0 ${W} ${H}" aria-hidden="true">`);
o.push(`<defs><clipPath id="clip-tramo01"><rect width="${W}" height="${H}"/></clipPath></defs>`);
o.push('<g clip-path="url(#clip-tramo01)">');
o.push(`<path class="map__land" d="${traza(G.arg, true)}"/>`);
for (const lat of [-54.5, -55]) { const [, y] = xy([lat, lonW]); o.push(`<path class="map__grat" d="M0 ${f(y)}H${W}"/>`); }
for (const lon of [-66, -65, -64]) { const [x] = xy([latN, lon]); o.push(`<path class="map__grat" d="M${f(x)} 0V${H}"/>`); }
o.push(`<path class="map__coast" d="${traza(G.costa)}"/>`);
o.push(`<path class="route--water" d="${suave(RUTA)}"/>`);
o.push('</g>');
// retícula
o.push(texto('map__gratlabel', [-54.5, lonW], '54° 30′ S', ` dx="1" dy="-0.7"`));
o.push(texto('map__gratlabel', [-55, lonW], '55° S', ` dx="1" dy="-0.7"`));
for (const lon of [-66, -65, -64]) o.push(texto('map__gratlabel', [latN, lon], `${-lon}° O`, ` dx="0.7" dy="2.4"`));
// topónimos del texto de Darwin
o.push(texto('map__place', [-54.74, -66.05], 'Tierra del Fuego', ' text-anchor="middle"'));
o.push(texto('map__place', [-54.575, -65.17], 'Cabo San Diego', ' text-anchor="end"'));
{ const [x, y] = xy([-54.8, -64.9]); o.push(`<text class="map__place map__place--water" x="${f(x)}" y="${f(y)}" text-anchor="middle" transform="rotate(-90 ${f(x)} ${f(y)})">Estrecho de Le Maire</text>`); }
o.push(texto('map__place', [-54.645, -64.26], 'Isla de los Estados', ' text-anchor="middle"'));
// parada
const [bx, by] = xy(BAHIA);
o.push(`<circle class="map__stop" cx="${f(bx)}" cy="${f(by)}" r="0.9"/>`);
o.push(`<text class="map__label" x="${f(bx - 2)}" y="${f(by + 0.9)}" text-anchor="end">01 <tspan class="map__labelname">Bahía del Buen Suceso</tspan></text>`);
// rótulo del recorrido y escala (20 km)
o.push(texto('map__note', [-54.43, -64.72], 'Llegada del <tspan font-style="italic">Beagle</tspan>, 17 dic. 1832', ' dx="2"'));
const km20 = (20 / 111.2) * k;
o.push(`<path class="map__scale" d="M${f(W - 6 - km20)} ${f(H - 5)}v1.2h${f(km20)}v-1.2"/>`);
o.push(`<text class="map__gratlabel" x="${f(W - 6 - km20)}" y="${f(H - 6)}">0</text><text class="map__gratlabel" x="${f(W - 6)}" y="${f(H - 6)}" text-anchor="end">20 km</text>`);
o.push(`<rect class="map__border" x="0.125" y="0.125" width="${W - 0.25}" height="${H - 0.25}"/>`);
o.push('</svg>');

writeFileSync(OUT, o.join('\n') + '\n');
console.log('Mapa de tramo 01 generado · lon', lonW, 'a', (lonW + W / kx).toFixed(2));
