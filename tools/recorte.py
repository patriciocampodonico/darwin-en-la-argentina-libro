# Recorta los mockups fotográficos de la página 007 de su fondo gris (fondo y sombra → transparente).
# Uso: py tools/recorte.py   (originales en assets/images/originales/mockup-*.webp)
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as nd

IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'images')

def guardar(im, mask, name):
    alpha = mask.filter(ImageFilter.GaussianBlur(0.7))
    out = im.convert('RGBA'); out.putalpha(alpha)
    out = out.crop(alpha.getbbox())
    out.save(os.path.join(IMG, name)); print(name, out.size)

# Web: la notebook es geométrica → pantalla y base como rectángulos redondeados (medidos sobre el original)
im = Image.open(os.path.join(IMG, 'originales', 'mockup-web.webp')).convert('RGB')
mask = Image.new('L', [s * 4 for s in im.size], 0); d = ImageDraw.Draw(mask)
d.rounded_rectangle([220 * 4, 122 * 4, 1316 * 4, 830 * 4], radius=26 * 4, fill=255)
d.rounded_rectangle([118 * 4, 825 * 4, 1419 * 4, 853 * 4], radius=7 * 4, fill=255)
guardar(im, mask.resize(im.size, Image.LANCZOS), '007-mockup-web.png')

# Libro: el fondo y la sombra son grises neutros; papel y tapa tienen color → máscara por saturación,
# extendida hacia abajo para incluir el canto de las hojas (gris, igual que la sombra)
im = Image.open(os.path.join(IMG, 'originales', 'mockup-libro.webp')).convert('RGB')
a = np.asarray(im.filter(ImageFilter.GaussianBlur(1.2))).astype(int)
obj = (a.max(2) - a.min(2)) > 6
obj = nd.binary_fill_holes(nd.binary_opening(obj, iterations=2))
lab, n = nd.label(obj)
obj = lab == (np.argmax(nd.sum(obj, lab, range(1, n + 1))) + 1)
obj = nd.binary_dilation(obj, structure=np.ones((33, 1)), origin=(-16, 0)) | obj
obj = nd.binary_fill_holes(obj)
obj = nd.gaussian_filter(obj.astype(float), 3) > 0.5  # borde liso
guardar(im, Image.fromarray((obj * 255).astype('uint8')), '007-mockup-libro.png')

# Fichas: son tres rectángulos en perspectiva. De cada una se toma la envolvente convexa de sus píxeles con color
# (papel cálido, R > B; tinta y reverso azules, B > R; el fondo y las sombras son grises neutros), dentro de una
# zona aproximada marcada a mano. Así los bordes salen rectos y sin halo de sombra.
from shapely.geometry import Polygon, MultiPoint
from shapely.ops import unary_union
im = Image.open(os.path.join(IMG, 'originales', '007-mockup-fichas.webp')).convert('RGB')
a = np.asarray(im.filter(ImageFilter.GaussianBlur(1.2))).astype(int)
rb = a[..., 0] - a[..., 2]
col = nd.binary_opening((rb >= 5) | (rb <= -14), iterations=2)
ZONAS = [[(150, 170), (632, 68), (785, 745), (300, 856)],     # Megatherium, con el canto de la pila
         [(728, 50), (1167, 80), (1092, 713), (655, 683)],    # Guanaco
         [(1190, 95), (1655, 165), (1570, 835), (1080, 750)]] # reverso azul
formas = []
for q in ZONAS:
    roi = Image.new('L', im.size, 0); ImageDraw.Draw(roi).polygon(list(Polygon(q).buffer(10).exterior.coords), fill=255)
    ys, xs = np.where(col & (np.asarray(roi) > 0))
    formas.append(MultiPoint(list(zip(xs[::5], ys[::5]))).convex_hull.simplify(2.5).buffer(-1.2, join_style=2))
forma = unary_union(formas)
K = 4
mask = Image.new('L', (im.width * K, im.height * K), 0); dr = ImageDraw.Draw(mask)
for g in getattr(forma, 'geoms', [forma]):
    dr.polygon([(x * K, y * K) for x, y in g.exterior.coords], fill=255)
guardar(im, mask.resize(im.size, Image.LANCZOS), '007-mockup-fichas.png')
