# THE SWEET EDIT.
**Global Sweet Industry Intelligence** · *Where sweet meets strategy.*

Lo que se mueve en el mundo dulce: plataforma de inteligencia competitiva, innovación y tendencias de la industria de snacks dulces.

🌐 Web: https://estherjnc-beep.github.io/the-sweet-edit/

## Cómo está organizado
| Carpeta / archivo | Qué contiene |
|---|---|
| `index.html` | La edición más reciente (la que se ve en la web) |
| `ediciones/` | Copia de cada edición publicada |
| `data/edicion-NN.js` | Los datos de cada edición (historias, señales, competencia, packaging) |
| `data/archivo.js` | Lista de ediciones para la sección “Ediciones anteriores” |
| `src/template.html` | Diseño de la web (no cambia entre ediciones) |
| `build.py` | Une diseño + datos: `python3 build.py 02` |

## Actualización semanal
Cada lunes se agrega `data/edicion-NN.js`, se actualiza `data/archivo.js`, se ejecuta `build.py` y se publica.
