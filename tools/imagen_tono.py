# Pasa una imagen a las dos tintas del sistema (azul profundo sobre papel) y la recorta.
# Uso: py tools/imagen_tono.py <origen> <salida.jpg> <x0> <y0> <x1> <y1>
import sys
from PIL import Image, ImageOps

src, out = sys.argv[1], sys.argv[2]
box = tuple(int(v) for v in sys.argv[3:7])
im = Image.open(src).convert('L').crop(box)
im = ImageOps.autocontrast(im, cutoff=1)
im = ImageOps.colorize(im, black='#1A3A5C', white='#EFEEE6')
im.save(out, quality=92)
print(out, im.size)
