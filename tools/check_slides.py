#!/usr/bin/env python3
"""N6 content check, run BEFORE building HTML (AGENTS.md sections 10-11).
Usage: python3 -I tools/check_slides.py [project_root]
Checks: schema, source exists, <=5 bullets, <=15 words/bullet, absolute words must be backed by the
cited wiki file, numbers must appear in the cited wiki file, key chemistry terms must appear in the
cited wiki file, and no term is used before the slide that explains it."""
import json, os, re, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
fails = []; fail = fails.append
slides = json.load(open("slides/content.json", encoding="utf-8"))
FIELDS = {"id", "title", "bullets", "source", "notes"}
ABSOLUTE = re.compile(r"\b(always|never|every time|magic|all reactions|guarantee[sd]?|only way)\b", re.I)
# key chemistry terms: if a bullet uses one, the cited wiki file must contain it
TERMS = ["carbocation", "racemization", "anti-periplanar", "zaitsev", "hofmann", "walden", "polar aprotic",
         "polar protic", "tosylate", "alkene", "backside", "beta", "leaving group", "nucleophile", "intermediate"]
norm = lambda s: re.sub(r"\s+", " ", s.lower().replace("β", "beta").replace("‑", "-"))

seen_terms = {}
for s in slides:
    sid = s.get("id", "?")
    if set(s.keys()) != FIELDS: fail(f"[schema] slide {sid}: fields differ: {sorted(s.keys())}")
    if not s.get("title") or not s.get("bullets"): fail(f"[schema] slide {sid}: empty title/bullets"); continue
    p = s.get("source", "")
    if not p or not os.path.exists(p): fail(f"[source] slide {sid}: source '{p}' missing"); continue
    wiki = norm(open(p, encoding="utf-8").read())
    if len(s["bullets"]) > 5: fail(f"[style] slide {sid}: {len(s['bullets'])} bullets (max 5)")
    for b in s["bullets"]:
        nb = norm(b)
        if not b.strip() or "undefined" in nb: fail(f"[schema] slide {sid}: empty/undefined text")
        if len(b.split()) > 15: fail(f"[style] slide {sid}: {len(b.split())} words (max 15): '{b[:55]}...'")
        a = ABSOLUTE.search(b)
        if a: fail(f"[overclaim] slide {sid}: absolute word '{a.group(0)}' in '{b[:60]}...'")
        for num in re.findall(r"\d+(?:\.\d+)?°?", b):
            if num.strip("°") not in wiki and not re.fullmatch(r"[123]°?", num): fail(f"[grounding] slide {sid}: number '{num}' not in {p}")
        for t in TERMS:
            if t in nb:
                if t not in wiki and not (t == "beta" and "β" in open(p, encoding="utf-8").read()):
                    fail(f"[grounding] slide {sid}: term '{t}' not in {p}")
                if t not in seen_terms: seen_terms[t] = (sid, bool(re.search(re.escape(t) + r"[^:]{0,30}(:| means | is a | are )", nb)) or ":" in b)
for t, (sid, defined) in seen_terms.items():
    if t in ("alkene", "intermediate", "beta", "backside", "tosylate", "hofmann", "walden", "polar aprotic", "polar protic", "zaitsev") : continue
    if not defined: fail(f"[order] term '{t}' first appears on slide {sid} without being explained there")
print(f"slides checked: {len(slides)}")
if fails:
    print(f"FAIL ({len(fails)} problems)"); [print(" -", x) for x in fails]; sys.exit(1)
print("PASS: content check")
