# PDF de revisión para compartir: tapa desplegada (contratapa + lomo + tapa) y después
# todo el interior en dobles páginas enfrentadas, como se vería el libro abierto.
# Uso: py tools/revision.py     → ../Darwin_en_la_Argentina_revision.pdf (carpeta LIBRO)
import io, os, pathlib, subprocess
import pymupdf

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
# rewrite_images conserva las transparencias (mapa tenue de 003).
doc = pymupdf.open(tmp_tapa)
with pymupdf.open(tmp_dobles) as dobles:
    doc.insert_pdf(dobles)
doc.rewrite_images(dpi_threshold=160, dpi_target=150, quality=75)
doc.set_metadata({'title': 'Darwin en la Argentina — revisión'})
paginas = len(doc)
doc.save(OUT, garbage=4, deflate=True)
doc.close()
for f in (tmp_tapa, tmp_dobles, ROOT / '_revision.html'):
    os.remove(f)
print(OUT.name, paginas, 'hojas', round(OUT.stat().st_size / 1e6, 1), 'MB')
