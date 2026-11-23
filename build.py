"""Build a single self-contained HTML from local vendor bundles."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
LIBHEIF = (ROOT / "vendor" / "libheif-bundle.js").read_text(encoding="utf-8")
FFLATE = (ROOT / "vendor" / "fflate.js").read_text(encoding="utf-8")
TPL = (ROOT / "src" / "app.template.html").read_text(encoding="utf-8")
OUT = ROOT / "HEIC转PNG-无损批量转换.html"

# libheif source as a JS string literal (JSON encoded, safe for <script>)
libheif_literal = json.dumps(LIBHEIF, ensure_ascii=False)
html = TPL.replace("/*__LIBHEIF__*/", LIBHEIF)
html = html.replace("/*__FFLATE__*/", FFLATE)
html = html.replace("/*__LIBHEIF_LITERAL__*/", libheif_literal)
OUT.write_text(html, encoding="utf-8")
print(f"built: {OUT} ({OUT.stat().st_size:,} bytes)")
