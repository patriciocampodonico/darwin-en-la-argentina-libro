# BOOK_SPEC — Darwin en la Argentina

Registro de decisiones del sistema. Los valores viven en `styles/tokens.css`; acá queda el porqué.

## Fuentes y jerarquía
1. `fuentes/01_Produccion/Darwin_textos_para_maquetar_v2.pdf` — plan operativo, 104 páginas. Se consulta la entrada antes de cada página.
2. Guía de cátedra · 3. TP4 · 4. Prompt maestro · 5. Corpus extraído (04/05) · 6. Escaneo crudo (06, comprobación).
7. Referencias visuales y web actual: lenguaje compartido, no se copia la interfaz.

## Decisiones fijadas (2026-10-06, aprobadas por Patricio)
| Tema | Decisión | Motivo |
|---|---|---|
| Formato | Apaisado 210 × 160 mm (antes A5, 148 mm; alargado el 15 oct. 2026 por corrección de la profesora), sangrado 3 mm | Fijo |
| Paginación | **Par = página izquierda, impar = derecha** (desde el 12 oct. 2026). 001 = carilla de cortesía en blanco, sin folio; 002–105 = contenido; 106 = guarda final en blanco. 106 páginas físicas + tapa y contratapa. **Página del libro = entrada del plan v2 + 1** (la entrada 004 del v2 es la página 005). |
| Márgenes | Sup. 16 · inf. 18 · interior 12 · exterior 10 mm (los 12 mm nuevos se repartieron arriba y abajo; la retícula de 28 líneas no cambió) | Folio a 7 mm del borde inferior |
| Retícula | 6 columnas de 28,42 mm, medianil 3,5 mm, caja 188 × 126 mm | Valores base del encargo |
| Línea de base | 4,5 mm (12,76 pt), 28 líneas | 4 mm (11,3 pt) quedaba por debajo de la interlínea pedida de 12,5–13 pt; 4,5 mm entra en el rango y divide la caja en 28 líneas exactas |
| Azul | `#1A3A5C` y tintas 80/60/40/20/10 % | El del encargo; la web (`#0A355E`) se unifica después |
| Papel | `#EFEEE6` | Mismo hueso que la web |
| Tipografías | Playfair Display · Lora · Inter (variables, OFL, en `assets/fonts/`) | Encargo. La web usa Fraunces: pendiente de unificar del lado web |
| Cuerpo Darwin | Lora 9,25 pt / 12,76 pt | Rango 9–9,5 / 12,5–13 |
| Rótulos del v2 | Se restituyen las tildes en títulos y metadata editorial (el v2 las trae sin tildes). El texto de Darwin no se toca | Son texto editorial del proyecto, no fuente |
| Notas | D = Darwin · E = edición española · ED = editorial del proyecto; nunca mezcladas | Encargo |

## Estilos tipográficos en uso
| Clase | Uso | Valor |
|---|---|---|
| `.t-opening` | Grandes aperturas | Playfair 36 pt / 3 líneas de base |
| `.t-display-line` | Línea display de tamaño libre que conserva la línea de base de las aperturas | Playfair, `--size` (título 26 pt, subtítulo 14 pt) |
| `.t-label` | Autor, rótulos destacados | Inter Medium 9 pt |
| `.t-data` | Datos y créditos en bloque | Inter 7,5 pt / 3 mm (3 líneas cada 2 líneas de base) |
| `.t-meta` | Metadata y rótulos mínimos | Inter Medium 7 pt (6,5 pt en variante chica) |

## Reglas de sistema fijadas al maquetar
- **Dos voces, dos familias**: Lora es solo para el texto de Darwin. La voz editorial del proyecto (introducciones, explicaciones, notas ED) va en Inter (`.t-editorial`, 9,5 pt / 4,5 mm).
- **Alturas de colgado en la apertura**: antetítulo o autor en la línea 6; título en las líneas 8–10; texto desde la línea 12.
- **Folio**: número de tres dígitos + sección («004 Apertura»), Inter 6,5 pt, margen inferior del lado exterior. Lo agrega el build a las páginas con `data-section`. 002 y 003 no llevan.
- **Imágenes de fondo «muy tenues»**: una tinta azul con transparencia, opacidad `--tenue` (30 %).

- **Código visual (página 006)**, definido en `styles/components.css`: texto de Darwin en Lora (`.t-darwin`); fecha y lugar con `.stopline`; notas con `.notetag` (D y E en contorno, ED llena); baldosa de registro; trazos de recorrido; `.placeholder` para assets pendientes.
- **Páginas densas**: el título sube a las líneas 2–4 y el contenido arranca en la línea 7.

- **Mapas**: vectoriales, generados desde coordenadas con `tools/mapas.mjs` y definidos en `styles/maps.css`. Tierra en azul al 20 %, costa en línea fina, retícula de paralelos y meridianos. Recorrido terrestre en línea llena; fluvial / marítimo en trazos; parada = punto; registro científico = rombo. El recorrido del río Santa Cruz se corta antes de la Cordillera.
- **Paradas**: se nombran siempre con número de dos dígitos en negrita + nombre; la fecha va debajo o al lado en Inter 7 pt.
- **Línea de tiempo**: entradas alternadas arriba y abajo de una línea continua que cruza la doble.

- **Páginas de parada** (`styles/paradas.css`): apertura con título en Playfair 36 pt; páginas narrativas con título en Playfair 20 pt (`.t-pagetitle`). Texto de Darwin en Lora 9,25 pt / 4,5 mm, alineado a la izquierda con corte de palabras; en 3 columnas de ancho (≈62 caracteres) o en dos columnas de 2 (≈40 caracteres). El folio lleva número y nombre de la parada.
- **Cortes editoriales**: […] siempre visible, en azul al 60 %.
- **Notas en página**: debajo del texto, en Inter 7,5 pt, con etiqueta D, E o ED. La llamada (1) se conserva en el texto como en la fuente.
- **Cotejo**: el escaneo (06) trae capa de texto; por ahora se coteja contra esa capa. El cotejo visual de las páginas escaneadas está pendiente (falta un visor de PDF en el entorno).

- **Registros y esquemas** (`styles/registros.css`): las páginas de registro llevan antetítulo «Registro de campo» con baldosa chica. Los esquemas hechos por el proyecto (perfiles, secciones, datos destacados) usan solo datos del fragmento de la página y llevan etiqueta ED.
- **Criterio de texto**: cuando el v2 corta a mitad de frase sin marcarlo, se agrega […]. Los errores evidentes de reconocimiento se corrigen y se anotan en el comentario inicial de cada página y en BOOK_PROGRESS.

- **Página oscura** (`data-tone="dark"`, en `styles/tramo-03.css`): fondo azul pleno y texto en color papel. Reservada a escenas de noche o pausas inmersivas; usar con moderación.
- **Frase en cuerpo mayor** (`.t-pullquote`): una frase de Darwin puede componerse en Playfair 20 pt en su lugar dentro del fragmento; nunca se repite ni se saca de orden.
- **Solapes del v2**: cuando un mismo tramo cierra una entrada y abre la siguiente, se deja solo en la segunda.

- **Cuerpo de texto justificado** (pedido por Patricio el 2026-10-06, aplicado a todo lo maquetado, incluidas las páginas aprobadas): el texto de lectura —fragmentos de Darwin y párrafos de la introducción (004–005)— va justificado con la última línea alineada a la izquierda. Fuente, cuerpo e interlínea no cambian. Para no abrir ríos, el build inserta guiones opcionales con división silábica del español (`tools/silabas.mjs`): mínimo 2 letras antes y 3 después del corte, sin partir palabras con mayúscula inicial. Sin viudas ni huérfanas al pasar de columna (`widows` / `orphans` 2). No se justifican notas, pies, rótulos ni listas. El cambio vive en `styles/paradas.css` y en el build; los archivos de página no se modificaron.
- **Medida del cuerpo** (autorizado por Patricio el 2026-10-06): el texto de lectura va siempre a 3 columnas de retícula de ancho (≈92 mm, unas 62 letras por línea). Quedan prohibidas las columnas de texto de 2 columnas de retícula: justificadas abrían ríos. Se recompusieron 013, 015, 017, 020, 023, 029 y 030 desde `styles/medida.css`, que se carga última; los archivos de página no cambiaron (conservan las clases `--2col` / `--3col`, hoy anuladas).
- **A vigilar**: en 017 el texto corre en dos columnas anchas y una palabra queda partida entre ambas.

## Implementación
- Una página = `pages/NNN.html` (fragmento). `node build.mjs` arma `index.html`.
- Composición sobre la retícula con `grid-column` / `grid-row`; estilos por página en `styles/pages.css`.
- Revisión: abrir `index.html` (tecla **G** muestra la retícula; `?p=002` aísla una página).
- `node build.mjs shot 002` → PNG, PNG con retícula y PDF en `salida/`; `shot 002-003` → PNG de la doble enfrentada. `node build.mjs pdf` → libro completo.
- `node build.mjs approve 002` bloquea una página aprobada (`approved.lock`); el build avisa si cambia.

## Pendientes del sistema
- Variante de exportación con sangrado de 3 mm y marcas de corte (todavía no implementada; ninguna página la necesita aún).
- Chrome exporta la página a 209,9 × 148,2 mm (redondeo a píxel). Revisar al preparar originales de imprenta.
- Alineación de títulos Playfair a la línea de base: hoy se alinea la caja de línea, no la base de la letra.
- Perfil de color / conversión CMYK del azul para imprenta.

## Advertencias documentales
- **072**: VERIFICACIÓN DOCUMENTAL PENDIENTE (llegada a Santa Fe; la página falta en el escaneo).
- **Río Santa Cruz (094–101)**: Darwin ve la Cordillera pero no la alcanza. Nunca representar llegada a las cumbres.
- Uruguay queda fuera del recorte.
- OCR a cotejar contra el escaneo cuando toque: «Patagonía» (012), «Fagas» (016), «Corunda» y «3**» (072); párrafo partido en 015; final sin punto en 015.
