# Dashboard gerencial · CEDIA Academia / TMO

## Consultar ahora

Abra `docs/index.html` con Chrome, Edge, Firefox o Safari. Es autónomo: incluye los datos y los gráficos, sin servicios externos, instalación ni conexión a internet.

## Publicar en GitHub Pages

1. Ingrese a su cuenta de GitHub y cree un repositorio, por ejemplo `cedia-tmo-dashboard`. Ese nombre es una sugerencia; todavía no se ha creado ningún repositorio.
2. Suba la carpeta `docs` conservando `docs/index.html`. Puede incluir los archivos fuente y esta guía en la raíz para mantener el proyecto.
3. En el repositorio vaya a **Settings → Pages → Build and deployment**.
4. En **Source**, seleccione **Deploy from a branch**. Seleccione la rama **main**, carpeta **/docs**, y guarde.
5. Espere la publicación y abra la dirección que GitHub muestra en Pages. Comparta esa dirección con gerencia. No comparta la dirección del archivo dentro del repositorio como si fuera el visor.

La disponibilidad de Pages depende del plan y la visibilidad del repositorio. Este paquete no requiere contraseña ni un servidor propio; el visor publicado está pensado para acceso público. No contiene el Excel original ni su desglose institucional.

Documentación oficial consultada el 9 de noviembre de 2026:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Indicadores y controles

- Inscripciones: suma de registros del período y línea seleccionados. No representa personas únicas.
- Ofertas con inscripciones: columnas del catálogo con al menos un registro positivo; los módulos TMO se cuentan de forma independiente.
- Mes de mayor demanda: mes con más inscripciones dentro de la selección. Si hay empate, se presenta el primero cronológicamente.
- Concentración top 1: inscripciones de la oferta más demandada divididas para el total seleccionado.
- Filtros de inicio, fin y línea; ajuste automático para impedir un intervalo invertido.
- Búsqueda por nombre que afecta solamente el detalle y el CSV.
- Exportación CSV compatible con Excel y opción de imprimir/guardar PDF desde el navegador.

## Conciliación del archivo recibido

| Línea | Inscripciones enero–octubre |
| --- | ---: |
| TMO | 3.036 |
| TMO Track | 4.405 |
| Cisco | 634 |
| Total | 8.075 |

Los 30 totales de mes y línea se conciliaron con B19:D28 de la hoja `TMO TRACK-CISCO 2026`. El total coincide con E31. TMO procede de B84:DH84 de la hoja `2026`. Cisco y TMO Track proceden de B3:U12 de `TMO TRACK-CISCO 2026`.

La fila de invitados en la hoja TMO aporta 15 registros que ya están incorporados en sus totales; no se suman nuevamente. No se usan las filas auxiliares ni el valor 212 como cursos impartidos. El catálogo visible tiene 111 columnas TMO, 13 Track y 7 Cisco: 131 ofertas con inscripciones. Esto no es una medición de certificaciones completas, horas impartidas o personas únicas.

Noviembre y diciembre están sin información. Se muestran como s/d en la evolución y tabla. No se calculan metas, ingresos, satisfacción, certificación o cobertura institucional porque esta versión pública no dispone de esos indicadores.

Hallazgo descriptivo: Equidad de Género suma 3.744 registros (46,4% del total). Septiembre y octubre suman 4.535 registros (56,2%). Esto describe concentración de demanda; no permite atribuir causas ni medir impacto educativo.

## Actualizar

El visor es una fotografía del archivo recibido, no una conexión en vivo. Para correcciones que conserven el mismo diseño de Excel y el corte enero–octubre:

1. Abra y guarde el Excel en Excel/LibreOffice para actualizar sus fórmulas y valores calculados.
2. Con Python y openpyxl disponibles, ejecute `python generar_datos.py "ruta/al/archivo.xlsx"` desde la carpeta del proyecto.
3. El generador concilia los totales por línea y mes, y reconstruye `docs/index.html` usando `plantilla.html`.
4. Revise el resultado y reemplace `docs/index.html` en GitHub. Pages publicará el cambio.

Para añadir noviembre, diciembre, otro año o cambiar filas/columnas del Excel se debe adaptar el generador y el corte/metodología de la plantilla. El importador está diseñado para la estructura recibida; no es un importador universal de Excel. Mantenga el Excel fuera del repositorio público.

## Verificación realizada

Conciliación de 30 totales mensuales, carga en navegador, filtro TMO (3.036), período sin registros y búsqueda Equidad (3.744). Se revisó visualmente la vista de escritorio. No se verificó un despliegue en GitHub: requiere conectar la cuenta y seleccionar el repositorio. No se hizo una prueba visual en dispositivo móvil.
