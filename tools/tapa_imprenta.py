# Tapa desplegada para imprenta: solapa de atrás + contratapa + lomo + tapa + solapa de adelante,
# con 3 mm de demasía (espejando el borde, como tools/prueba.py), marcas de corte y marcas de plegado punteadas.
# Desde el 20 oct. 2026: solapas de 80 mm y lomo de 10 mm → 590 × 160 mm al corte; la hoja mide 610 × 180 mm
# (no entra en A2 con marcas: va en plotter o en A1).
# Uso: py tools/tapa_imprenta.py   → ../Darwin_tapa_solapas_imprenta.pdf (carpeta LIBRO)
import io, os, pathlib, re, subprocess
import numpy as np
import pymupdf
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = next(p for p in ['C:/Program Files/Google/Chrome/Application/chrome.exe',
                          'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'] if os.path.exists(p))
MM = 72 / 25.4
B, M, DPI = 3, 10, 300                     # demasía, margen para las marcas, resolución de la demasía
TAPA = 'a'
css = (ROOT / 'tapa' / 'tapa.css').read_text(encoding='utf-8')
FLAP = float(re.search(r'--flap:\s*([\d.]+)mm', css).group(1))
SPINE = float(re.search(r'--spine:\s*([\d.]+)mm', css).group(1))
PW, PH = 210, 160
W = 2 * FLAP + 2 * PW + SPINE
PLIEGUES = [FLAP, FLAP + PW, FLAP + PW + SPINE, FLAP + 2 * PW + SPINE]
AZUL = (0x1A / 255, 0x3A / 255, 0x5C / 255)

tmp = ROOT / 'salida' / '_tapa.pdf'
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--virtual-time-budget=8000', f'--print-to-pdf={tmp}',
                '--no-pdf-header-footer', (ROOT / 'tapa' / 'tapa.html').as_uri() + f'?v={TAPA}'], stderr=subprocess.DEVNULL, check=True)
src = pymupdf.open(tmp)
R = lambda x0, y0, x1, y1: pymupdf.Rect(x0 * MM, y0 * MM, x1 * MM, y1 * MM)
corte = R(0, 0, W, PH)                    # el PDF de Chrome puede medir unas décimas de más: se toma la caja exacta

pix = src[0].get_pixmap(dpi=DPI, alpha=False, clip=corte)
im = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3)
b = round(B / 25.4 * DPI)
buf = io.BytesIO(); Image.fromarray(np.pad(im, ((b, b), (b, b), (0, 0)), mode='symmetric')).save(buf, 'JPEG', quality=92)

doc = pymupdf.open()
hoja = doc.new_page(width=(W + 2 * M) * MM, height=(PH + 2 * M) * MM)
hoja.insert_image(R(M - B, M - B, M + W + B, M + PH + B), stream=buf.getvalue(), keep_proportion=False)
hoja.show_pdf_page(R(M, M, M + W, M + PH), src, 0, clip=corte)   # en vectores, encima
m = dict(color=(0, 0, 0), width=0.25)
for x in (M, M + W):                                              # corte, en las cuatro esquinas
    hoja.draw_line((x * MM, 1 * MM), (x * MM, (M - B - 1) * MM), **m)
    hoja.draw_line((x * MM, (M + PH + B + 1) * MM), (x * MM, (PH + 2 * M - 1) * MM), **m)
for y in (M, M + PH):
    hoja.draw_line((1 * MM, y * MM), ((M - B - 1) * MM, y * MM), **m)
    hoja.draw_line(((M + W + B + 1) * MM, y * MM), ((W + 2 * M - 1) * MM, y * MM), **m)
for x in PLIEGUES:                                                # plegado, punteado
    for y0, y1 in ((1, M - B - 1), (M + PH + B + 1, PH + 2 * M - 1)):
        hoja.draw_line(((M + x) * MM, y0 * MM), ((M + x) * MM, y1 * MM), dashes='[2 2] 0', **m)
hoja.insert_text(((M + 2) * MM, (PH + 2 * M - 2.5) * MM),
                 f'Darwin en la Argentina · tapa desplegada {W:g} × {PH} mm al corte · solapas {FLAP:g} mm · lomo {SPINE:g} mm · '
                 f'demasía {B} mm · punteado = plegado', fontsize=5.5, color=AZUL)
out = ROOT.parent / 'Darwin_tapa_solapas_imprenta.pdf'
doc.set_metadata({'title': 'Darwin en la Argentina — tapa para imprenta'})
doc.save(out, deflate=True, garbage=3)
doc.close(); src.close(); os.remove(tmp)
print(out.name, f'{W + 2 * M:g} × {PH + 2 * M} mm', round(out.stat().st_size / 1e6, 1), 'MB')
