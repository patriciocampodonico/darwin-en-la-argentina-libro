# Tapa desplegada para imprenta: solapa de atrás + contratapa + lomo + tapa + solapa de adelante.
# Desde el 20 oct. 2026 va a sangre (simple faz, pedido de Patricio): la hoja mide la tapa al corte, 590 × 160 mm
# (solapas de 80 mm, lomo de 10 mm), sin demasía ni marcas de corte; solo las marcas de plegado punteadas,
# 5 mm arriba y abajo en cada pliegue. Entra en A2.
# Uso: py tools/tapa_imprenta.py   → ../Darwin_tapa_solapas_imprenta.pdf (carpeta LIBRO)
import os, pathlib, re, subprocess
import pymupdf

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = next(p for p in ['C:/Program Files/Google/Chrome/Application/chrome.exe',
                          'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'] if os.path.exists(p))
MM = 72 / 25.4
TAPA = 'a'
css = (ROOT / 'tapa' / 'tapa.css').read_text(encoding='utf-8')
FLAP = float(re.search(r'--flap:\s*([\d.]+)mm', css).group(1))
SPINE = float(re.search(r'--spine:\s*([\d.]+)mm', css).group(1))
PW, PH = 210, 160
W = 2 * FLAP + 2 * PW + SPINE
PLIEGUES = [FLAP, FLAP + PW, FLAP + PW + SPINE, FLAP + 2 * PW + SPINE]

tmp = ROOT / 'salida' / '_tapa.pdf'
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--virtual-time-budget=8000', f'--print-to-pdf={tmp}',
                '--no-pdf-header-footer', (ROOT / 'tapa' / 'tapa.html').as_uri() + f'?v={TAPA}'], stderr=subprocess.DEVNULL, check=True)
src = pymupdf.open(tmp)
R = lambda x0, y0, x1, y1: pymupdf.Rect(x0 * MM, y0 * MM, x1 * MM, y1 * MM)
corte = R(0, 0, W, PH)                    # el PDF de Chrome puede medir unas décimas de más: se toma la caja exacta

doc = pymupdf.open()
hoja = doc.new_page(width=W * MM, height=PH * MM)                 # a sangre: la hoja es la tapa al corte, sin demasía ni marcas de corte
hoja.show_pdf_page(R(0, 0, W, PH), src, 0, clip=corte)
fondo = src[0].get_pixmap(dpi=50, alpha=False, clip=corte)
for x in PLIEGUES:                                                # plegado, punteado, arriba y abajo (5 mm)
    for y0, y1 in ((0, 5), (PH - 5, PH)):
        px = fondo.pixel(min(round((x + 3) / 25.4 * 50), fondo.width - 1), round((y0 + 2.5) / 25.4 * 50))
        tinta = (1, 1, 1) if sum(px) < 380 else (0, 0, 0)         # blanco sobre el azul (lomo), negro sobre papel; se mira 3 mm a la derecha del pliegue
        hoja.draw_line((x * MM, y0 * MM), (x * MM, y1 * MM), color=tinta, width=0.25, dashes='[2 2] 0')
out = ROOT.parent / 'Darwin_tapa_solapas_imprenta.pdf'
doc.set_metadata({'title': 'Darwin en la Argentina — tapa para imprenta'})
doc.save(out, deflate=True, garbage=3)
doc.close(); src.close(); os.remove(tmp)
print(out.name, f'{W:g} × {PH} mm', round(out.stat().st_size / 1e6, 1), 'MB')
