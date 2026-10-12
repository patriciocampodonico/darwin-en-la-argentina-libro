# BOOK_PROGRESS — control de páginas

**2026-10-06 — cambio global autorizado:** cuerpo de texto justificado con última línea a la izquierda en todas las páginas con texto de lectura (003, 004, 011–030), incluidas las aprobadas. Ver BOOK_SPEC.
**2026-10-06 — segundo cambio global autorizado:** medida única de 3 columnas para el cuerpo; recompuestas 012, 014, 016, 019, 022 (aprobadas) y 028, 029 (en revisión). 012: título en columnas 1–3 y texto en 4–6 desde la línea 19. 014: la imagen pasa a media página y el texto a columnas 4–6. 016: dos columnas anchas. 019: título 1–3, texto 4–6. 022 y 028: texto en columnas 1–3. 029: texto en 1–3, pie del esquema junto a la figura.

Estados: pendiente / trabajando / revisión / APROBADA. Una página APROBADA queda bloqueada
(`approved.lock`) y no se modifica sin autorización explícita.

Resumen: 71 aprobadas · 33 en revisión · 0 pendientes (de 104).

## 001 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · portadilla (página izquierda)
- Contenido: «Darwin en la Argentina» (v2, entrada 001). El v2 lo trae en mayúsculas; se compone en altas y bajas.
- Assets: ninguno raster. Línea de recorrido en SVG dentro de la página.
- Decisiones especiales: Playfair Display 36 pt / 3 líneas de base, columnas 1–5, líneas 8–13. Línea de recorrido esquemática con 15 marcas (15 paradas), líneas 21–22, rotulada 01 y 15 en Inter 6,5 pt. Fondo hueso. Sin folio.
- Última modificación: 2026-10-06

## 002 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · título y datos de la edición (página derecha, enfrentada a 001)
- Contenido: título, subtítulo, autor, dato de la selección y dato del proyecto (v2, entrada 002), sin cambios de redacción. El guion «-» del v2 antes de FAPyD se compone como raya corta «–»; el título de la obra fuente va en cursiva.
- Assets: ninguno raster. Marca del sistema en SVG dentro de la página.
- Decisiones especiales: bloque en columnas 3–6. Autor en Inter 9 pt (línea 6). Título Playfair 26 pt y subtítulo Playfair cursiva 14 pt, sobre las mismas líneas de base que las dos líneas del título de 001. Datos en Inter 7,5 pt / 3 mm en dos bloques (col. 3–4 y 5–6) bajo filete fino, a la altura de la línea de recorrido de 001. Marca del sistema (punto de parada en anillo de registro, 9 mm) en el ángulo superior exterior. Sin folio.
- Última modificación: 2026-10-06

## 003 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · introducción (página izquierda; se enfrenta a 004)
- Contenido: párrafo de la entrada 003 del v2, sin cambios. Título «El recorte argentino» y antetítulo «Introducción» salen del rótulo «Introduccion - El recorte argentino» (tildes restituidas).
- Assets: `assets/maps/argentina-tenue.png` — PROVISORIO (mapa ilustrado de la web, no es cartografía a escala).
- Decisiones especiales: texto en columnas 1–3, Inter 9,5 pt / 4,5 mm (voz editorial; Lora queda para Darwin). Antetítulo en línea 6 y título Playfair 26 pt en líneas 8–10, las mismas alturas que 001–002. Mapa a toda la altura de la página sobre columnas 4–6, en azul del sistema al 30 %. Primer folio del libro: «003 Apertura», margen inferior exterior.
- Última modificación: 2026-10-06

## 004 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · introducción (página derecha, enfrentada a 003)
- Contenido: párrafo de la entrada 004 del v2, sin cambios. Antetítulo «Introducción» y título «Qué va a encontrar el lector» (tilde restituida). Rótulos del mosaico tomados de la lista de recursos del v2: Fósil, Ave, Planta, Río, Montaña, Mapa.
- Assets: seis pictogramas en SVG dentro de la página — PROVISORIOS (ver ASSET_MANIFEST).
- Decisiones especiales: misma estructura que 003 (antetítulo línea 6, título líneas 8–10, texto en columnas 1–3 desde la línea 12). El título corre en una sola línea sobre las seis columnas. Mosaico 3 × 2 en columnas 4–6: baldosas azules de 1 columna × 6 líneas con silueta en color papel (negativo tipo cianotipo) y rótulo Inter 7 pt debajo. Folio «004 Apertura».
- Última modificación: 2026-10-06

## 005 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · clave de lectura (página izquierda, doble con 006)
- Contenido: título y seis definiciones de la entrada 005 del v2. Cada «rótulo: definición» se separa en rótulo + frase (inicial en mayúscula); la redacción no cambia. Título en altas y bajas.
- Ejemplos (todos reales, del v2): frase de Darwin de la entrada 011; «01 Bahía del Buen Suceso · 17–20 dic. 1832» (metadata de 011); «Registro de flora / Fagus betuloides» (015); nombres del código de notas D, E y ED (103).
- Assets: ninguno raster. Reutiliza la hoja del mosaico de 004 (provisoria).
- Decisiones especiales: página densa, título en líneas 2–4. Seis tarjetas de 2 columnas × 9 líneas (muestra, rótulo, definición) bajo filete fino. **Fija el código visual del libro**: Darwin en Lora; fecha y lugar como número de parada en negrita + lugar / fecha; registro con baldosa azul; mapa de tramo con línea, puntos y flecha; notas D y E en etiqueta de contorno, ED en etiqueta llena.
- Última modificación: 2026-10-06

## 006 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · sistema de tres piezas (página derecha, doble con 005)
- Contenido: título, tres piezas y párrafo final de la entrada 006 del v2. «LIBRO - lectura…» se compone como rótulo «Libro» + frase; sin cambios de redacción.
- Assets: QR del mapa digital — PENDIENTE (placeholder rotulado, columna 6, 28,4 × 27 mm).
- Decisiones especiales: misma estructura de tres pares de columnas que 005. Dibujos esquemáticos en línea: doble página apaisada, pantalla del mapa con recorrido, dos fichas en tres franjas (como define el TP4). Párrafo final en columnas 1–3 bajo filete.
- Última modificación: 2026-10-06

## 007 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · cartografía (página izquierda, doble con 008)
- Contenido: título y lista de paradas 01–08 de la entrada 007 del v2. Fechas sintéticas tomadas de la cronología (009–010) y de la metadata de cada parada.
- Assets: `assets/maps/general.svg` — PROVISORIO (mapa esquemático generado por `tools/mapas.mjs`).
- Decisiones especiales: título en líneas 2–4; lista en columnas 1–3 (número, nombre, fecha; 2 líneas por parada); mapa de todo el recorrido en columnas 5–6 a toda la caja (1° de latitud ≈ 5 mm), con recuadro que remite al detalle de 008. En este mapa solo se numeran 01, 13, 14 y 15; el resto se numera en el detalle.
- Última modificación: 2026-10-06

## 008 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · cartografía (página derecha, doble con 007)
- Contenido: «Continuación» (paradas 09–15 y regreso por el Paraná) y leyenda de la entrada 008 del v2. El título «Mapa general del recorrido» no se repite: lo lleva 007 para toda la doble.
- Assets: `assets/maps/detalle.svg` — PROVISORIO (ídem).
- Decisiones especiales: mapa de detalle (paradas 02–12, 1° de latitud ≈ 12 mm) en columnas 1–3; lista en columnas 4–5; leyenda en columna 6. Recorrido terrestre en línea llena, fluvial / marítimo en línea de trazos, registro científico con rombo. Fechas de 10 (1–5 oct.) y 11 (5–12 oct.) deducidas de la metadata de 069–072 y de la cronología. Nota ED: «Mapas esquemáticos: las ubicaciones son orientativas.»
- Rombos de registro: paradas 01, 05, 09, 13 y 14 (las que tienen en el v2 una página titulada como registro, inventario o especie). Criterio a confirmar.
- Última modificación: 2026-10-06

## 009 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · cronología (página izquierda, doble con 010)
- Contenido: nueve entradas de la entrada 009 del v2. Inicial en mayúscula y sin punto final; guiones de rango como raya corta. Se agrega el número de parada delante de cada fecha.
- Assets: ninguno.
- Decisiones especiales: línea de tiempo horizontal al centro de la caja, entradas alternadas arriba y abajo cada media columna. Tramo punteado entre 1832 y 1833 (salto de ocho meses). La línea sigue hasta el lomo y continúa en 010. No es proporcional al tiempo.
- Última modificación: 2026-10-06

## 010 — APROBADA (2026-10-06) 🔒
- Tipo: Apertura · cronología e índice (página derecha, doble con 009)
- Contenido: seis entradas e índice de paradas de la entrada 010 del v2. «Beagle» en cursiva. El índice suma el número de la primera página de cada parada según el plan v2.
- Assets: ninguno.
- Decisiones especiales: la línea entra desde el lomo y termina en la última entrada (8 de mayo de 1834). Índice en columnas 5–6, una parada por línea de base.
- Última modificación: 2026-10-06

## 011 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 01 · apertura de parada (página izquierda, doble con 012)
- Contenido: fragmento de Darwin de la entrada 011 del v2. Título «Bahía del Buen Suceso»; metadata «01 · 17–20 dic. 1832».
- Cotejo: coincide con la capa de texto del escaneo (pág. 291 del libro). Se conserva «Patagonía» como figura en la fuente. «1832.—Tras» se compone con la raya pegada, como en la edición. **Falta cotejo visual del escaneo** (no hay herramienta para ver las páginas escaneadas).
- Assets: `assets/images/011-buen-suceso.jpg` — PROVISORIO.
- Decisiones especiales: franja superior con imagen a sangre hasta la línea 17; franja inferior con número y fecha (línea 19), título en Playfair 36 pt en dos líneas (columnas 1–3) y texto de Darwin en Lora 9,25 pt (columnas 4–6). El folio pasa a decir «01 Bahía del Buen Suceso».
- Última modificación: 2026-10-06

## 012 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 01 · narrativa + mapa de tramo (página derecha, doble con 011)
- Contenido: fragmento de la entrada 012 del v2, sin cambios. Coincide con la capa de texto del escaneo (págs. 291–292).
- Assets: `assets/maps/tramo-01.svg` — PROVISORIO (esquemático).
- Decisiones especiales: misma estructura de franjas que 011. Arriba, mapa de tramo de 6 columnas × 17 líneas con los lugares que Darwin nombra en 011 (cabo San Diego, estrecho de Le Maire, isla de los Estados, bahía) y la llegada del Beagle en trazos. Abajo, título de página en Playfair 20 pt (columnas 1–2) y texto en dos columnas (3–4 y 5–6).
- Última modificación: 2026-10-06

## 013 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 01 · narrativa con notas (página izquierda, doble con 014)
- Contenido: fragmento de la entrada 013 del v2 con su corte […] visible. Coincide con la capa de texto del escaneo (págs. 292 y 298).
- Nota E (1): nota de la edición española sobre los fiords, tomada de la capa de texto del escaneo (págs. 298–299). Se omite la referencia bibliográfica final, marcada con […]. Falta cotejo visual.
- Nota ED: frase del proyecto tomada de la web (tarjeta de Tierra del Fuego), con «Darwin» como sujeto.
- Assets: imagen PENDIENTE (placeholder rotulado, columnas 4–6 a sangre, 104 × 148 mm).
- Decisiones especiales: título en líneas 2–5, texto desde la línea 7 en columnas 1–3, notas debajo en Inter 7,5 pt con sus etiquetas. La imagen cruza el lomo y sigue en 014.
- Última modificación: 2026-10-06

## 014 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 01 · narrativa (página derecha, doble con 013)
- Contenido: fragmento de la entrada 014 del v2. El v2 parte el párrafo en «En ambos lados / yacían» por un salto de página; en la fuente es continuo (págs. 299–300) y así se compone. Se conserva «medula» sin tilde, como en la fuente.
- Assets: imagen PENDIENTE (placeholder rotulado, columnas 1–2 a sangre, 72 × 148 mm).
- Decisiones especiales: título en líneas 2–3, texto en dos columnas (3–4 y 5–6) desde la línea 7.
- Última modificación: 2026-10-06

## 015 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 01 · registro científico (izquierda, doble con 016)
- Contenido: fragmento de la entrada 015 del v2. Nota E (1) sobre Drymis, de la pág. 300 del libro. Ficha (lugar, fecha, nombres) y nota ED sobre los nombres científicos, a partir de la «información adicional» del v2.
- Cambios respecto del v2: «Fagas» → «Fagus» (error de reconocimiento; el v2 ya pide «Fagus»); corte marcado con […] después de «sombrío» (el v2 corta a mitad de frase sin marcarlo); nombres científicos en cursiva.
- Assets: dos ilustraciones botánicas PENDIENTES.
- Decisiones especiales: antetítulo «Registro de campo» con baldosa chica. El tamaño de cada espécimen sigue al texto: Fagus grande (columnas 4–5), Drymis chico (columna 6).
- Última modificación: 2026-10-06

## 016 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 01 · narrativa + esquema (derecha, doble con 015)
- Contenido: fragmento de la entrada 016 del v2, en tres columnas.
- Cambios respecto del v2: se restituye «Solander.» de la fuente (el v2 corta en «el Dr. […]»); «magnifícencia» → «magnificencia» (error de reconocimiento, falta cotejo visual); punto y aparte en «Una loma», como en la fuente.
- Assets: perfil esquemático en SVG dentro de la página (definitivo si se aprueba).
- Decisiones especiales: perfil sin escala con los datos del fragmento (bosque, zona de turba, roca pizarrosa, 450 metros, loma con sendero de guanacos, cumbre más alta con nieve a trechos), rotulado como esquema ED.
- Última modificación: 2026-10-06

## 017 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · apertura (izquierda, doble con 018)
- Contenido: fragmento de la entrada 017 del v2. Título «Carmen de Patagones / Río Negro» en dos líneas; metadata «02 · 3–10 ago. 1833».
- Cambios respecto del v2: el v2 arranca en «3 de agosto llegó», sin sujeto; se compone «El Beagle […] el 3 de agosto llegó», con palabras de la fuente y el corte marcado (se omite la salida de Maldonado, Uruguay).
- Assets: `assets/maps/tramo-02.svg` — PROVISORIO (esquemático).
- Decisiones especiales: apertura distinta de 011: título arriba a todo el ancho, texto en columnas 1–3 y mapa de tramo en columnas 4–6, con el paralelo 41° S que nombra Darwin.
- Última modificación: 2026-10-06

## 018 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · narrativa + sección geológica (derecha, doble con 017)
- Contenido: fragmento de la entrada 018 del v2. Corte marcado con […] después de «raquítica y pobre» (el v2 corta a mitad de frase).
- Assets: sección esquemática en SVG dentro de la página (definitiva si se aprueba).
- Decisiones especiales: sección del cantil sin escala (grava, arenisca, conglomerado de piedra pómez, arenisca, mar), rotulada como esquema ED, junto al lomo; texto en columnas 4–6.
- Última modificación: 2026-10-06

## 019 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · pausa con imagen (izquierda, doble con 020)
- Contenido: fragmento de la entrada 019 del v2, sin cambios.
- Assets: imagen PENDIENTE (franja superior a sangre, 210 × 77,5 mm).
- Última modificación: 2026-10-06

## 020 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · narrativa + datos (derecha, doble con 019)
- Contenido: fragmento de la entrada 020 del v2, sin cambios. Tres medidas destacadas, textuales del fragmento, rotuladas ED.
- Assets: `assets/images/020-salina-flamenco.jpg` — PROVISORIO.
- Decisiones especiales: imagen vertical en columnas 4–6 hasta el borde exterior; termina en el pie de la caja para dejar libre el folio.
- Última modificación: 2026-10-06

## 021 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · registro científico (izquierda, doble con 022)
- Contenido: fragmento de la entrada 021 del v2 hasta «empieza a evaporarse».
- Cambios respecto del v2: el v2 repite al final de 021 el tramo «El cieno es negruzco… infusorios», que también abre 022; se deja solo en 022. «superñcie» → «superficie» (error de reconocimiento).
- Assets: dos baldosas en SVG dentro de la página (definitivas si se aprueba).
- Decisiones especiales: cristal de yeso dibujado a tamaño real (7 cm, la medida que da Darwin) con su cota; «la madre» como cristales chicos esparcidos. Nota ED: son nombres de los gauchos, no nomenclatura actual.
- Última modificación: 2026-10-06

## 022 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · narrativa + registro (derecha, doble con 021)
- Contenido: fragmento de la entrada 022 del v2, en dos columnas.
- Cambios respecto del v2: «jCuán» → «¡Cuán»; rayas del inciso final como en la fuente; corte marcado con […] (el v2 termina en «cieno» y omite el final de la frase).
- Assets: cuatro pictogramas PROVISORIOS (confervas, infusorios, gusanos anélidos, flamencos).
- Última modificación: 2026-10-06

## 023 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · pausa / cita (izquierda, doble con 024)
- Contenido: fragmento de la entrada 023 del v2. La última frase («¡Bien podemos afirmar…!») se compone en Playfair 20 pt en su lugar, sin repetirse.
- Cambios respecto del v2: «jBien» → «¡Bien». «Cáncer salinas» se conserva.
- Nota D (1): solo la referencia, «Linnean Trans., vol. XI, pág. 205. […]». El reconocimiento lee «Linnosan»: PENDIENTE de cotejo visual.
- Assets: imagen PENDIENTE (paisaje de salina, 188 × 31,5 mm).
- Última modificación: 2026-10-06

## 024 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 02 · transición (derecha, doble con 023)
- Contenido: fragmento de la entrada 024 del v2, sin cambios.
- Assets: esquema del camino por tierra (paradas 02–08, nombres del índice de 010), SVG en la página, sin escala, etiqueta ED. Reemplaza al «mapa de transición» del v2.
- Última modificación: 2026-10-06

## 025 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 03 · apertura (izquierda, doble con 026)
- Contenido: fragmento de la entrada 025 del v2. Título «Camino al Río Colorado»; metadata «03 · 11 ago. 1833».
- Cambios respecto del v2: se quita la última frase («El país, en todo el trayecto…»), que el v2 repite al comienzo de 026.
- Assets: imagen PENDIENTE (franja vertical a sangre, 70 × 148 mm). Esquema lineal del tramo con los hitos de 025–030, sin escala, etiqueta ED.
- Última modificación: 2026-10-06

## 026 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 03 · narrativa (derecha, doble con 025)
- Contenido: fragmento de la entrada 026 del v2, sin cambios.
- Assets: imagen PENDIENTE (textura de suelo y arbustos, 92 × 94,5 mm).
- Última modificación: 2026-10-06

## 027 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 03 · narrativa con imagen (izquierda, doble con 028)
- Contenido: fragmento de la entrada 027 del v2, sin cambios. Nota ED redactada por el proyecto (grafía «Walleechu» y contexto de la palabra «salvajes»).
- Assets: imagen PENDIENTE (árbol con ofrendas, mitad izquierda a sangre, 102 × 148 mm).
- Última modificación: 2026-10-06

## 028 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 03 · pausa inmersiva (derecha, doble con 027)
- Contenido: fragmento de la entrada 028 del v2, como párrafo continuo (el v2 lo parte por un salto de página). Nota E (1): «En español en el original.» Lista ED de las cuatro cosas, con palabras del fragmento.
- Pendiente de cotejo visual: «chairca» (¿«charca»?), así en el v2 y en el reconocimiento.
- Assets: imagen PENDIENTE (hoguera de noche, 188 × 36 mm).
- Decisiones especiales: **primera página oscura del libro** (fondo azul pleno, texto en color papel), porque es la noche. Se activa con `data-tone="dark"`.
- Última modificación: 2026-10-06

## 029 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 03 · narrativa + registro (izquierda, doble con 030)
- Contenido: fragmento de la entrada 029 del v2 con su corte […]. «buhos» y «Cavia Patagónica» como en la edición.
- Assets: imagen PENDIENTE del agutí (60 × 54 mm). Franja de terrenos (cascajo, césped, salitral, río), SVG en la página, sin escala, etiqueta ED.
- Última modificación: 2026-10-06

## 030 — APROBADA (2026-10-06) 🔒
- Tipo: Parada 03 · narrativa + esquema (derecha, doble con 029)
- Contenido: fragmento de la entrada 030 del v2, sin cambios.
- Assets: imagen PENDIENTE (yeguada cruzando el río, 92 × 63 mm). Esquema del curso tortuoso con las tres medidas del fragmento, sin escala, etiqueta ED.
- Última modificación: 2026-10-06

## 031 — APROBADA (2026-10-06)
- Tipo: Parada 04 · apertura (izquierda, doble con 032). Título «Camino a Bahía Blanca»; antetítulo «Cambio de territorio»; metadata «04 · ago. 1833».
- Contenido: fragmento de la entrada 031 del v2 en dos columnas anchas. Cambio: «se'dividían» → «se dividían».
- Assets: franja de tres terrenos (SVG en la página, sin escala, ED).

## 032 — APROBADA (2026-10-06)
- Tipo: Parada 04 · narrativa + esquema (derecha). Fragmento de la entrada 032 sin cambios.
- Assets: perfil de dunas sobre arcilla con charcos (SVG, sin escala, ED).

## 033 — APROBADA (2026-10-06)
- Tipo: Parada 04 · narrativa (izquierda, doble con 034). Fragmento de la entrada 033 con su corte […]; «Africa» sin tilde como en la fuente.
- Assets: imagen PENDIENTE (posta al pie del cerro, 92 × 85,5 mm).

## 034 — APROBADA (2026-10-06)
- Tipo: Parada 04 · narrativa con notas + esquema (derecha). Fragmento de la entrada 034; punto y aparte en «Bahía Blanca apenas», como en la fuente.
- Nota E (1): nota del traductor («Hoy es una ciudad de 40.000 habitantes…»). Nota ED: «Ese "hoy" es el de la traducción: 1921.»
- Assets: planta esquemática del fuerte (SVG, sin escala, forma supuesta, ED).

## 035 — APROBADA (2026-10-06)
- Tipo: Parada 05 · apertura (izquierda, doble con 036). Título «Bahía Blanca / Punta Alta»; metadata «05 · 1832–1833».
- Contenido: fragmento de la entrada 035; la primera frase («…una perfecta catacumba de monstruos de razas extintas.») va en Playfair 20 pt, en su lugar.
- Assets: imagen PENDIENTE (costa de Punta Alta, franja superior a sangre, 210 × 37 mm).

## 036 — APROBADA (2026-10-06)
- Tipo: Parada 05 · narrativa + esquemas (derecha). Fragmento de la entrada 036. Cambios: «ag-osto» → «agosto», «hallañ» → «hallan».
- Assets: línea de las dos visitas y corte del terreno (SVG, sin escala, ED). La visita anterior no lleva fecha porque el fragmento no la da.

## 037 — APROBADA (2026-10-06)
- Tipo: Parada 05 · fósil / hallazgo (izquierda, doble con 038). Inventario 1.º a 4.º.
- Cambios respecto del v2: ordinales dañados recompuestos como 1.º–4.º; se completa «El Mylodon Darwinii» con el final de la frase en la fuente.
- Nota ED: «El inventario sigue en la página siguiente: son nueve grandes cuadrúpedos.»
- Assets: imagen PENDIENTE (cuatro esqueletos o siluetas a tamaños comparados, 92 × 94,5 mm).

## 038 — APROBADA (2026-10-06)
- Tipo: Parada 05 · fósil / hallazgo (derecha). Inventario 5.º a 8.º, Toxodon y cierre.
- Cambios respecto del v2: ordinales recompuestos; coma después de «el Toxodon» (el reconocimiento lee «Toxodorij tal»). Falta cotejo visual.
- Assets: plano de «unos 200 metros cuadrados» con nueve puntos (SVG, sin escala, ED).

## 039 — APROBADA (2026-10-06)
- Tipo: Parada 05 · narrativa + esquema (izquierda, doble con 040). Fragmento de la entrada 039.
- Cambios respecto del v2: «CtenomySy especie» → «Ctenomys, especie»; «tucutuco^ pero» → «tucutuco, pero». Falta cotejo visual.
- Assets: esquema de distancia entre los dos sitios, sin dirección (el fragmento no la da). Imagen PENDIENTE (cantil de tierra roja, 92 × 67,5 mm).

## 040 — APROBADA (2026-10-06)
- Tipo: Parada 05 · registro geológico (derecha). Fragmento de la entrada 040 sin cambios.
- Assets: sección de capas y 23 puntos por las 23 especies de conchas (13 + 4 + 6; las 6 salen por resta). SVG, sin escala, ED.

## 041 — APROBADA (2026-10-06)
- Tipo: Parada 05 · fósil / hallazgo (izquierda, doble con 042). Fragmento de la entrada 041.
- Cambios respecto del v2: coma después de «Scelidotherium» (el reconocimiento lee «Scelidoiheñumj incluso»). Falta cotejo visual.
- Assets: esquema de la capa con huesos, rótula y caparazón (SVG, formas convencionales, ED). Imagen PENDIENTE (esqueleto parcial de Scelidotherium, 92 × 58,5 mm).

## 042 — APROBADA (2026-10-06)
- Tipo: Parada 05 · registro geológico (derecha). Fragmento de la entrada 042.
- Cambios respecto del v2: «antigüe" dad» → «antigüedad»; «Mr, Lyell» → «Mr. Lyell»; se reponen la llamada (1) y el punto final. Nota D (1) tomada de la fuente («Principies of Ceology» → «Principles of Geology»).
- Assets: esquema de la ley de Lyell (SVG, ED; rotulado como interpretación histórica, no datación).

## 043 — APROBADA (2026-10-06)
- Tipo: Parada 05 · fósil / hallazgo (izquierda, doble con 044). Texto en las columnas 4–6, de la fila 2 a la 28.
- Cambios respecto del v2: «megateroideoSf» → «megateroideos,»; «Scelidoiherium» → «Scelidotherium»; coma después de «Mylodon»; «las raíl) Principies of Ceology, vol. IV, págf. 40. mas» → «las ramas» (la nota al pie estaba metida en el texto). Nota D (2) tomada de la fuente; «Mylodon robustas» → «robustus» (DUDA, falta cotejo visual).
- Nota ED: «La explicación es del profesor Owen, tal como la resume Darwin.»
- Assets: imagen PENDIENTE (Megatherium erguido, con llamadas funcionales, 92 × 67,5 mm).

## 044 — APROBADA (2026-10-06)
- Tipo: Parada 05 · narrativa (derecha). La primera pregunta va en Playfair 20 pt, en su lugar.
- Cambios respecto del v2: «íos» → «los»; […] al final (el v2 corta a mitad de frase).
- Nota ED: «Darwin deja la pregunta abierta: las conchas del mar no alcanzan para saber cómo era la tierra.»
- Assets: imagen PENDIENTE (llanos con vegetación rala, sugerida, 92 × 54 mm).

## 045 — APROBADA (2026-10-06)
- Tipo: Apertura de parada 06 · Sierra de la Ventana (izquierda, doble con 046). Texto en dos columnas anchas. Sin cambios respecto del v2.
- Assets: franja del primer día (SVG, sin escala, ED).

## 046 — APROBADA (2026-10-06)
- Tipo: Parada 06 · narrativa (derecha). Texto en dos columnas anchas.
- Cambios respecto del v2: «Bahía Blanca,y» → «Bahía Blanca, y». Notas tomadas de la fuente: E (1), D (2) y E (*); «Eryngmm» → «Eryngium».
- Assets: tres medidas (1.000 m, 1.060 m, 6 leguas).

## 047 — APROBADA (2026-10-06)
- Tipo: Parada 06 · imagen + esquema (izquierda, doble con 048). «ai venir» → «al venir».
- Assets: perfil de la subida a 250–300 m (SVG, pendiente exagerada, ED). Imagen PENDIENTE (vivac al amanecer, franja a sangre 210 × 64 mm).

## 048 — APROBADA (2026-10-06)
- Tipo: Parada 06 · narrativa + corte (derecha). Antetítulo «9 de septiembre». Sin cambios respecto del v2.
- DUDA: «laderas espinadas» (¿«empinadas»?), igual en el v2 y en el reconocimiento; falta cotejo visual.
- Assets: corte esquemático macizo – valle – cuatro picos (SVG, ED; no es un perfil real).

## 049 — APROBADA (2026-10-06)
- Tipo: Parada 06 · narrativa + esquema (izquierda, doble con 050). Punto y aparte en «Ya he dicho», como en la fuente.
- Assets: esquema del punto alcanzado, por debajo de los dos picos más altos (orden de los picos supuesto); lista de tres rocas.

## 050 — APROBADA (2026-10-06)
- Tipo: Parada 06 · narrativa (derecha).
- Cambios respecto del v2: se quita el […] entre «más a gusto.» y «10 de septiembre» (en la fuente el texto es corrido); «En el camino.vi» → «En el camino vi». Nota E (1) tomada de la fuente.
- Assets: línea del regreso (SVG, ED). Imagen PENDIENTE (horizonte de la llanura desde la sierra, 92 × 54 mm).

## 051 — APROBADA (2026-10-06)
- Tipo: Apertura de parada 07 · Travesía de las Pampas (izquierda, doble con 052). Sin cambios respecto del v2.
- Assets: línea de postas y fechas, 10–19 sep., con datos de las entradas 050–058 (SVG, sin escala, ED). Imagen PENDIENTE (llanura con rebaño, 92 × 40,5 mm).
- OJO: si cambian los textos de 055–058, revisar esta línea.

## 052 — APROBADA (2026-10-06)
- Tipo: Parada 07 · escena de noche, PÁGINA OSCURA (derecha). Antetítulo «12–13 de septiembre».
- Cambios respecto del v2: el v2 trae el pasaje dos veces (la primera incompleta, separadas por […]); se compone una sola vez. No hay texto sobre las bolas en la entrada, así que no se muestran.
- Assets: línea de la escena, de la hoguera hacia afuera (SVG, ED). Imagen PENDIENTE (fogón visto desde la loma, franja a sangre 210 × 59,5 mm).

## 053 — APROBADA (2026-10-06)
- Tipo: Parada 07 · narrativa + esquema (izquierda, doble con 054). El texto arranca en la fila 6 (23 líneas).
- DUDA: «hacía el Norte» (con tilde), igual en el v2 y en el reconocimiento; se deja.
- Assets: esquema de la región pantanosa, 128 km hacia el Norte (SVG, ED).

## 054 — APROBADA (2026-10-06)
- Tipo: Parada 07 · narrativa + datos (derecha). Sin cambios respecto del v2. El título «Fuego y lago» es del v2; el fragmento no nombra un lago.
- Assets: tres números del fragmento. Imagen PENDIENTE (horizonte nocturno con hogueras, 188 × 36 mm).

## Tildes que se dejan como en la fuente (041–054)
«asi» (043), «mas que» (049), «para mi» (050), «hacía el Norte» (053), «útilísima» (045), «fértilísima» (044). Decide Patricio si se normalizan.

## 055 — APROBADA (2026-10-06)
- Parada 07 · narrativa (izquierda, doble con 056). Dos columnas anchas. «ios cuales» → «los cuales»; punto y aparte en «Se nos refirió».
- Assets: conteo de animales muertos por el pedrisco, un punto por animal (SVG, ED).

## 056 — APROBADA (2026-10-06)
- Parada 07 · narrativa + planta (derecha). Sin cambios respecto del v2.
- Assets: planta de El Corral y de la eminencia a una misma escala (forma circular supuesta; se toman 4 km).

## 057 — APROBADA (2026-10-06)
- Parada 07 · narrativa + datos (izquierda, doble con 058). Sin cambios respecto del v2. El texto arranca en la fila 6, a la par de 058.
- Assets: franja azul vertical del lado del lomo = río Salado (hito del recorrido, no frontera actual); dos medidas.

## 058 — APROBADA (2026-10-06)
- Parada 07 · narrativa (derecha). Dos columnas anchas desde la fila 6.
- OMISIÓN VISIBLE por Uruguay: se quita «, como en Banda Oriental, donde hay una gran diferencia entre el país que rodea a Montevideo y las sabanas muy poco pobladas de Colonia,» y se marca […].
- Notas D tomadas de la fuente: (1) Atwater («Atvater» en el reconocimiento, DUDA) y (1) Azara. Nota ED sobre la numeración repetida.
- Assets: lista «El razonamiento, paso a paso» (observa, supone, consulta, duda).

## 059 — APROBADA (2026-10-06)
- Apertura de parada 08 · Buenos Aires I (izquierda, doble con 060). Sin cambios respecto del v2.
- Assets: esquema de las afueras a la cuadrícula; sigue en 060 a través del lomo (SVG, ED; no es un plano).

## 060 — APROBADA (2026-10-06)
- Parada 08 · retícula protagonista (derecha). Sin cambios en el fragmento.
- Notas tomadas de la fuente: D (1) con […] por la oración sobre Montevideo; E (*) con las rayas recompuestas (DUDA).
- Assets: retícula de cuadras a sangre, con una cuadra destacada (SVG, ED).

## 061 — APROBADA (2026-10-06)
- Parada 08 · diagrama (izquierda, doble con 062). Sin cambios respecto del v2.
- Assets: secuencia ciudad → cuadra → casa → patio → azotea (SVG, ED; divisiones supuestas).

## 062 — APROBADA (2026-10-06)
- Parada 08 · narrativa (derecha). «sin embarg-o» → «sin embargo»; «edifícios» → «edificios»; punto y aparte en «El gran corral».
- Assets: esquema patio / plaza. Imagen PENDIENTE (plaza hacia 1830, 92 × 40,5 mm).

## 063 — APROBADA (2026-10-06)
- Apertura de parada 09 · Camino al Paraná / Rosario (izquierda, doble con 064). Dos columnas anchas.
- Cambios respecto del v2: «sí se marcha» → «si se marcha»; «hacía Mendoza» y «hacía la mitad» → «hacia» (tildes de más del reconocimiento).
- Assets: seis medidas del fragmento.

## 064 — APROBADA (2026-10-06)
- Parada 09 · narrativa + imagen (derecha). Sin cambios respecto del v2.
- Assets: imagen PENDIENTE (cardal como textura, media página a sangre, 102 × 148 mm).

## 065 — APROBADA (2026-10-06)
- Parada 09 · registro de campo (izquierda, doble con 066). […] al final (el v2 corta a mitad de frase). No se agrega explicación moderna.
- Assets: lista de lo que hay en el montón. Imagen PENDIENTE (vizcacha en la boca de la madriguera, 92 × 40,5 mm).

## 066 — APROBADA (2026-10-06)
- Parada 09 · página de aire (derecha). La última frase va en Playfair 20 pt, en su lugar. Sin cambios respecto del v2.
- Assets: franja azul a sangre al pie = río Paraná.

## 067 — APROBADA (2026-10-06)
- Parada 09 · imagen + corte (izquierda, doble con 068). Sin cambios respecto del v2.
- Assets: corte de la meseta, «unos 18 m» (SVG, ED). Imagen PENDIENTE (panorama del Paraná, franja a sangre 210 × 59,5 mm).

## 068 — APROBADA (2026-10-06)
- Parada 09 · tres conceptos (derecha). Ordinales dañados recompuestos como 1.º, 2.º, 3.º.
- Assets: tres baldosas «Conecta · Abarca · Drena» (SVG, rótulos ED).

## 069 — APROBADA (2026-10-06)
- Apertura de parada 10 · Paraná fósil / Santa Fe (izquierda, doble con 070).
- Cambios respecto del v2: «octubre,—» → «.—»; «llegfado» → «llegado»; «So!» → «Sol»; «Ip salobre» → «lo salobre».
- Assets: imagen PENDIENTE (barranca del Paraná, media página a sangre).

## 070 — APROBADA (2026-10-06)
- Parada 10 · fósil / hallazgo (derecha). «guaridasi» → «guaridas!».
- El final del v2 está dañado (repite el comienzo de 071 y salta a un tramo de la pág. 183): se quita y el texto termina en «lavado de las Pampas.».
- Assets: corte del tajo con los dos esqueletos, el diente y los huesos (SVG, ED; formas convencionales).

## 071 — APROBADA (2026-10-06) · VERIFICACIÓN DOCUMENTAL PENDIENTE
- Parada 10 · narrativa + esquema (izquierda). La pág. 182 del libro falta en el escaneo; el texto está en la capa de texto (fuera de orden) y coincide con el v2. Lleva un aviso visible en la página, que se quita cuando se coteje con un original completo.
- Cambios respecto del v2: «3**» → «3°». Nota E (1) tomada de la fuente («género Cocías» → «Cactus», DUDA). Nota ED: «Corunda» es Coronda.
- Assets: esquema de lo que cambia hacia el Norte (SVG, ED).

## 072–104 — revisión (tramo final, compuesto el 2026-10-06)
El detalle de cada página está en el comentario que abre su archivo (pages/NNN.html). Resumen de lo que no es rutina:

- 072: «hoVas» → «horas». Esquema del laberinto de ramales (no es mapa).
- 073–074: el v2 repite el mismo pasaje en las dos; queda solo en 074. 073 lleva la primera frase y la imagen PENDIENTE de los riscos.
- 075, 076, 081, 093: […] al final (el v2 corta a mitad de frase). 076: nota D (1) de la fuente; los pasos 3 y 4 del método resumen lo que sigue en el diario.
- 077: «plan-’ ta» → «planta». 078: «quehubiera» → «que hubiera».
- 079–080: «prolong-ar», «varías», «preseíitan» corregidos; la frase repetida («Estas espesuras…») queda solo en 080; en 080 se quita el pie de figura metido en «estrecho»; nota E (1) con «Felis onça» (DUDA).
- 082: se repone «Habiéndome visto forzado a detenerme» (fuente) al comienzo del segundo tramo; «al fín» → «al fin». Se conserva la mención del paquebote a Montevideo.
- 083–084: «, —» → «.—»; «alg-unas» → «algunas».
- 085: «apariencia. lento» → «apariencia lento»; nota E (3) con «Lama huanacus» (DUDA).
- 088: «Thirsty Hill, la Montaña Sedienta» (DUDA: en la fuente la línea está partida y parece faltar una palabra).
- 089–091: REORDENADO. 090 lleva el pasaje completo de los guijarros («Estos blancos estratos… conchas terciarias. […]») con nota E (1). 091 (Macrauchenia) NO usa el texto del v2: lleva el pasaje de la fuente que trata del animal (pág. 258); se quitó la llamada (1). REQUIERE OK DE PATRICIO.
- 092: primera pregunta en cuerpo mayor; nota E (1) de la fuente. No se cierra con respuesta moderna.
- 096: nota D (1) de la fuente. 097: «antig’uos» → «antiguos». 099: «montana» → «montaña».
- 100: se quita el encabezado de página metido en el texto («US bARWlN: VIAJE DEL…»). Esquema final: la Cordillera vista, no alcanzada.
- 101: mapa general (el de 007, PROVISORIO) + quince paradas con el medio de viaje. 102: una observación por parada (rótulos del v2). 103: fuentes (texto del v2) + código de notas + créditos PENDIENTES. 104: colofón (texto del v2), QR PENDIENTE, imagen de cierre PENDIENTE; sin folio.

## Pendientes generales antes de la entrega
- Cotejo VISUAL contra el escaneo de todas las palabras marcadas DUDA y verificación documental de 071.
- Tildes dejadas como en la fuente (043, 044, 045, 049, 050, 053, 081 «navio», 088 «nivea»): decide Patricio.
- Mapas PROVISORIOS (costas esquemáticas): 007, 008, 011, 017, 101. Imágenes con placeholder: ver ASSET_MANIFEST. QR: 006 y 104.
- Exportación con sangrado y marcas de corte (no implementada); tamaño de página del PDF de Chrome: 209,9 × 148,2 mm.

## Ilustraciones colocadas (7 oct. 2026)

Se reemplazaron los 39 recuadros de imagen pendiente por ilustraciones generadas con ChatGPT a partir de dos referencias de estilo del proyecto (páginas 013, 014, 015 ×2, 019, 023, 025–030, 033, 035, 037, 039, 041, 043, 044, 047, 050–052, 054, 062, 064, 065, 067, 069, 073, 075, 077, 080, 083, 085, 087, 091, 095 y 104).
- Autorizado por el usuario, incluidas las páginas ya aprobadas (013–069): en ellas solo cambió el recuadro pendiente por la imagen; texto, cajas y retícula quedan iguales. Se volvieron a bloquear.
- Originales en `assets/images/originales/`; recorte a la caja y paso a las dos tintas con `tools/fotos.py`; estilos en `styles/fotos.css`.
- Folio sobre chapa de papel en 025, 027, 069, 073 y 087 (el folio cae sobre una imagen a toda altura).
- Siguen pendientes: QR (006, 104), créditos de imágenes (103), mapas provisorios, imágenes provisorias de 011 y 020.
- A revisar: 065 (la vizcacha se parece a un conejo), 080 (ilustración nueva, no la figura de la edición de 1921), 085 (el recorte apaisado corta las patas del guanaco), 035 (el recorte deja fuera la luna).

## Tapa, guardas y QR (12 oct. 2026)
- Tapa (opción A) y contratapa incorporadas a index.html como primera y última página; se toman de tapa/tapa.html. Guardas vacías, sin rótulo.
- QR del mapa digital colocado en 006, 104 y contratapa (assets/images/qr-mapa-digital.svg, vectorial, azul sobre papel). 006 vuelta a aprobar con autorización del usuario.
- No se pudo leer el destino del QR desde acá: falta probarlo con un teléfono sobre una impresión.
- Siguen pendientes: créditos de imágenes (103), mapas provisorios, sangrado y marcas de corte de la tapa, ancho real del lomo.
- 004: mosaico de pictogramas reemplazado por una tira de seis fragmentos de láminas del libro (tools/fragmentos.py). PENDIENTE de aprobación del usuario.
- 006: esquemas de «Libro» y «Mapa digital» reemplazados por mockups fotográficos recortados (tools/recorte.py), en color. Fichas: sigue el esquema hasta tener mockup.
- 021–022: pictogramas reemplazados por láminas en grabado (tools/laminas.py). Aprobadas de nuevo por pedido del usuario.
- Contratapa: Megatherium nuevo con el árbol completo (tapa-megatherium.jpg). La 043 conserva el anterior.
- 043: Megatherium nuevo también en la página (REEMPLAZOS en tools/fotos.py). 004 aprobada.
- 021–022: recomposición (dos franjas en 021; mosaico de 022 a la altura del texto).
- 068: los tres esquemas (conecta · abarca · drena) reemplazados por láminas en grabado generadas con ChatGPT (tools/laminas.py). Aprobada de nuevo por pedido del usuario.

## RENUMERACIÓN +1 (12 oct. 2026) — LEER ANTES DE USAR NÚMEROS DE PÁGINA
- Pedido del usuario: el libro se muestra como impreso (tapa → carilla de cortesía en blanco → dobles) y la carilla cuenta como página 001.
- TODO lo anterior a esta entrada usa la numeración vieja. Página nueva = página vieja + 1 = entrada del plan v2 + 1.
- Se renombraron: pages/NNN.html, clases pNNN__ y #pNNN en HTML/CSS, data-page, approved.lock, imágenes assets/images/NNN-*, originales NNNx-*, tablas de tools/ y ASSET_MANIFEST. Los comentarios «entrada NNN» del v2 NO se tocaron.
- Paridad: par = izquierda, impar = derecha. 001 (cortesía) y 106 (guarda final) en blanco, sin archivo: las genera build.mjs.
- Referencias visibles actualizadas: índice de paradas (011), «páginas 051–059» (052), «páginas 061 y 062» (062), «página 061» (083).
- Verificado comparando el PDF anterior y el nuevo página por página: solo cambian folios y esas referencias.
- Respaldo previo: ../_respaldo_antes_de_renumerar.zip.
- Pendientes en numeración nueva: guanaco 086, vizcacha 066, créditos 104, verificación documental 072, mapas provisorios 008, 009, 013, 018, 102; en revisión 073–105.

## Publicación en GitHub (12 oct. 2026)
- Repo público: https://github.com/patriciocampodonico/darwin-en-la-argentina-libro (carpeta book/, sin salida/ ni originales/).
- Página para la compañera (GitHub Pages, rama main): https://patriciocampodonico.github.io/darwin-en-la-argentina-libro/
- Después de cada cambio: node build.mjs → git add -A → git commit → git push. La página se actualiza sola en 1–2 minutos.
- 010–011: un solo título para la doble («Cronología 1832–1834»); los rangos del v2 quedan como rótulos de tramo; índice de paradas subido. Aprobadas de nuevo por pedido del usuario.
- Web: la doble entra completa al abrir (zoom --fit en print.css + viewport 1280) y los CSS llevan sello de versión.
- 011: índice de paradas sobre panel azul a sangre (columnas 5–6, de arriba abajo), más interlineado (1,5 líneas) y rótulo a 13 pt; folio de 011 en color papel.
- 058 y 067: las franjas de río pasan de azul plano a textura de agua en grabado (ChatGPT, tools/laminas.py → agua); nombre del río en Inter negrita a 15 pt. Solo CSS e imágenes: siguen bloqueadas.
- MAPAS (008, 009, 013, 018, 102): cartografía real de Natural Earth 1:10m (tools/geodatos.py → assets/maps/geo.json): costa, límite internacional, ríos y lagos; Malvinas como Argentina; vecinos en tono claro. Recorrido a caballo posta por posta; Santa Cruz por el cauce real. Ya no son provisorios. 008, 009, 013 y 018 aprobadas y bloqueadas de nuevo (12 oct. 2026).
- 006: la muestra de «Texto de Darwin» lleva […] y la descripción pasa a «Fragmentos seleccionados del diario, en la tipografía de la muestra.» Aprobada de nuevo.
- 014–015: una sola imagen del bosque para la doble (ChatGPT; tools/laminas.py la parte por el lomo; fotos.py las saltea con APARTE). Mismos nombres de archivo: las páginas siguen bloqueadas.
- 019: la sección del cantil baja al pie de la caja (mismas filas que el mapa de 018) y su nota ED pasa a la derecha, abajo. Solo CSS.
- 019: el texto de Darwin baja a la fila 11, la misma línea en que arranca el de 018. Solo CSS.
- 019: el título baja a las filas 7–8; comparte línea de base con la segunda línea del título de 018. Solo CSS.
- 019: título en filas 3–4, con el tope de las mayúsculas a la misma altura que la primera línea del título de 018 (ajuste fino de 0,35 mm). Solo CSS.
- 021: una línea de aire entre el rótulo «Las medidas del fragmento» y los filetes de los datos. Solo CSS. El mismo rótulo pegado a los filetes sigue así en 058 y 064 (ofrecido al usuario).
- 022–023 reestructuradas: en 022 el texto sube arriba a la derecha (junto al título, como 044), la nota ED queda bajo el título y las dos láminas pasan a 12 líneas de alto (cristal sigue a 7 cm reales); en 023 el mosaico 2 × 2 ocupa las columnas 4–6, pegado al texto. El pie de las láminas de 022 coincide con el de las viñetas de 023.
- 022 (ajuste pedido): texto de Darwin bajo el título (cols 1–3, filas 5–12), nota ED a su derecha terminando con la última línea del texto, láminas de 11 líneas (filas 14–24). 023 queda como estaba.
- 023: el mosaico baja dos líneas (filas 9–28); el pie de las imágenes de abajo coincide con la última línea del texto. Solo CSS. Las láminas de 022 terminan ahora dos líneas más arriba que las viñetas de 023.
- 025: el esquema del camino y su nota ED bajan al pie de la caja, a la altura de la imagen de 024. Solo CSS.
- 023 (corrección): rótulo ED en la fila 7 (primera línea del texto), imágenes en 8–15 y 18–25, epígrafes en 16 y 26 (última línea del texto). Solo CSS.
- 027: texto a 2 columnas (21 líneas) e imagen a 4 columnas, mismas filas 7–27: empiezan y terminan juntos. Excepción pedida por el usuario a la medida de 3 columnas del cuerpo. Imagen re-recortada (fotos.py, 124,3 × 94,5 mm).
- 2026-10-12 · 029: el rótulo ED «Las cuatro cosas necesarias» y su lista bajan dos líneas; el rótulo arranca a la altura de la primera línea del texto (solo CSS, styles/medida.css; la página sigue bloqueada).
- 2026-10-12 · 030–031 recompuestas a pedido de Patricio. 030: la figura del agutí pasa a las columnas 4–6 (imagen de 13 líneas, alineada a la izquierda), su pie y la nota ED debajo (solo CSS). 031: la imagen baja a las líneas 7–20, igual que el texto; el esquema del río se redibuja en franja a todo el ancho (líneas 22–27, viewBox 188 × 27, curva de meandros generada) con la nota ED en la línea 28. Cambió el HTML de 031 (solo el SVG): re-aprobada.
- 2026-10-12 · 033 recompuesta a pedido de Patricio, a la par de 032: texto en dos columnas anchas desde la línea 10 (como 032), perfil de dunas redibujado en franja a todo el ancho (líneas 19–26, viewBox 188 × 36) y nota ED en la línea 28, a la altura de la de 032. Cambió el HTML de 033 (solo el SVG): re-aprobada.
- 2026-10-12 · 035 a la par de 034 (pedido de Patricio): la planta del fuerte se alarga (viewBox 92,34 × 85,5) y termina en la línea 25, como la imagen de 034; su nota ED y las notas E/ED del texto bajan al pie y cierran en la línea 27, donde termina el texto de 034. El rótulo «Muralla» ya no se sale de la caja. Cambió el HTML de 035 (solo el SVG): re-aprobada.
- 2026-10-12 · 036–037: la franja de Punta Alta cruza la doble. Imagen nueva de ChatGPT (continuación hacia la derecha de la de 036; original en assets/images/originales/037-punta-alta.webp, la prepara tools/laminas.py con el mismo recorte que 036 → assets/images/037-punta-alta.jpg, 186 ppp). 037 recompuesta bajo la franja: título en la línea 9 (donde empieza el de 036), texto y esquemas desde la 12, nota ED cierra en la 28. Cambió el HTML de 037 (se agregó la imagen): re-aprobada. Falta sumar esta imagen a los créditos de 104.
- 2026-10-12 · 038–041 recompuestas por encargo de Patricio (trabajo autónomo: huecos, composición y alineación entre página izquierda y derecha; misma información). 038: lista en dos columnas anchas arriba (1.º–2.º | 3.º–4.º), lámina de los esqueletos centrada y más grande al pie (116 mm de ancho, antes 90; termina en la línea 27 como el plano de 039), nota ED en la línea 28 como la de 039 (solo CSS). 039: sin cambios. 040: imagen recortada a 13 líneas (7–19, igual que el texto; tools/fotos.py), esquema de distancia desde la línea 21 (viewBox recortado arriba) y su nota ED a la derecha, a la misma altura. 041: corte de capas redibujado más alto (líneas 7–19, como la imagen de 040), conchas bajo el texto desde la línea 21 y nota ED a la derecha. Cambió el HTML de 040 y 041 (solo los SVG): re-aprobadas.
- 2026-10-12 · 038: los cuatro esqueletos se recortan uno por uno y se reparten a todo el ancho de la caja, con ~16 mm de aire entre ellos (tools/laminas.py → assets/images/038-megaterios-fila.jpg, 308 ppp; misma escala relativa). 039: el plano de los 200 m² se achata (viewBox 92,34 × 22,5) y termina en la línea 23, donde termina el texto de la derecha; su nota ED pasa a la línea 25. Cambió el HTML de 038 (archivo de imagen) y 039 (SVG): re-aprobadas.
- 2026-10-12 · 040: la imagen del cantil se alarga (líneas 7–22, recorte 92,3 × 72 mm, 361 ppp) y la nota ED termina en la línea 25, donde termina el esquema de distancia. 041: las conchas suben y terminan en la línea 22, donde termina la nota ED de la derecha. Solo CSS e imagen: las páginas siguen bloqueadas.
- 2026-10-12 · 038: esqueletos un 28 % más grandes (caja de 15 líneas, 13–27; 66,5 mm de alto el mayor; 241 ppp), con ~3 mm entre cajas; el Megatherium queda bajo la columna corta de la lista. Solo CSS e imagen: la página sigue bloqueada.
- 2026-10-12 · build.mjs: cada imagen de las páginas lleva un sello de versión (?v=hash del archivo). Motivo: al reemplazar una imagen con el mismo nombre (038), el navegador seguía mostrando la copia vieja en la página publicada.
- 2026-10-12 · 037 (ajuste pedido por Patricio): el texto baja a las líneas 14–28 y termina en la misma línea que el texto de 036; empieza a la altura del primer rótulo del esquema de visitas y termina con el último renglón de la nota ED. Para que entre la columna de esquemas, el corte del terreno se achata (viewBox 92,34 × 36; mismos rótulos). Cambió el HTML de 037 (SVG): re-aprobada.
- 2026-10-12 · 042–043 recompuestas a la par (trabajo autónomo, misma información). 042: la lámina del Scelidotherium sube a la derecha del texto (columnas 4–6, líneas 7–13: empieza y termina con el texto); el esquema de la grava se redibuja apaisado en franja a todo el ancho (líneas 19–26, viewBox 188 × 36, mismos elementos y rótulos), igual que la franja del tiempo de 043; nota ED al pie (27–28) como la de 043. 043: la nota D baja a la última línea del texto (15). Cambió el HTML de 042 (SVG): re-aprobada; 043 solo CSS.
- 2026-10-12 · 044–047 revisadas y recompuestas (trabajo autónomo, misma información; solo CSS e imagen, las cuatro siguen bloqueadas). 044: Megatherium más grande (ancho completo de las columnas 1–3, líneas 9–22) y notas al pie de la columna: D en 24–26, ED en la 28, donde termina el texto. 045: la pregunta baja a las líneas 8–11 y el texto a 15–28 para terminar como el de 044; la imagen empieza con el texto (15–25, recorte 92,3 × 49,5 mm) y la nota ED termina con él (27–28). 046: sin cambios. 047: el texto baja una línea (8–21) y termina como el de 046; notas y medidas pasan a la banda 24–28, la misma de la franja y la nota ED de 046.
- 2026-10-12 · 048–051 revisadas y recompuestas (trabajo autónomo, misma información). 048: texto en 20–25 y nota ED en 24–25, terminan juntos. 049: el corte sube a 16–23 y su nota ED a la 25, a la par del cierre de 048. 050: el esquema de los picos crece (viewBox 92,34 × 67,5; líneas 7–21) y su nota ED termina con el texto (25); las tres rocas pasan a una banda al pie, en fila (rótulo 27, lista 28). 051: la imagen empieza y termina con el texto (7–22; recorte 92,3 × 72 mm, foco a la izquierda, 361 ppp); el esquema del regreso pasa a franja a todo el ancho (24–27, viewBox 188 × 18) y las notas E y ED a la línea 28. tools/fragmentos.py: coordenadas del fragmento «montaña» de 005 adaptadas al nuevo recorte (no se regeneró 005). Cambió el HTML de 050 y 051 (SVG): re-aprobadas; 048 y 049 solo CSS.
- 2026-10-12 · 052–055 revisadas y recompuestas (trabajo autónomo, misma información). 052: la imagen termina con el texto (línea 20; recorte 92,3 × 45 mm). 053: texto, esquema y nota bajan una línea y cierran en la 28, como 052; la primera línea del texto queda en la línea de base del título. 054: el esquema de la región se alarga (viewBox 92,34 × 90; líneas 6–25) y su nota ED termina con el texto (28). 055: los tres números pasan de fila a columna, apilados junto al texto (líneas 7–19), cada uno apoyado en su filete; el último queda en el renglón final del texto. Cambió el HTML de 054 (SVG): re-aprobada; el resto solo CSS e imagen.
- 2026-10-12 · 055: la imagen de las hogueras va a sangre abajo y a la derecha (pedido de Patricio; caja 198 × 48 mm, 197 ppp); el folio queda sobre una chapa de papel. Solo CSS e imagen: sigue bloqueada.
- 2026-10-12 · 056–059 revisadas y recompuestas (trabajo autónomo, misma información). 056: la nota ED sube a la línea 27, donde cierra 057. 057: la planta de El Corral crece (viewBox 92,34 × 76,5; líneas 7–23; misma proporción entre los dos círculos) y su nota ED termina con el texto (27). 058: las dos medidas pasan de fila a columna, apiladas junto al texto (7–19) y apoyadas en su filete, como en 055; la nota ED de la franja baja a la línea 21, columnas 1–3, a la altura de las notas de 059. 059: sin cambios. Cambió el HTML de 057 (SVG): re-aprobada; el resto solo CSS.
- 2026-10-12 · 060–063 revisadas (trabajo autónomo, misma información; solo CSS, las cuatro siguen bloqueadas). 060: la nota ED pasa a la derecha del texto (columnas 4–6) y termina con él (línea 11). 061: las notas terminan con el texto (línea 11). 062: la nota ED cierra en la línea 28, como el texto y la imagen de 063. 063: sin cambios.
- 2026-10-12 · 060: el rótulo «Ciudad» pasa a «Ciudad de Buenos Aires», en 12 pt (pedido de Patricio). 061: el rótulo «Cuadra» va dentro de su cuadra, en papel, para que no lo corte la cuadra de arriba. Cambió el HTML de las dos: re-aprobadas.
- 2026-10-12 · 060: el esquema de puntos y rayas de las afueras se reemplaza por una lámina (ChatGPT; original assets/images/originales/060-afueras.webp → tools/laminas.py → assets/images/060-afueras.jpg, 135 mm de ancho, 289 ppp). Va dentro del SVG de la franja, se desvanece hacia las cuadras punteadas y arranca a la altura de la primera fila de cuadras de 061; el rótulo «Afueras…» sube sobre la lámina. HTML de 060 cambiado: re-aprobada. Falta sumar esta lámina a los créditos de 104.
- 2026-10-12 · 064–067 revisadas (trabajo autónomo, misma información; solo CSS, las cuatro siguen bloqueadas). 064: sin cambios. 065: el texto sube una línea (6–21) y termina como el de 064; el folio pasa a chapa de papel (caía sobre la imagen a media página y no se leía). 066: la lámina, el rótulo y la lista suben; el último ítem de la lista queda en el último renglón del texto (26). 067: sin cambios.
- 2026-10-12 · 067: la franja del río Paraná va a sangre también abajo (pedido de Patricio; textura recortada a 210 × 48 mm, 181 ppp); el folio queda sobre chapa de papel. Solo CSS e imagen: sigue bloqueada.
- 2026-10-12 · 068–073 revisadas (trabajo autónomo, misma información). 068: la nota ED termina con el texto (27). 069: rótulo y láminas bajan una línea; los pies cierran en la 27, como 068. 070: sin cambios. 071: el esquema de la barranca crece (viewBox 92,34 × 72; líneas 7–22) y su nota ED termina con el texto (25). 072: el esquema de latitud se alarga (viewBox 92,34 × 81; líneas 7–24); su nota ED y las notas del texto cierran en la 28, como la nota de 073. 073: sin cambios (sigue sin aprobar). Cambió el HTML de 071 y 072 (SVG): re-aprobadas; 072 conserva su aviso de verificación documental pendiente.
- 2026-10-12 · 074–105 revisadas (trabajo autónomo, misma información; ninguna de estas páginas está aprobada todavía). Con cambios: 077 (nota D termina con la lista), 078 (nota ED termina con el texto), 080 (esquema de la isla redibujado más alto; nota ED termina con el texto), 081 (nota E a la par de la nota ED), 082 (la franja baja una línea, a la altura de la de 083), 084 (el esquema del abra empieza con el texto), 085 (perfil más alto; nota ED termina con el texto), 086 (texto desde la línea 7; nota e imagen a la altura de la franja de grava de 087), 088 (esquema y nota bajan; la nota a la altura de los pies de 089), 094 (los tres números apilados junto al texto, como en 055), 096 (imagen, esquema y nota compactados; la nota termina con el texto), 099 (corte redibujado más alto; nota ED termina con el texto). Sin cambios: 074–076, 079, 083, 087, 089–093, 095, 097, 098, 100–105.
- 2026-10-12 · 072: VERIFICACIÓN DOCUMENTAL HECHA. La pág. 182 (que falta en el escaneo del proyecto) se cotejó a la vista con el facsímil de la misma edición (Espasa-Calpe 1921, tomo I) en Wikisource/Commons, imagen 209 del djvu: el texto del fragmento y la nota (1) coinciden palabra por palabra (comparación a la vista y mecánica contra la transcripción). Se confirma «3°» y «género Cactus» (ya no es duda). Se quita el cartel de la página; re-aprobada.
- 2026-10-12 · 024: la imagen de la salina va a sangre abajo y a la izquierda (pedido de Patricio; caja 198 × 43,5 mm, 197 ppp); el folio queda sobre chapa de papel. Solo CSS e imagen: sigue bloqueada.
