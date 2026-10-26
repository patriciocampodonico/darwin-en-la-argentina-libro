# Código de barras EAN-13 del ISBN para la contratapa (26 oct. 2026).
# Uso: py tools/codigo_barras.py [ISBN de 12 o 13 cifras]  → reemplaza el <svg class="back__isbn"> de tapa/tapa.html
# (va en línea, no como imagen, para que las cifras usen la Inter del libro).
# El número por defecto es DE MUESTRA (prefijo argentino 978-987, editorial 00): reemplazar por el ISBN real cuando lo haya.
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
L = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
G = ['0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111']
R = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']
PARIDAD = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']

def control(d12):
    s = sum(int(c) * (3 if i % 2 else 1) for i, c in enumerate(d12))
    return str((10 - s % 10) % 10)

num = ''.join(c for c in (sys.argv[1] if len(sys.argv) > 1 else '978987000000') if c.isdigit())[:12]
num += control(num)
bits = '101' + ''.join((L if p == 'L' else G)[int(c)] for p, c in zip(PARIDAD[int(num[0])], num[1:7])) + '01010' \
     + ''.join(R[int(c)] for c in num[7:]) + '101'
guardas = {*range(3), *range(45, 50), *range(92, 95)}

# Módulo de 0,33 mm (EAN al 100 %): 95 módulos + 11 de zona libre a la izquierda y 7 a la derecha. Unidades del SVG = módulos.
ANCHO, ALTO, BARRA, CIFRA = 113, 80, 66, 9
x0 = 11
rects = []
i = 0
while i < 95:
    if bits[i] == '1':
        j = i
        while j < 95 and bits[j] == '1': j += 1
        h = BARRA + (5 if i in guardas else 0)
        rects.append(f'<rect x="{x0 + i}" y="0" width="{j - i}" height="{h}"/>')
        i = j
    else:
        i += 1
txt = lambda x, s, a='middle': f'<text x="{x}" y="{BARRA + 4 + CIFRA}" text-anchor="{a}">{s}</text>'
textos = [txt(x0 - 2, num[0], 'end'), txt(x0 + 3 + 21, num[1:7]), txt(x0 + 50 + 21, num[7:])]
isbn = f'ISBN {num[:3]}-{num[3:6]}-{num[6:8]}-{num[8:12]}-{num[12]}'
svg = (f'<svg class="back__isbn" viewBox="0 -14 {ANCHO} {ALTO + 14}" role="img" aria-label="{isbn}">'
       f'<g font-size="{CIFRA}">'
       f'<text x="{x0 + 47.5}" y="-5" text-anchor="middle" font-size="8">{isbn}</text>'
       + ''.join(rects) + ''.join(textos) + '</g></svg>')
tapa = ROOT / 'tapa' / 'tapa.html'
src = tapa.read_text(encoding='utf-8')
tapa.write_text(re.sub(r'<svg class="back__isbn".*?</svg>', lambda m: svg, src, flags=re.S), encoding='utf-8', newline='')
print(isbn)
