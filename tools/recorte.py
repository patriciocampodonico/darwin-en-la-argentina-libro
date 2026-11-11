# Recorta los mockups fotográficos de la página 005 de su fondo gris (fondo y sombra → transparente).
# Uso: py tools/recorte.py   (originales en assets/images/originales/mockup-*.webp)
# 11 nov. 2026: libro y fichas pasan a los mockups nuevos de la web (Acerca de): mockup-libro-2026.webp y 005-mockup-fichas-2026.webp
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

# Web: notebook y teléfono son geométricos → rectángulos redondeados medidos sobre el original
# (mockup-web-2.webp, 12 oct. 2026; reemplaza al anterior, mockup-web.webp, que mostraba solo la notebook)
im = Image.open(os.path.join(IMG, 'originales', 'mockup-web-2.webp')).convert('RGB')
mask = Image.new('L', [s * 4 for s in im.size], 0); d = ImageDraw.Draw(mask)
d.rounded_rectangle([122 * 4, 147 * 4, 1108 * 4 + 3, 790 * 4], radius=22 * 4, fill=255)    # pantalla
d.rounded_rectangle([31 * 4, 780 * 4, 1199 * 4 + 3, 806 * 4], radius=6 * 4, fill=255)      # base
d.rounded_rectangle([1162 * 4, 194 * 4, 1414 * 4 + 3, 708 * 4 + 3], radius=46 * 4, fill=255)  # teléfono
guardar(im, mask.resize(im.size, Image.LANCZOS), '005-mockup-web.png')

# Libro: el fondo y la sombra son grises neutros; papel y tapa tienen color → máscara por saturación,
# extendida hacia abajo para incluir el canto de las hojas (gris, igual que la sombra)
im = Image.open(os.path.join(IMG, 'originales', 'mockup-libro-2026.webp')).convert('RGB')
a = np.asarray(im.filter(ImageFilter.GaussianBlur(1.2))).astype(int)
# mockup 2026: papel y canto cálidos (R > B), tapa azul (B > R); fondo y sombra grises exactos
rb = a[..., 0] - a[..., 2]
obj = (rb >= 4) | (rb <= -8)
obj = nd.binary_fill_holes(nd.binary_closing(nd.binary_opening(obj, iterations=2), iterations=4))
lab, n = nd.label(obj)
obj = lab == (np.argmax(nd.sum(obj, lab, range(1, n + 1))) + 1)
# borde superior: por columna, del color (alisado con mediana); laterales y canto inferior, medidos a mano
# sobre el original (el canto y la sombra son grises parecidos y la máscara de color no los separa)
xs = np.arange(160, 2002)
top = np.array([obj[:, x].argmax() for x in xs]).astype(float)
top = nd.uniform_filter1d(nd.median_filter(top, 61, mode='nearest'), 9, mode='nearest')
abajo = [(2084, 1062), (2077, 1080), (1850, 1082), (1600, 1078), (1400, 1071), (1240, 1062), (1150, 1045),
         (1090, 1022), (1070, 1012), (1048, 1014), (1000, 1027), (850, 1063), (600, 1076), (320, 1082), (100, 1082), (83, 1064)]
K = 4
mask = Image.new('L', (im.width * K, im.height * K), 0)
pts = [(158, 370)] + list(zip(xs, top)) + [(2003, 352)] + abajo
ImageDraw.Draw(mask).polygon([(x * K, y * K) for x, y in pts], fill=255)
obj = np.asarray(mask.resize(im.size, Image.LANCZOS)) / 255
guardar(im, Image.fromarray((obj * 255).astype('uint8')), '005-mockup-libro.png')

# Fichas: son tres rectángulos en perspectiva. De cada una se toma la envolvente convexa de sus píxeles con color
# (papel cálido, R > B; tinta y reverso azules, B > R; el fondo y las sombras son grises neutros), dentro de una
# zona aproximada marcada a mano. Así los bordes salen rectos y sin halo de sombra.
from shapely.geometry import Polygon, MultiPoint
from shapely.ops import unary_union
im = Image.open(os.path.join(IMG, 'originales', '005-mockup-fichas-2026.webp')).convert('RGB')
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
guardar(im, mask.resize(im.size, Image.LANCZOS), '005-mockup-fichas.png')
