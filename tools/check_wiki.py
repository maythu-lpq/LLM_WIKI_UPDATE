#!/usr/bin/env python3
"""N1/N3 wiki check (AGENTS.md sections 3, 6, 9).  Usage: python3 -I tools/check_wiki.py [project_root]
Exit 0 = PASS, 1 = FAIL. Each FAIL line names the rule it breaks."""
import json, os, re, sys, glob
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
fails = []
fail = fails.append
REQUIRED = ["Overview", "Kinetics & Rate Law", "Step-by-Step Mechanism",
            "Stereochemistry", "Controlling Factors", "Related Mechanisms"]
wiki_files = sorted(f for f in glob.glob("wiki/*.md") if os.path.basename(f) not in ("index.md", "sources.md"))
raw_files = sorted(os.path.basename(f) for f in glob.glob("raw/*.pdf"))

for f in wiki_files:                                   # six fixed sections
    heads = re.findall(r"^## (.+?)\s*$", open(f, encoding="utf-8").read(), re.M)
    for sec in REQUIRED:
        if not any(h.startswith(sec) for h in heads): fail(f"[format] {f}: missing section '{sec}'")

for f in glob.glob("wiki/*.md"):                       # links resolve
    for label, target in re.findall(r"\[([^\]]+)\]\(([^)#]+\.md)(?:#[^)]*)?\)", open(f, encoding="utf-8").read()):
        if not target.startswith("http") and not os.path.exists(os.path.join("wiki", target)):
            fail(f"[link] {f}: link to '{target}' does not exist")

idx = open("wiki/index.md", encoding="utf-8").read()   # index lists every note
for f in wiki_files:
    if os.path.basename(f) not in idx: fail(f"[index] wiki/index.md does not link {os.path.basename(f)}")

src = open("wiki/sources.md", encoding="utf-8").read() # source log complete, >= 5
if len(raw_files) < 5: fail(f"[sources] only {len(raw_files)} files in raw/ (need >= 5)")
for r in raw_files:
    if r not in src: fail(f"[sources] raw/{r} is NOT logged in wiki/sources.md")
m = re.search(r"Current Distinct Files in `raw/`:\*\*\s*\*\*(\d+)\*\*", src)
if m and int(m.group(1)) != len(raw_files): fail(f"[sources] sources.md says {m.group(1)} files but raw/ has {len(raw_files)}")
for name in set(re.findall(r"`wiki/([a-z0-9\-]+\.md)`", src)):
    if not os.path.exists("wiki/" + name): fail(f"[sources] sources.md mentions wiki/{name} which does not exist")
for f in wiki_files:
    if os.path.basename(f) not in src: fail(f"[sources] {f} is not listed as fed by any source")
# every raw source must feed at least one existing wiki note (no orphan sources)
for r in raw_files:
    sec = re.split(r"\n### ", src)
    block = next((s for s in sec if r in s.split("\n")[0]), "")
    if not re.search(r"`wiki/[a-z0-9\-]+\.md`", block): fail(f"[sources] raw/{r} feeds no wiki page")

REQ = ["name","category","fullName","molecularity","rateLaw","steps","intermediate","stereochemistry","regiochemistry","rearrangements","substrate"]
mech = json.load(open("data/mechanisms.json", encoding="utf-8"))
if len({tuple(sorted(x.keys())) for x in mech}) != 1: fail("[data] mechanisms.json entries have different field names")
for x in mech:
    for k in REQ:
        if k not in x or str(x[k]).strip() == "": fail(f"[data] mechanisms.json '{x.get('id')}' missing/empty '{k}'")
    for k in ("source", "url"):
        if not os.path.exists(x.get(k, "")): fail(f"[data] mechanisms.json '{x.get('id')}' {k} '{x.get(k)}' not found")

qs = json.load(open("data/questions.json", encoding="utf-8")); cnt = {}
for i, q in enumerate(qs):
    cnt[q["mechanism"]] = cnt.get(q["mechanism"], 0) + 1
    if not (0 <= q["answer"] < len(q["options"])): fail(f"[quiz] question {i} answer index out of range")
    if not os.path.exists(q.get("source", "")): fail(f"[quiz] question {i} source '{q.get('source')}' missing")
for x in mech:
    if cnt.get(x["id"], 0) < 5: fail(f"[quiz] '{x['id']}' has {cnt.get(x['id'],0)} questions (need >= 5)")

print(f"wiki notes: {len(wiki_files)} | raw PDFs: {len(raw_files)} | mechanisms: {len(mech)} | quiz questions: {len(qs)}")
if fails:
    print(f"FAIL ({len(fails)} problems)"); [print(" -", x) for x in fails]; sys.exit(1)
print("PASS: wiki check")
