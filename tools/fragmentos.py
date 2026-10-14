# Fragmentos de las láminas del libro para el mosaico de la página 005 (caja 28,4 × 31,5 mm).
# Uso: py tools/fragmentos.py   (el de «Mapa» sale de salida/008.png: antes, node build.mjs shot 008)
import os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'assets', 'images')
INK, PAPER = '#1A3A5C', '#EFEEE6'
AR = 31.5 / 28.42

# nombre, origen, x0, y0, ancho del recorte (el alto sale de la proporción), lámina sin procesar
FRAGMENTOS = [
    ('fosil', 'originales/tapa-megatherium.webp', 520, 300, 440, True),
    ('ave', '079-picotijera.jpg', 1250, 200, 640, False),
    ('planta', '014a-fagus-betuloides.jpg', 100, 200, 900, False),
    ('rio', '103-santa-cruz.jpg', 500, 173, 754, False),
    ('montana', '049-horizonte-sierra.jpg', 0, 200, 560, False),
    ('mapa', '../../salida/008.png', 1600, 850, 600, False),
]
for name, src, x, y, w, raw in FRAGMENTOS:
    im = Image.open(os.path.join(IMG, src))
    im = im.crop((x, y, x + w, y + round(w * AR)))
    if raw:  # mismo paso a dos tintas que tools/fotos.py
        g = im.convert('L')
        lut = [min(255, round(255 * (v - 40) / (228 - 40))) if v > 40 else 0 for v in range(256)]
        im = ImageOps.colorize(g.point(lut), black=INK, white=PAPER)
    im.convert('RGB').save(os.path.join(IMG, f'005-{name}.jpg'), quality=92)
    print(name, im.size, round(w / 28.42 * 25.4), 'ppp')
