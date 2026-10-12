# Prepara la cartografía real de los mapas a partir de Natural Earth 1:10m (dominio público,
# naturalearthdata.com; versión «punto de vista argentino», con las Malvinas dentro de la Argentina).
# Recorta y simplifica para cada mapa y escribe assets/maps/geo.json, que leen tools/mapas.mjs y tramo0N.mjs.
# Uso: py tools/geodatos.py <carpeta con los .geojson de Natural Earth>
#   ne_10m_admin_0_countries_arg · ne_10m_rivers_lake_centerlines · ne_10m_lakes
import json, os, sys
from shapely.geometry import shape, box, mapping
from shapely.ops import unary_union, linemerge

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'maps', 'geo.json')
leer = lambda n: json.load(open(os.path.join(SRC, n + '.geojson'), encoding='utf-8'))['features']

# mapa: (lonO, latS, lonE, latN), tolerancia de simplificación en grados, decimales, ríos y lagos que entran
MAPAS = {
    'general': ((-72.5, -55.6, -56.0, -30.5), 0.02, 3, ['Paraná', 'Uruguay', 'Salado', 'Colorado', 'Negro', 'Chubut', 'Deseado', 'Santa Cruz'], ['Lago Argentino', 'Lago Viedma', 'Lago Buenos Aires']),
    'detalle': ((-65.6, -41.3, -56.2, -31.0), 0.008, 3, ['Paraná', 'Uruguay', 'Salado', 'Colorado', 'Negro', 'Carcarañá'], []),
    'tramo01': ((-66.65, -55.05, -63.65, -54.35), 0.0008, 4, [], []),
    'tramo02': ((-63.5, -41.3, -62.4, -40.55), 0.0008, 4, ['Negro'], []),
}

paises = {f['properties']['ADM0_A3']: shape(f['geometry']).buffer(0) for f in leer('ne_10m_admin_0_countries_arg')
          if f['properties']['ADM0_A3'] in ('ARG', 'CHL', 'URY', 'BRA', 'PRY', 'BOL')}
arg = paises['ARG']
otros = unary_union([g for k, g in paises.items() if k != 'ARG'])
tierra = unary_union(list(paises.values()))
rios = [(f['properties'].get('name'), shape(f['geometry'])) for f in leer('ne_10m_rivers_lake_centerlines') if f['geometry']]
lagos = [(f['properties'].get('name'), shape(f['geometry'])) for f in leer('ne_10m_lakes')]

def anillos(g, nd, area_min=0):
    out = []
    for p in getattr(g, 'geoms', [g]):
        if p.geom_type == 'Polygon' and not p.is_empty and p.area >= area_min:
            out.append([[round(x, nd), round(y, nd)] for x, y in p.exterior.coords])
    return out
def lineas(g, nd):
    if g.is_empty: return []
    if g.geom_type in ('MultiLineString', 'GeometryCollection'): g = linemerge([l for l in g.geoms if l.geom_type == 'LineString']) if len(g.geoms) else g
    return [[[round(x, nd), round(y, nd)] for x, y in l.coords] for l in getattr(g, 'geoms', [g]) if l.geom_type == 'LineString' and len(l.coords) > 1]

geo = {'fuente': 'Natural Earth 1:10m (dominio público), punto de vista argentino'}
for nombre, (bb, tol, nd, rs, ls) in MAPAS.items():
    m = 0.4 if tol > 0.001 else 0.05
    caja = box(bb[0] - m, bb[1] - m, bb[2] + m, bb[3] + m)
    amin = (tol * 3) ** 2
    costa = tierra.boundary.intersection(caja).simplify(tol)
    limite = arg.boundary.intersection(otros.buffer(0.002)).intersection(caja).simplify(tol)
    geo[nombre] = {
        'arg': anillos(arg.intersection(caja).simplify(tol), nd, amin),
        'otros': anillos(otros.intersection(caja).simplify(tol), nd, amin),
        'costa': lineas(costa, nd),
        'limite': lineas(limite, nd),
        'rios': {n: lineas(unary_union([g for k, g in rios if k == n]).intersection(caja).simplify(tol), nd) for n in rs},
        'lagos': {n: anillos(unary_union([g for k, g in lagos if k == n]).simplify(tol), nd) for n in ls},
    }
    d = geo[nombre]
    print(nombre, 'puntos:', sum(len(r) for k in ('arg', 'otros', 'costa', 'limite') for r in d[k]), '· ríos', {n: len(v) for n, v in d['rios'].items()})
json.dump(geo, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(OUT, round(os.path.getsize(OUT) / 1024), 'KB')
