# Láminas de los registros 022 (cristales), 023 (vida en la salmuera) y 069 (el Paraná), a partir de
# assets/images/originales/022*.webp, 023*.webp y 069*.webp. Uso: py tools/laminas.py
import os
import numpy as np
from PIL import Image, ImageOps

IMG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'images')
INK, PAPER = '#1A3A5C', '#EFEEE6'

def lamina(name):
    """Gris con el papel de la imagen llevado a blanco, para fundirse con la página."""
    im = Image.open(os.path.join(IMG, 'originales', name + '.webp')).convert('L')
    bg = int(np.median(np.asarray(im)))
    return im.point([min(255, round(255 * (v - 40) / (bg - 12 - 40))) if v > 40 else 0 for v in range(256)])

def guardar(im, name, ancho_mm):
    ImageOps.colorize(im, black=INK, white=PAPER).save(os.path.join(IMG, name + '.jpg'), quality=92)
    print(name, im.size, round(im.width / ancho_mm * 25.4), 'ppp')

# 022a · cristal de yeso a TAMAÑO REAL: de punta a punta (x 55–1484 del original) = 70 mm.
# Caja 92,34 × 31,5 mm; el cristal empieza a 11,17 mm del borde izquierdo (bajo la regla de 7 cm) y a 1,5 mm del superior.
im = lamina('022a-padre')
px = (1484 - 55) / 70
canvas = Image.new('L', (round(92.34 * px), round(31.5 * px)), 255)
canvas.paste(im, (round(11.17 * px) - 55, round(1.5 * px) - 318))
guardar(canvas, '022a-padre', 92.34)

# 022b · sulfato de sodio: franja horizontal a la proporción de la caja
im = lamina('022b-madre')
h = round(im.width * 31.5 / 92.34)
guardar(im.crop((0, 512 - h // 2, im.width, 512 - h // 2 + h)), '022b-madre', 92.34)

# 023 · cuatro viñetas, caja 28,42 × 27 mm
for name in ('023a-confervas', '023b-infusorios', '023c-gusanos', '023d-flamenco'):
    im = lamina(name)
    h = round(im.width * 27 / 28.42)
    guardar(im.crop((0, (im.height - h) // 2, im.width, (im.height - h) // 2 + h)), name, 28.42)

# 069 · tres vistas del río, caja 60,34 × 45 mm. Mismo criterio para las tres: el dibujo llena la caja,
# con 30 px de papel sobre y bajo el dibujo; el ancho sale de la proporción. (y0, y1 del recorte, centro x)
for name, y0, y1, cx in (('069a-conecta', 167, 933, 843), ('069b-abarca', 160, 938, 766), ('069c-drena', 57, 973, 768)):
    im = lamina(name)
    w = round((y1 - y0) * 60.34 / 45)
    guardar(im.crop((cx - w // 2, y0, cx - w // 2 + w, y1)), name, 60.34)

# 058 y 067 · textura de agua de los ríos (franjas a sangre). Tono oscuro: el negro de la imagen pasa a la tinta.
def agua(name, caja, x0, y0):
    im = Image.open(os.path.join(IMG, 'originales', name + '.webp')).convert('L')
    w, h = (im.width - x0, round((im.width - x0) * caja[1] / caja[0])) if caja[0] > caja[1] else (round((im.height - y0) * caja[0] / caja[1]), im.height - y0)
    im = ImageOps.autocontrast(im.crop((x0, y0, x0 + w, y0 + h)), cutoff=(1, 0))
    guardar(im.point([round(255 * (v / 255) ** 1.9) for v in range(256)]), name, caja[0])  # más denso: el nombre va encima
agua('058-agua-salado', (40.42, 148), 20, 0)    # franja vertical junto al lomo
agua('067-agua-parana', (210, 36), 0, 330)      # franja horizontal de lado a lado
