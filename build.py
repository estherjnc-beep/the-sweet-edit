"""Arma la web de The Sweet Edit.

Uso: python3 build.py 02
Lee src/template.html + data/archivo.js + data/edicion-NN.js y escribe:
  - index.html (edición actual)
  - ediciones/edicion-NN.html (copia para el archivo)
"""
import sys, pathlib
n = sys.argv[1]
root = pathlib.Path(__file__).parent
tpl = (root / "src/template.html").read_text(encoding="utf-8")
data = (root / f"data/edicion-{n}.js").read_text(encoding="utf-8")
arch = (root / "data/archivo.js").read_text(encoding="utf-8")
assert "/*DATA*/" in tpl
html = tpl.replace("/*DATA*/", data + "\n" + arch)
(root / "index.html").write_text(html, encoding="utf-8")
(root / "ediciones").mkdir(exist_ok=True)
# en la copia del archivo, los enlaces a otras ediciones suben un nivel
(root / f"ediciones/edicion-{n}.html").write_text(html.replace('"ediciones/', '"../ediciones/'), encoding="utf-8")
print("OK: index.html y ediciones/edicion-%s.html" % n)
