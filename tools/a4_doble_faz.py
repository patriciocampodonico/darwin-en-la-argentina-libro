# Libro para imprimir en A4 doble faz, una hoja del libro por A4, para encuadernar pegado (lomo / cola).
# 20 oct. 2026, pedido de Patricio: hoja k del PDF impar = frente (página impar, recto), par = dorso (página par, verso).
# Frente: la página al corte exacto, con un rectángulo negro de 0,3 mm por fuera del borde de corte (guía para cortar).
# Dorso: la página con 3 mm de demasía (espejando el borde, como tools/prueba.py), sin rectángulo:
# si el corte se corre un poco, del otro lado sigue habiendo imagen.
# Página centrada en el A4 apaisado → frente y dorso coinciden al imprimir a doble faz volteando por el borde corto.
# Uso: node build.mjs pdf   y después   py tools/a4_doble_faz.py   → ../Darwin_libro_A4_doble_faz.pdf (carpeta LIBRO)
#      py tools/a4_doble_faz.py liviano   → ../Darwin_libro_A4_doble_faz_liviano.pdf: el mismo, con las imágenes
#      recomprimidas (texto y trazos siguen en vectores) para que pese menos de 10 MB.
import io, pathlib, sys
import numpy as np
import pymupdf
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
MM = 72 / 25.4
LIVIANO = 'liviano' in sys.argv[1:]
PW, PH, B = 210, 160, 3
DPI, CALIDAD = (130, 50) if LIVIANO else (300, 90)
SW, SH = 297, 210                          # A4 apaisado
X, Y = (SW - PW) / 2, (SH - PH) / 2        # esquina de corte de la página
LINEA = 0.3
R = lambda x0, y0, x1, y1: pymupdf.Rect(x0 * MM, y0 * MM, x1 * MM, y1 * MM)

libro = pymupdf.open(ROOT / 'salida' / 'libro.pdf')   # la hoja n del PDF es la página n (0 = tapa, 1 = carilla de cortesía, 104 = guarda)
corte = R(0, 0, PW, PH)                                # Chrome deja unas décimas de más: se toma la caja exacta
doc = pymupdf.open()
for n in range(1, 105):
    hoja = doc.new_page(width=SW * MM, height=SH * MM)
    frente = n % 2 == 1
    if not frente:                                     # demasía: la página como imagen, con 3 mm espejados alrededor
        pix = libro[n].get_pixmap(dpi=DPI, alpha=False, clip=corte)
        im = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3)
        b = round(B / 25.4 * DPI)
        im = np.pad(im, ((b, b), (b, b), (0, 0)), mode='symmetric')
        if LIVIANO:                                    # solo se ve el anillo de 3 mm: el centro (tapado por la página) va liso y casi no pesa
            im = im.copy(); im[2 * b:-2 * b, 2 * b:-2 * b] = im[b:-b, b:-b].reshape(-1, 3).mean(0)
        buf = io.BytesIO(); Image.fromarray(im).save(buf, 'JPEG', quality=CALIDAD)
        hoja.insert_image(R(X - B, Y - B, X + PW + B, Y + PH + B), stream=buf.getvalue(), keep_proportion=False)
    hoja.show_pdf_page(R(X, Y, X + PW, Y + PH), libro, n, clip=corte)   # en vectores, encima
    if frente:                                         # el borde de adentro de la línea cae justo en el corte
        hoja.draw_rect(R(X - LINEA / 2, Y - LINEA / 2, X + PW + LINEA / 2, Y + PH + LINEA / 2), color=(0, 0, 0), width=LINEA * MM)
    hoja.insert_text(((X) * MM, (SH - 8) * MM), f'Darwin en la Argentina · hoja {(n + 1) // 2} de 52 · página {n:03d} · '
                     f'{"frente: cortar por el borde de adentro de la línea negra" if frente else "dorso: 3 mm de demasía"} · '
                     'A4 al 100 %, doble faz, voltear por el borde corto', fontsize=6, color=(0.45, 0.45, 0.45))
if LIVIANO:                                            # todas las imágenes (también las de los fondos que Chrome dibuja como patrón):
    # achicadas a 760 px de lado mayor (~90 dpi a página entera) y en JPEG; las máscaras de transparencia, achicadas y sin pérdida.
    # (rewrite_images de PyMuPDF rompía esos patrones; acá cada imagen se reemplaza en su mismo lugar)
    LADO = 760
    mascaras = {int(doc.xref_get_key(x, 'SMask')[1].split()[0]) for x in range(1, doc.xref_length())
                if doc.xref_is_stream(x) and doc.xref_get_key(x, 'SMask')[0] == 'xref'}
    for x in range(1, doc.xref_length()):
        if not doc.xref_is_stream(x) or doc.xref_get_key(x, 'Subtype')[1] != '/Image' or doc.xref_get_key(x, 'ImageMask')[1] == 'true':
            continue
        pix = pymupdf.Pixmap(doc, x)
        if pix.alpha: pix = pymupdf.Pixmap(pix, 0)
        if pix.colorspace and pix.colorspace.n not in (1, 3): pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        im = Image.frombytes('L' if pix.n == 1 else 'RGB', (pix.width, pix.height), pix.samples)
        im.thumbnail((LADO, LADO), Image.LANCZOS)
        if x in mascaras:
            doc.update_stream(x, im.tobytes(), compress=True); filtro = '/FlateDecode'
        else:
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=CALIDAD)
            if buf.tell() >= len(doc.xref_stream_raw(x)):   # ya estaba más liviana: se deja como está
                continue
            doc.update_stream(x, buf.getvalue(), compress=False); filtro = '/DCTDecode'
        for k, v in (('Filter', filtro), ('DecodeParms', 'null'), ('Width', str(im.width)), ('Height', str(im.height)),
                     ('BitsPerComponent', '8'), ('ColorSpace', '/DeviceGray' if im.mode == 'L' else '/DeviceRGB')):
            doc.xref_set_key(x, k, v)
out = ROOT.parent / ('Darwin_libro_A4_doble_faz_liviano.pdf' if LIVIANO else 'Darwin_libro_A4_doble_faz.pdf')
doc.set_metadata({'title': 'Darwin en la Argentina — libro en A4 doble faz'})
doc.save(out, deflate=True, garbage=3)
print(out.name, len(doc), 'páginas,', round(out.stat().st_size / 1e6, 1), 'MB')
