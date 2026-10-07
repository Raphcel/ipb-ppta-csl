"""Derive ipb-ppta-en.csl (English as the default language) from ipb-ppta.csl.

Run it after every change to ipb-ppta.csl. `--check` only reports whether the English file is in sync.
Only the default locale, the style name and the style id differ; the macros are shared.
"""
import pathlib
import sys

SRC = pathlib.Path(__file__).resolve().parent.parent / "ipb-ppta.csl"  # the repo root
DST = SRC.with_name("ipb-ppta-en.csl")
EDITS = [
    ('default-locale="id-ID"', 'default-locale="en-US"'),
    ("<title>IPB: Pedoman Penyajian Tugas Akhir 2026 (PPTA, tidak resmi)</title>",
     "<title>IPB: Pedoman Penyajian Tugas Akhir 2026 (PPTA, unofficial, English)</title>"),
    ("<title-short>IPB PPTA 2026</title-short>", "<title-short>IPB PPTA 2026 (EN)</title-short>"),
    ("<id>http://www.zotero.org/styles/ipb-ppta-2026-unofficial</id>",
     "<id>http://www.zotero.org/styles/ipb-ppta-2026-en-unofficial</id>"),
]

text = SRC.read_text(encoding="utf-8")
for old, new in EDITS:
    assert text.count(old) == 1, f"ipb-ppta.csl: expected exactly one {old!r}"
    text = text.replace(old, new)

if "--check" in sys.argv:
    if not DST.exists() or DST.read_text(encoding="utf-8") != text:
        sys.exit(f"{DST.name} is out of date: run python tools/make_en.py")
    print(f"{DST.name}: in sync")
else:
    DST.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {DST.name}")
