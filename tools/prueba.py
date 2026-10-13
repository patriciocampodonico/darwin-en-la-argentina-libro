# Prueba de impresión en cuadernillo cosido a caballete (acaballado), montada en pliegos SRA3 (450 × 320 mm).
# Cada pliego lleva dos tiras de 420 × 148 mm (dos páginas enfrentadas), con 3 mm de demasía y marcas de corte y de plegado.
# Un A3 justo (420 × 297 mm) no alcanza: dos tiras con demasía miden 426 × 308 mm.
# La demasía se arma espejando 3 mm del borde de cada página (las imágenes a sangre continúan; el papel sigue siendo papel).
# Uso: py tools/prueba.py 1 16   (primera y última página del cuadernillo; la cantidad tiene que ser múltiplo de 4)
#      antes: node build.mjs pdf   → sale ../Darwin_prueba_NNN-NNN_SRA3.pdf (carpeta LIBRO)
import io, pathlib, sys
import numpy as np
import pymupdf
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
MM = 72 / 25.4
PW, PH, B = 210, 148, 3            # página y demasía, en mm
SW, SH = 450, 320                  # pliego SRA3 apaisado
X0, Y0 = (SW - 2 * PW) / 2, (SH - 2 * (PH + 2 * B)) / 2 + B   # esquina de corte de la tira de arriba
DPI = 300
AZUL = (0x1A / 255, 0x3A / 255, 0x5C / 255)

a, z = int(sys.argv[1]), int(sys.argv[2])
N = z - a + 1
assert N % 4 == 0, 'la cantidad de páginas tiene que ser múltiplo de 4'
libro = pymupdf.open(ROOT / 'salida' / 'libro.pdf')   # la hoja n del PDF es la página n (0 = tapa, 1 = carilla de cortesía)
R = lambda x0, y0, x1, y1: pymupdf.Rect(x0 * MM, y0 * MM, x1 * MM, y1 * MM)

def demasia(n, lado):
    """La página, como imagen, con 3 mm espejados arriba, abajo y del lado de afuera (no en el pliegue)."""
    pix = libro[n].get_pixmap(dpi=DPI, alpha=False)
    im = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3)
    b = round(B / 25.4 * DPI)
    lados = (b, 0) if lado == 'i' else (0, b)
    buf = io.BytesIO(); Image.fromarray(np.pad(im, ((b, b), lados, (0, 0)), mode='symmetric')).save(buf, 'JPEG', quality=90)
    return buf.getvalue()

def tira(hoja, y, izq, der):
    """Dos páginas enfrentadas con su demasía (no hay demasía en el pliegue) y sus marcas."""
    for n, x, lado in ((izq, X0, 'i'), (der, X0 + PW, 'd')):
        caja = R(x - B if lado == 'i' else x, y - B, x + PW if lado == 'i' else x + PW + B, y + PH + B)
        hoja.insert_image(caja, stream=demasia(n, lado), keep_proportion=False)
        hoja.show_pdf_page(R(x, y, x + PW, y + PH), libro, n)       # la página, en vectores, encima
    m = dict(color=(0, 0, 0), width=0.25)
    for yy in (y, y + PH):                                           # marcas de corte horizontales, a los costados
        hoja.draw_line((( X0 - B - 8) * MM, yy * MM), ((X0 - B - 1.5) * MM, yy * MM), **m)
        hoja.draw_line(((X0 + 2 * PW + B + 1.5) * MM, yy * MM), ((X0 + 2 * PW + B + 8) * MM, yy * MM), **m)

def pliego(doc, arriba, abajo, rotulo):
    hoja = doc.new_page(width=SW * MM, height=SH * MM)
    for y, par in ((Y0, arriba), (Y0 + PH + 2 * B, abajo)):
        if par: tira(hoja, y, *par)
    m = dict(color=(0, 0, 0), width=0.25)
    for x in (X0, X0 + 2 * PW):                                      # marcas de corte verticales, arriba y abajo
        hoja.draw_line((x * MM, 0.8 * MM), (x * MM, (Y0 - B - 1) * MM), **m)
        hoja.draw_line((x * MM, (SH - Y0 + B + 1) * MM), (x * MM, (SH - 0.8) * MM), **m)
    for y0, y1 in ((0.8, Y0 - B - 1), (SH - Y0 + B + 1, SH - 0.8)):  # marca de plegado, punteada
        hoja.draw_line(((X0 + PW) * MM, y0 * MM), ((X0 + PW) * MM, y1 * MM), dashes='[2 2] 0', **m)
    hoja.insert_text((3 * MM, (SH - 1.2) * MM), rotulo, fontsize=5.5, color=AZUL)

# Imposición a caballete: la tira k lleva, de frente, [N−2k | 1+2k] y, de dorso, [2+2k | N−1−2k]
pag = lambda i: a + i - 1
frente = [(pag(N - 2 * k), pag(1 + 2 * k)) for k in range(N // 4)]
dorso = [(pag(2 + 2 * k), pag(N - 1 - 2 * k)) for k in range(N // 4)]
doc = pymupdf.open()
for s in range(0, N // 4, 2):
    for cara, lista in (('frente', frente), ('dorso', dorso)):
        arr, aba = lista[s], lista[s + 1] if s + 1 < len(lista) else None
        txt = ' · '.join(f'{p[0]:03d}|{p[1]:03d}' for p in (arr, aba) if p)
        pliego(doc, arr, aba, f'Darwin en la Argentina · prueba {a:03d}–{z:03d} · pliego {s // 2 + 1} {cara} · {txt} · doble faz, voltear por el borde corto')
        print(f'pliego {s // 2 + 1} {cara}: {txt}')
out = ROOT.parent / f'Darwin_prueba_{a:03d}-{z:03d}_SRA3.pdf'
doc.save(out, deflate=True, garbage=3)
print(out.name, len(doc), 'caras', round(out.stat().st_size / 1e6, 1), 'MB')
