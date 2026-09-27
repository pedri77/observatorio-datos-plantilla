# Plantilla: tu observatorio de datos públicos con IA

Plantilla gratuita de la serie **«Construido con IA»** de [IAcademy](https://iacedemy.com/free/yt/construido-con-ia/). Es la base mínima de proyectos como [Techo](https://pedri77.github.io/mapa-vivienda-espana/) (vivienda) y [Oferta Única](https://pedri77.github.io/oferta-unica/) (contratación pública).

Incluye un ejemplo que funciona desde el primer minuto: el **coste salarial por comunidad autónoma** se descarga cada día de la API del INE, se valida y se publica en un mapa con tabla. Gratis, sin servidores.

## Empieza en 5 minutos

1. Pulsa **Use this template → Create a new repository** (público).
2. En tu repositorio nuevo: **Settings → Pages → Source: GitHub Actions**.
3. Ve a **Actions → Actualizar datos y publicar → Run workflow**.
4. En un par de minutos tendrás la web en `https://TU-USUARIO.github.io/TU-REPO/`.

Se actualizará sola cada día a las 06:00 UTC.

## Adáptalo a tu pregunta

| Paso | Qué hacer | Ayuda |
|---|---|---|
| 1 | Define tu pregunta, tu público y 3-5 fuentes oficiales | [datos.gob.es](https://datos.gob.es), [INE](https://www.ine.es), boletines oficiales |
| 2 | Investiga con agentes que citan fuentes | `prompts/01-investigacion.md` |
| 3 | Adapta `scripts/actualizar.py`: cambia `FUENTE`, `transformar()` y `validar()` | Comentarios en el propio script |
| 4 | Verifica los datos | `prompts/02-verificacion.md` |
| 5 | Ajusta `site/index.html` (título, unidad, colores) | — |
| 6 | Revisa la web antes de publicar | `prompts/03-revision-visual.md` y `CHECKLIST.md` |

## Estructura

```
scripts/actualizar.py        descarga, transforma y valida → site/data.json
site/index.html              mapa (Leaflet) + tabla ordenable, sin dependencias de build
site/ccaa.geojson            límites de comunidades autónomas (es-atlas, IGN)
.github/workflows/           actualización diaria y publicación en GitHub Pages
prompts/                     los prompts usados en Techo y Oferta Única
CHECKLIST.md                 lo que hay que revisar antes de publicar
```

## En local

```bash
python3 scripts/actualizar.py
python3 -m http.server -d site 8000   # abre http://localhost:8000
```

## Aprende a construirlo paso a paso

El proyecto guiado de IAcademy lleva esta plantilla hasta un observatorio completo: varias fuentes, municipios, calculadora, vigilancia de fuentes con avisos y publicación responsable. [iacedemy.com](https://iacedemy.com/free/yt/construido-con-ia/?utm_source=github&utm_medium=plantilla&utm_campaign=construido-con-ia).

## Licencia

Código: MIT. Límites territoriales: [es-atlas](https://github.com/martgnz/es-atlas) (IGN). Datos del ejemplo: INE, reutilizables citando la fuente.
