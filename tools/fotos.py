# Prepara las ilustraciones generadas (assets/images/originales/, en orden de descarga)
# para sus cajas: recorte a la proporción de la caja, paso a las dos tintas del sistema.
# Uso: py tools/fotos.py        (escribe assets/images/NNN-nombre.jpg)
import glob, os
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets', 'images', 'originales')
OUT = os.path.join(ROOT, 'assets', 'images')
INK, PAPER = '#1A3A5C', '#EFEEE6'

# Página de 210 × 160 mm (15 oct. 2026: antes 148 mm; las cajas a sangre arriba o abajo crecieron 6 mm).
# id, nombre, ancho y alto de la caja en mm, modo (c = recorte que llena la caja, l = lámina entera sobre papel),
# foco horizontal y vertical del recorte (0–1), tenue (0–1: mezcla con el papel)
FOTOS = [
    ('012', 'senda-bosque', 104, 160, 'c', .5, .5, 0),
    ('013', 'bosque-torrente', 72, 160, 'c', .55, .5, 0),
    ('014a', 'fagus-betuloides', 60, 112, 'l', .5, .5, 0),
    ('014b', 'drymis-winteri', 28, 54, 'l', .5, .5, 0),
    ('018', 'el-carmen', 210, 83.5, 'c', .5, .36, 0),
    ('022', 'salina', 210, 49.5, 'c', .5, .47, 0),
    ('024', 'jinetes-llanura', 70, 160, 'c', .47, .5, 0),
    ('025', 'suelo-espinoso', 124.3, 94.5, 'c', .5, .5, 0),
    ('026', 'walleechu', 102, 160, 'c', .5, .5, 0),
    ('027', 'hoguera', 188, 36, 'c', .5, .56, 0),
    ('028', 'aguti', 60, 54, 'l', .5, .5, 0),
    ('029', 'yeguada', 92.3, 56.65, 'c', .5, .5, 0),
    ('032', 'posta', 92.3, 92.65, 'c', .5, .45, 0),
    ('034', 'punta-alta', 210, 43, 'c', .5, .50, 0),
    ('036', 'megaterios', 92.3, 94.5, 'l', .5, .5, 0),
    ('038', 'cantil-huesos', 92.3, 72, 'c', .58, .5, 0),
    ('040', 'scelidotherium', 92.3, 58.5, 'l', .5, .5, 0),
    ('042', 'megatherium', 92.3, 67.5, 'l', .5, .5, 0),
    ('043', 'llanos', 92.3, 49.5, 'c', .5, .5, .35),
    ('046', 'vivac', 210, 70, 'c', .5, .56, 0),
    ('049', 'horizonte-sierra', 92.3, 72, 'c', .4, .45, 0),
    ('050', 'llanura-rebano', 92.3, 45, 'c', .5, .50, 0),
    ('051', 'fogon', 210, 65.5, 'c', .5, .50, 0),
    ('053', 'hogueras', 210, 54, 'c', .5, .52, 0),
    ('061', 'plaza-buenos-aires', 92.3, 40.5, 'c', .5, .40, 0),
    ('063', 'cardal', 102, 160, 'c', .5, .5, 0),
    ('064', 'vizcacha', 92.3, 40.5, 'l', .5, .5, 0),
    ('066', 'parana-rosario', 210, 65.5, 'c', .5, .45, 0),
    ('068', 'barranca-parana', 102, 160, 'c', .5, .5, 0),
    ('072', 'riscos-bajada', 102, 160, 'c', .5, .5, 0),
    ('074', 'diente-caballo', 92.3, 72, 'l', .5, .5, 0),
    ('076', 'gran-seco', 210, 65.5, 'c', .5, .56, 0),
    ('079', 'picotijera', 92.3, 36, 'l', .5, .5, 0),
    ('082', 'puerto-deseado', 210, 61, 'c', .5, .45, 0),
    ('084', 'guanaco', 92.3, 31.5, 'c', .5, .36, 0),
    ('086', 'san-julian', 102, 160, 'c', .5, .5, 0),
    ('090', 'macrauchenia', 92.3, 45, 'l', .5, .5, 0),
    ('094', 'sirga', 92.3, 40.5, 'c', .5, .52, 0),
    ('103', 'santa-cruz', 60, 54, 'c', .5, .45, 0),
]

files = sorted(glob.glob(os.path.join(SRC, 'Imagen*.png')), key=os.path.getmtime)
assert len(files) == len(FOTOS), f'{len(files)} originales para {len(FOTOS)} cajas'

# Originales regenerados después (no entran en el orden de descarga)
REEMPLAZOS = {'042': 'tapa-megatherium.webp',  # Megatherium con el árbol completo
              '090': '090-macrauchenia-suelo.webp'}  # 20 oct. 2026: medio esqueleto en el suelo, sin cráneo (sin la trompa de hueso)
APARTE = {'012', '013'}  # una sola imagen para la doble: la prepara tools/laminas.py

SOLO = set(__import__('sys').argv[1:])  # py tools/fotos.py 018 022 … rehace solo esas
for (pid, name, bw, bh, mode, fx, fy, faint), f in zip(FOTOS, files):
    if pid in APARTE or (SOLO and pid not in SOLO): continue
    f = os.path.join(SRC, REEMPLAZOS.get(pid, f))
    im = Image.open(f).convert('L')
    w, h = im.size
    ar = bw / bh
    if mode == 'c':
        cw, ch = (w, round(w / ar)) if w / h < ar else (round(h * ar), h)
        x0 = min(max(round(fx * w - cw / 2), 0), w - cw)
        y0 = min(max(round(fy * h - ch / 2), 0), h - ch)
        im = ImageOps.autocontrast(im.crop((x0, y0, x0 + cw, y0 + ch)), cutoff=0.5)
    else:
        # Lámina: el fondo de papel de la imagen pasa a blanco para fundirse con la página
        bg = sorted(im.resize((64, 64)).getdata())[int(64 * 64 * .6)]
        lut = [min(255, round(255 * (v - 40) / (bg - 12 - 40))) if v > 40 else 0 for v in range(256)]
        im = im.point(lut)
        cw, ch = (round(h * ar), h) if w / h < ar else (w, round(w / ar))
        canvas = Image.new('L', (cw, ch), 255)
        canvas.paste(im, ((cw - w) // 2, (ch - h) // 2))
        im = canvas
    im = ImageOps.colorize(im, black=INK, white=PAPER)
    if faint:
        im = Image.blend(im, Image.new('RGB', im.size, PAPER), faint)
    out = os.path.join(OUT, f'{pid}-{name}.jpg')
    im.save(out, quality=92)
    print(pid, os.path.basename(f)[-12:], '->', os.path.basename(out), im.size, f'{round(im.size[0] / bw * 25.4)} ppp')
