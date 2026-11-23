#!/usr/bin/env python3
"""N8 final check: opens every page in a real headless browser over http:// (not file:///).
Usage: python3 -I tools/check_site.py [project_root]   (needs: pip install playwright; playwright install chromium)
Checks: console errors, 404s, 'undefined'/'NaN' text, horizontal overflow (desktop + phone),
broken links, slide deck walk-through (HTML == content.json), compare tool (all pairs),
predictor (all combinations), quiz (all filters), chatbot (grounded answers + honest miss)."""
import glob, itertools, json, os, re, subprocess, sys, time
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
from playwright.sync_api import sync_playwright
PORT = 8765; BASE = f"http://127.0.0.1:{PORT}/"
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=ROOT)
time.sleep(1.0)
fails, stats = [], {}; fail = fails.append
BAD = re.compile(r"undefined|\bNaN\b|\[object Object\]", re.I)
def new_page(browser, w=1280, h=800):
    page = browser.new_context(viewport={"width": w, "height": h}).new_page(); page.problems = []
    page.on("console", lambda m: page.problems.append(f"console error: {m.text}") if m.type == "error" else None)
    page.on("pageerror", lambda e: page.problems.append(f"pageerror: {e}"))
    page.on("response", lambda r: page.problems.append(f"HTTP {r.status}: {r.url}") if r.status >= 400 else None)
    return page
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        pages = ["index.html"] + sorted(glob.glob("pages/*.html")) + ["slides/index.html"]
        for p in pages:
            for (w, h) in ((1280, 800), (390, 800)):
                pg = new_page(browser, w, h); pg.goto(BASE + p); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(300)
                m = BAD.search(pg.inner_text("body"))
                if m: fail(f"[text] {p} @{w}px shows '{m.group(0)}'")
                if pg.evaluate("document.documentElement.scrollWidth") > w + 2: fail(f"[overflow] {p} @{w}px has horizontal overflow")
                for pr in pg.problems: fail(f"[load] {p} @{w}px {pr}")
                if not pg.title().strip() or "<" in pg.title(): fail(f"[title] {p}: bad <title> '{pg.title()}'")
                for href in pg.eval_on_selector_all("a[href]", "els=>els.map(e=>e.getAttribute('href'))"):
                    if href.startswith(("http", "#", "mailto")): continue
                    t = os.path.normpath(os.path.join(os.path.dirname(p), href.split('#')[0]))
                    if href.split('#')[0] and not os.path.exists(t): fail(f"[link] {p}: broken link '{href}'")
                pg.context.close()
        stats["pages"] = len(pages)

        slides = json.load(open("slides/content.json", encoding="utf-8"))
        pg = new_page(browser); pg.goto(BASE + "slides/index.html"); pg.wait_for_load_state("networkidle")
        for i, s in enumerate(slides):
            if f"Slide {i+1} / {len(slides)}" not in pg.inner_text("#slide-counter"): fail(f"[slides] counter wrong at slide {i+1}")
            n = pg.locator("#slide-bullets li").count()
            if n != len(s["bullets"]): fail(f"[slides] slide {i+1}: HTML shows {n} bullets, content.json has {len(s['bullets'])} (out of sync)")
            if not pg.inner_text("#slide-title").strip(): fail(f"[slides] slide {i+1}: empty title")
            if pg.evaluate("(()=>{const c=document.getElementById('slide-card');return c.scrollHeight>c.clientHeight+2})()"): fail(f"[overflow] slide {i+1}: text overflows card")
            if s["source"] not in pg.inner_text("#slide-source-text"): fail(f"[slides] slide {i+1}: source '{s['source']}' not shown")
            if i < len(slides) - 1: pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(60)
        stats["slides_walked"] = len(slides)
        for pr in pg.problems: fail(f"[slides] {pr}")
        pg.context.close()

        pg = new_page(browser); pg.goto(BASE + "pages/compare.html"); pg.wait_for_load_state("networkidle")
        opts = pg.eval_on_selector_all("#mech-1-select option", "els=>els.map(e=>e.value)"); n = 0
        for a, b in itertools.product(opts, opts):
            pg.select_option("#mech-1-select", a); pg.select_option("#mech-2-select", b); pg.wait_for_timeout(40)
            m = BAD.search(pg.inner_text("#comparison-output"))
            if m: fail(f"[compare] {a} vs {b} shows '{m.group(0)}'")
            n += 1
        stats["compare_pairs"] = n; pg.context.close()

        pg = new_page(browser); pg.goto(BASE + "pages/predictor.html"); pg.wait_for_load_state("networkidle")
        ids = ["#substrate-select", "#reagent-select", "#solvent-select", "#temp-select"]
        vals = [pg.eval_on_selector_all(f"{i} option", "els=>els.map(e=>e.value)") for i in ids]; n = 0
        for combo in itertools.product(*vals):
            for i, v in zip(ids, combo): pg.select_option(i, v)
            pg.wait_for_timeout(15); m = BAD.search(pg.inner_text("#prediction-result"))
            if m: fail(f"[predictor] {combo} shows '{m.group(0)}'")
            n += 1
        stats["predictor_combos"] = n
        for pr in pg.problems: fail(f"[predictor] {pr}")
        pg.context.close()

        pg = new_page(browser); pg.goto(BASE + "pages/quiz.html"); pg.wait_for_load_state("networkidle"); mx = 0
        for btn in pg.locator(".filter-btn").all():
            btn.click(); pg.wait_for_timeout(80); c = pg.locator(".quiz-card").count(); mx = max(mx, c)
            m = re.search(r"\((\d+)\)", btn.inner_text())
            if c == 0 or (m and int(m.group(1)) != c): fail(f"[quiz] button '{btn.inner_text().strip()}' but {c} cards shown")
        stats["quiz_max_cards"] = mx
        for pr in pg.problems: fail(f"[quiz] {pr}")
        pg.context.close()

        qa = json.load(open("tools/chat_tests.json", encoding="utf-8")) if os.path.exists("tools/chat_tests.json") else [{"q": "Why does SN1 cause racemization?", "expect": "sn1.md"}]
        pg = new_page(browser); pg.goto(BASE + "pages/chat.html"); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(1500)
        for t in qa:
            pg.fill("#chat-input", t["q"]); pg.press("#chat-input", "Enter"); pg.wait_for_timeout(1000)
            last = pg.locator("#chat-messages > *").last.inner_text()
            if BAD.search(last): fail(f"[chat] '{t['q']}' shows undefined")
            if t["expect"].lower() not in last.lower(): fail(f"[chat] '{t['q']}' -> last answer does not contain '{t['expect']}' (got: {last[:90]!r})")
        stats["chat_questions"] = len(qa)
        for pr in pg.problems: fail(f"[chat] {pr}")
        browser.close()
finally:
    srv.terminate()
print("stats:", stats)
if fails:
    print(f"FAIL ({len(fails)} problems)")
    for x in fails[:60]: print(" -", x)
    sys.exit(1)
print("PASS: site check")
