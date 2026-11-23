#!/usr/bin/env python3
"""N7 build step: copies slides/content.json into the embedded FALLBACK_SLIDES block of slides/index.html,
so the HTML can never drift away from the checked content.  Usage: python3 -I tools/build_slides.py [project_root]"""
import json, os, re, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
slides = json.load(open("slides/content.json", encoding="utf-8"))
html = open("slides/index.html", encoding="utf-8").read()
block = "const FALLBACK_SLIDES = " + json.dumps(slides, ensure_ascii=False, indent=6).replace("\n", "\n    ") + ";"
new, n = re.subn(r"const FALLBACK_SLIDES = \[.*?\n    \];", lambda m: block, html, count=1, flags=re.S)
if n != 1: sys.exit("FAIL: FALLBACK_SLIDES block not found in slides/index.html")
open("slides/index.html", "w", encoding="utf-8").write(new)
print(f"built slides/index.html from content.json ({len(slides)} slides)")
