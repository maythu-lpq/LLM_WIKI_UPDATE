# Organic Chemistry Reaction Mechanism LLM Wiki

A small LLM Wiki about SN1, SN2, E1 and E2, plus a teaching slide deck made only from that wiki.

## Folders
- `raw/` original textbook PDFs (never edited by the AI). 5 files.
- `wiki/` notes written from `raw/`: `sn1`, `sn2`, `e1`, `e2`, `alcohols`, `alkenes`, `alkynes`, `index`, `sources`.
- `slides/` teaching deck: `outline.md` -> `content.json` -> `index.html`.
- `pages/`, `index.html`, `assets/`, `data/` the study website (mechanism pages, predictor, quiz, compare, chatbot).
- `tools/` check scripts. `logs/` run logs and raw check output.
- `AGENTS.md` the rules the AI follows (naming, wiki format, ingest, slide graph N1-N8, lessons learned).

## Add a new source
1. Put the PDF in `raw/`.
2. Ask the AI to summarize it and propose wiki pages. Approve. Then it writes the notes (AGENTS.md section 9).
3. Run `python3 -I tools/check_wiki.py`.

## Check everything
```
python3 -I tools/check_wiki.py     # wiki and sources
python3 -I tools/check_slides.py   # slide content before HTML
python3 -I tools/build_slides.py   # content.json -> slides/index.html
python3 -I tools/check_site.py     # real browser test (needs: pip install playwright && playwright install chromium)
```

No API keys or personal data are stored in this repository.
