# Mapa y flor de la página 004, tomados de la imagen de fondo de la web (WEB/Darwin-Explorar/assets/mapa-argentina.png,
# copiada en assets/images/originales/004-mapa-web.png). Salen en una sola tinta (el azul del libro) con transparencia:
# lo oscuro del original pasa a tinta y el papel a transparente. La página los muestra muy tenues (opacidad --tenue).
# Uso: py tools/mapa004.py
import os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INK = (0x1A, 0x3A, 0x5C)
src = Image.open(os.path.join(ROOT, 'assets', 'images', 'originales', '004-mapa-web.png')).convert('L')

def tinta(caja, salida, borrar=(), borde=0, mar=None):
    g = np.asarray(src.crop(caja).filter(ImageFilter.GaussianBlur(0.6))).astype(float)
    papel = np.percentile(g, 90)                      # nivel del papel en ese recorte
    alfa = np.clip((papel - 10 - g) / (papel - 10 - 45), 0, 1) ** 0.85
    for x0, y0, x1, y1 in borrar:                     # borrado con borde difuminado (30 px), para no cortar el halo en seco
        yy, xx = np.mgrid[0:alfa.shape[0], 0:alfa.shape[1]]
        fuera = np.maximum.reduce([x0 - xx, xx - x1, y0 - yy, yy - y1])
        alfa *= np.clip(fuera / 30, 0, 1)
    if borde:                                         # se funde hacia los bordes libres (arriba y derecha)
        h, w = alfa.shape
        alfa *= np.clip(np.arange(h)[:, None] / borde, 0, 1) * np.clip((w - 1 - np.arange(w))[None, :] / borde, 0, 1)
    if mar:                                           # mar alrededor del territorio: gris claro que se difumina hacia afuera
        px, py, radio, nivel = mar
        alfa = np.pad(alfa, ((py, py), (px, px)))
        tierra = ndimage.binary_fill_holes(ndimage.binary_closing(alfa > 0.3, iterations=4))
        d = ndimage.distance_transform_edt(~tierra)   # distancia a la costa, en px
        t = np.clip(1 - d / radio, 0, 1)
        rng = np.random.default_rng(4)                # borde irregular, como una mancha de tinta
        grano = ndimage.gaussian_filter(rng.random(alfa.shape), 26); grano = (grano - grano.min()) / np.ptp(grano)
        halo = nivel * np.clip(t * 1.9 - 0.75 * grano, 0, 1) ** 0.8
        h, w = alfa.shape; m = 70                     # nunca llega al borde del recorte
        halo *= np.clip(np.minimum.reduce([np.arange(h)[:, None] + 0 * np.arange(w), (h - 1 - np.arange(h))[:, None] + 0 * np.arange(w),
                                           np.arange(w)[None, :] + 0 * np.arange(h)[:, None], (w - 1 - np.arange(w))[None, :] + 0 * np.arange(h)[:, None]]) / m, 0, 1)
        alfa = np.where(tierra, alfa, np.maximum(alfa, ndimage.gaussian_filter(halo, 5)))
    out = np.zeros(alfa.shape + (4,), np.uint8); out[..., :3] = INK; out[..., 3] = (alfa * 255).round()
    Image.fromarray(out).save(os.path.join(ROOT, 'assets', salida)); print(salida, out.shape[1], 'x', out.shape[0])

# mapa: se borra la esquina donde asoma la escala gráfica
tinta((1330, 230, 2330, 2110), os.path.join('maps', 'argentina-tenue.png'), borrar=[(-40, 1790, 160, 1920)],
      mar=(300, 160, 250, 0.3))  # lienzo ampliado 300 px a los lados y 160 arriba y abajo; el mar llega a 250 px de la costa
# flor: esquina inferior izquierda del original (sale a sangre por la izquierda y por abajo)
tinta((0, 1210, 960, 2168), os.path.join('images', '004-flor.png'), borde=40)

# 005 · flor de ceibo (ilustración aparte, fondo blanco): mismo paso a una tinta con transparencia.
# La rama entra por el borde derecho, así que en la página va a sangre por la derecha.
im = Image.open(os.path.join(ROOT, 'assets', 'images', 'originales', '005-flor.webp')).convert('RGBA')
blanco = Image.new('RGBA', im.size, (255, 255, 255, 255)); blanco.alpha_composite(im)
g = np.asarray(blanco.convert('L')).astype(float)
alfa = np.clip((245 - g) / (245 - 60), 0, 1) ** 0.85
out = np.zeros(alfa.shape + (4,), np.uint8); out[..., :3] = INK; out[..., 3] = (alfa * 255).round()
Image.fromarray(out).save(os.path.join(ROOT, 'assets', 'images', '005-flor.png')); print('005-flor.png', im.size)
