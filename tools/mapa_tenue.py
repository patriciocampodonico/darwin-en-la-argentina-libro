# Genera assets/maps/argentina-tenue.png a partir del mapa ilustrado de la web
# (fuentes/05_Web_Actual/Proyecto_Web/assets/imgFondooooooo.png).
# Recorta el mapa, lo pasa a una sola tinta (azul del sistema) con transparencia,
# quita la escala gráfica de la interfaz y funde los bordes del recorte.
from PIL import Image, ImageFilter
import numpy as np

SRC = '../fuentes/05_Web_Actual/Proyecto_Web/assets/imgFondooooooo.png'
OUT = 'assets/maps/argentina-tenue.png'
BOX = (1215, 235, 2335, 2168)          # recorte en px del original
BLUE = (0x1A, 0x3A, 0x5C)

im = Image.open(SRC).convert('RGB').crop(BOX)
lum = np.asarray(im.convert('L'), dtype=np.float32) / 255
paper = np.percentile(lum, 90)          # tono del papel de fondo
alpha = np.clip((paper - lum) / (paper - lum.min()), 0, 1)
alpha[alpha < 0.04] = 0

h, w = alpha.shape
mask = np.ones((h, w), dtype=np.float32)
mask[int(h * 0.90):, :int(w * 0.24)] = 0      # escala gráfica de la web
edge = 90                                      # fundido de bordes laterales, en px
ramp = np.clip(np.minimum(np.arange(w), w - 1 - np.arange(w)) / edge, 0, 1)
mask *= ramp[None, :]
mask = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(40)), dtype=np.float32) / 255

rgba = np.zeros((h, w, 4), dtype=np.uint8)
rgba[..., :3] = BLUE
rgba[..., 3] = (alpha * mask * 255).astype(np.uint8)
Image.fromarray(rgba).save(OUT, optimize=True)
print(OUT, (w, h))
