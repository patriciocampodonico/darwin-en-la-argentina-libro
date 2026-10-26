# PDF de revisión para compartir: tapa desplegada (contratapa + lomo + tapa) y después
# todo el interior en dobles páginas enfrentadas, como se vería el libro abierto.
# Uso: py tools/revision.py     → ../Darwin_en_la_Argentina_revision.pdf (carpeta LIBRO)
import io, os, pathlib, subprocess
import pymupdf
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = next(p for p in ['C:/Program Files/Google/Chrome/Application/chrome.exe',
                          'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'] if os.path.exists(p))
OUT = ROOT.parent / 'Darwin_en_la_Argentina_revision.pdf'
TAPA = 'a'  # variante de tapa elegida

DOBLES = '''<style>
@page { size: 420mm 160mm; margin: 0; }
@media print {
  .spread { display: flex !important; width: 420mm; height: 160mm; break-after: page; break-inside: avoid; }
  .spread:has(.page--cover) { display: none !important; }
  /* Carilla de cortesía (001) y guarda final (106): se muestran en blanco, frente al retiro de tapa */
  .spread:has(.page--guard) .slot--empty { display: block !important; width: 210mm; height: 160mm; flex: none; background: var(--paper); font-size: 0; }
  .page { break-after: auto !important; }
}
</style>
</head>'''

def pdf(url, dest):
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--virtual-time-budget=8000',
                    f'--print-to-pdf={dest}', '--no-pdf-header-footer', url], stderr=subprocess.DEVNULL, check=True)

subprocess.run(['node', 'build.mjs'], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
html = io.open(ROOT / 'index.html', encoding='utf-8').read().replace('</head>', DOBLES, 1)
io.open(ROOT / '_revision.html', 'w', encoding='utf-8').write(html)

tmp_tapa, tmp_dobles = ROOT / 'salida' / '_tapa.pdf', ROOT / 'salida' / '_dobles.pdf'
pdf((ROOT / 'tapa' / 'tapa.html').as_uri() + f'?v={TAPA}', tmp_tapa)
pdf((ROOT / '_revision.html').as_uri(), tmp_dobles)

# Unión y versión liviana para reenviar (la calidad de imprenta está en salida/libro.pdf).
# Cada imagen se achica en su mismo lugar (rewrite_images de PyMuPDF rompía los fondos que Chrome dibuja como patrón);
# las máscaras de transparencia (mapa tenue de 003) se achican sin pérdida.
doc = pymupdf.open(tmp_tapa)
with pymupdf.open(tmp_dobles) as dobles:
    doc.insert_pdf(dobles)
LADO, CALIDAD = 1600, 75
mascaras = {int(doc.xref_get_key(x, 'SMask')[1].split()[0]) for x in range(1, doc.xref_length())
            if doc.xref_is_stream(x) and doc.xref_get_key(x, 'SMask')[0] == 'xref'}
for x in range(1, doc.xref_length()):
    if not doc.xref_is_stream(x) or doc.xref_get_key(x, 'Subtype')[1] != '/Image' or doc.xref_get_key(x, 'ImageMask')[1] == 'true':
        continue
    pix = pymupdf.Pixmap(doc, x)
    if max(pix.width, pix.height) <= LADO and x in mascaras:
        continue
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
doc.set_metadata({'title': 'Darwin en la Argentina — revisión'})
paginas = len(doc)
doc.save(OUT, garbage=4, deflate=True)
doc.close()
for f in (tmp_tapa, tmp_dobles, ROOT / '_revision.html'):
    os.remove(f)
print(OUT.name, paginas, 'hojas', round(OUT.stat().st_size / 1e6, 1), 'MB')
