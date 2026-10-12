// Mapa de tramo de la parada 02: desembocadura del río Negro y El Carmen o Patagones (página 018).
// Genera assets/maps/tramo-02.svg. PROVISORIO: costa y cauce esquemáticos trazados con puntos
// de referencia (lat, lon). Uso: node tools/tramo02.mjs
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const OUT = join(dirname(fileURLToPath(import.meta.url)), '..', 'assets', 'maps', 'tramo-02.svg');
const W = 92.34, H = 85.5;               // 3 columnas × 19 líneas de base
const latN = -40.55, latS = -41.3, lonW = -63.5;
const k = H / (latN - latS);
const kx = k * Math.cos(((latN + latS) / 2) * Math.PI / 180);
const f = (n) => n.toFixed(2);
const xy = ([lat, lon]) => [(lon - lonW) * kx, (latN - lat) * k];

const COSTA = [[-40.85, -62.2], [-40.9, -62.3], [-40.97, -62.55], [-41.03, -62.78], [-41.07, -62.82], [-41.1, -63.0], [-41.14, -63.3], [-41.15, -63.7]];
const RIO = [[-40.43, -63.67], [-40.6, -63.35], [-40.72, -63.15], [-40.8, -62.98], [-40.92, -62.9], [-41.04, -62.79]];
const LLEGADA = [[-41.2, -62.4], [-41.12, -62.6], [-41.05, -62.76]];
const CARMEN = [-40.8, -62.98];

const suave = (pts) => {
  const q = pts.map(xy);
  let d = `M${f(q[0][0])} ${f(q[0][1])}`;
  for (let i = 0; i < q.length - 1; i++) {
    const p0 = q[i - 1] || q[i], p1 = q[i], p2 = q[i + 1], p3 = q[i + 2] || p2;
    d += `C${f(p1[0] + (p2[0] - p0[0]) / 6)} ${f(p1[1] + (p2[1] - p0[1]) / 6)} ${f(p2[0] - (p3[0] - p1[0]) / 6)} ${f(p2[1] - (p3[1] - p1[1]) / 6)} ${f(p2[0])} ${f(p2[1])}`;
  }
  return d;
};
const texto = (cls, pos, t, extra = '') => { const [x, y] = xy(pos); return `<text class="${cls}" x="${f(x)}" y="${f(y)}"${extra}>${t}</text>`; };

const o = [];
o.push(`<svg class="map" viewBox="0 0 ${W} ${H}" aria-hidden="true">`);
o.push(`<defs><clipPath id="clip-tramo02"><rect width="${W}" height="${H}"/></clipPath></defs>`);
o.push('<g clip-path="url(#clip-tramo02)">');
o.push(`<path class="map__land" d="${suave(COSTA)}L${xy([-40.3, -63.7]).map(f).join(' ')}L${xy([-40.3, -62.2]).map(f).join(' ')}Z"/>`);
{ const [, y] = xy([-41, lonW]); o.push(`<path class="map__grat" d="M0 ${f(y)}H${W}"/>`); }
{ const [x] = xy([latN, -63]); o.push(`<path class="map__grat" d="M${f(x)} 0V${H}"/>`); }
o.push(`<path class="map__coast" d="${suave(COSTA)}"/>`);
o.push(`<path class="map__river map__river--main" d="${suave(RIO)}"/>`);
o.push(`<path class="route--water" d="${suave(LLEGADA)}"/>`);
o.push('</g>');
o.push(texto('map__gratlabel', [-41, lonW], '41° S', ' dx="1" dy="-0.7"'));
o.push(texto('map__gratlabel', [latN, -63], '63° O', ' dx="0.7" dy="2.4"'));
{ const [x, y] = xy([-40.62, -63.22]); o.push(`<text class="map__place map__place--water" x="${f(x)}" y="${f(y)}" transform="rotate(27 ${f(x)} ${f(y)})">Río Negro</text>`); }
o.push(texto('map__place', [-41.075, -63.12], 'Cantiles', ' text-anchor="middle"'));
const [cx, cy] = xy(CARMEN);
o.push(`<circle class="map__stop" cx="${f(cx)}" cy="${f(cy)}" r="0.9"/>`);
o.push(`<text class="map__label" x="${f(cx + 2)}" y="${f(cy - 0.6)}">02 <tspan class="map__labelname">El Carmen o Patagones</tspan></text>`);
o.push(texto('map__note', [-41.22, -62.44], 'Llegada del <tspan font-style="italic">Beagle</tspan>,', ' text-anchor="end" dx="-2"'));
o.push(texto('map__note', [-41.22, -62.44], '3 ago. 1833', ' text-anchor="end" dx="-2" dy="2.8"'));
const km20 = (20 / 111.2) * k;
o.push(`<path class="map__scale" d="M5 ${f(H - 5)}v1.2h${f(km20)}v-1.2"/>`);
o.push(`<text class="map__gratlabel" x="5" y="${f(H - 6)}">0</text><text class="map__gratlabel" x="${f(5 + km20)}" y="${f(H - 6)}" text-anchor="end">20 km</text>`);
o.push(`<rect class="map__border" x="0.125" y="0.125" width="${f(W - 0.25)}" height="${f(H - 0.25)}"/>`);
o.push('</svg>');

writeFileSync(OUT, o.join('\n') + '\n');
console.log('Mapa de tramo 02 generado · lon', lonW, 'a', (lonW + W / kx).toFixed(2));
