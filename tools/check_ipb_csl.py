"""Render the PPTA 2026 Bab VII examples through ipb-ppta.csl and assert the guide's forms.

Run it with python from any folder (needs pandoc on PATH).

Fixtures are the guide's own examples (printed pp. 73-80), with initials as printed there.
Where an example contradicts the guide's rule, the rule is asserted and the line says so.
"""
import html
import json
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
# the style sits beside this script (the thesis folder) or one folder up (tools/ in the public repo)
CSL = HERE / "ipb-ppta.csl" if (HERE / "ipb-ppta.csl").exists() else HERE.parent / "ipb-ppta.csl"


def names(*people):
    """'Family|Given' for a person, a bare string for an organization or a one-word name."""
    return [{"family": f, "given": g} if g else {"literal": f} for f, _, g in (p.partition("|") for p in people)]


def date(*parts):
    return {"date-parts": [list(parts)]}


def ref(id, type, **fields):
    return {"id": id, "type": type, **{k.replace("_", "-"): v for k, v in fields.items()}}


REFS = [
    # 7.2.1.8 journal articles (pp. 73-75)
    ref("syed", "article-journal", author=names("Syed|J."), issued=date(2024), container_title="Energies",
        title="Enhancement of heat transfer using water/graphene nanofluid and the impact of passive techniques—experimental, numerical and ML approaches",
        volume="18", issue="1", page="1-26", DOI="10.3390/en18010077"),
    ref("brett", "article-journal", author=names("Brett|D. F."), issued=date(2025), container_title="J Engl Acad Purp",
        title="Titles in archaeology research articles: A corpus-based comparison with other disciplines",
        volume="77", page="1-11", DOI="10.1016/j.jeap.2025.101545"),
    ref("rusmana", "article-journal", author=names("Rusmana|I.", "Nedwell|D. B."), issued=date(2024),
        container_title="HAYATI J Biosci", title="Denitrifier still has the important role in nitrate reduction",
        volume="31", issue="4", page="630-640", DOI="10.4308/hjb.31.4.630-640"),
    ref("aulia", "article-journal", author=names("Aulia|G.", "Rachman|F.", "Untari|F.", "Rasyid|A.", "Hapsari|Y."),
        issued=date(2024), container_title="Journal of Applied Pharmaceutical Science",
        container_title_short="J. Appl. Pharm. Sci.", volume="14", issue="1", page="286-290",
        title="Utilizing the co-culture method to improve the investigation of secondary metabolites of marine bacteria",
        DOI="10.7324/JAPS.2024.136305"),
    # the guide prints five names and "et al."; the sixth here is a stand-in
    ref("pezzino", "article-journal", issued=date(2026), container_title="Behav Sci", volume="16", issue="5", page="1-21",
        author=names("Pezzino|V.", "Berbary|C.", "McKinney|C.", "Sangiorgio|C.", "Moriuchi|E.", "Keenam|X."),
        title="Working alliance and subjective engagement with a digital avatar CBT platform", DOI="10.3390/bs16050719"),
    ref("hunter", "article-journal", author=names("Hunter|J.", "Duff|G."), issued=date(2016), container_title="Science",
        title="GM crops—lessons from medicine", genre="editorial", volume="353", issue="6305", page="1187",
        DOI="10.1126/science.aaj1764"),
    ref("tren", "article-journal", issued=date(2026), container_title="Food Rev Indones", volume="1", issue="1",
        page="19-21", title="Tren kemasan praktis & inovatif", title_short="Tren ...",
        URL="https://example.org/tren", accessed=date(2026, 10, 7)),
    # 7.2.2 books and chapters (pp. 75-77)
    ref("rusli", "book", author=names("Rusli|S."), issued=date(2012), title="Pengantar Ilmu Kependudukan",
        edition="2", publisher="LP3ES", publisher_place="Jakarta"),
    ref("wahyudi", "book", author=names("Wahyudi|A. T.", "Astuti|R. I.", "Priyanto|J. A."), issued=date(2022),
        title="Metode Eksperimen dalam Genetika Bakteri", editor=names("Nugraha|B."), publisher="IPB Press"),
    ref("ipb", "book", author=names("IPB"), issued=date(2026), title="Pedoman Penyajian Tugas Akhir", publisher="IPB Press"),
    ref("higuchi", "book", author=names("Higuchi|H."), issued=date(2016), translator=names("Syartinilia"),
        title="Rekam Jejak Perjalanan Migrasi Burung Menggunakan Teknologi Satellite-Tracking", publisher="IPB Press"),
    ref("buchori", "chapter", author=names("Buchori|D.", "Puspitasari|S.", "Sahari|B.", "Rizali|A."), issued=date(2017),
        title="Insect pollinators in decline: conservation challenges in the tropics",
        editor=names("Aguirre|A. A.", "Sukumar|R."), page="290-300", publisher="Oxford University Press",
        container_title="Tropical Conservation: Perspectives on Local and Global Priorities",
        publisher_place="New York", event_place="New York"),
    # 7.2.3 proceedings (p. 78)
    ref("yunindanova", "paper-conference", author=names("Yunindanova|M. B.", "Pujiasmanto|B.", "Setyaningrum|R."),
        issued=date(2015), title="Kajian agroekologi dan upaya domestikasi sidaguri di Kabupaten Wonogiri",
        editor=names("Maharijaya|A.", "Efendi|D.", "Slamet|S."), page="37-42",
        container_title="Prosiding Seminar Nasional Perhimpunan Hortikultura Indonesia",
        event_date={"date-parts": [[2015, 10, 19], [2015, 10, 20]]}, event_place="Bogor, Indonesia",
        publisher="Pusat Kajian Hortikultura Tropika"),
    ref("mirsam", "paper-conference", author=names("Mirsam|H.", "Rosya|A.", "Rahim|Y. F.", "Rusae|A.", "Munif|A."),
        issued=date(2015), title="Eksplorasi cendawan antagonis dari tanaman kirinyuh", page="167-175",
        container_title="Prosiding Seminar Nasional Perlindungan Tanaman II", event_date=date(2014, 11, 13),
        event_place="Bogor, Indonesia", publisher="Pusat Kajian Pengendalian Hama Terpadu", accessed=date(2026, 5, 12),
        URL="https://repository.ipb.ac.id/bitstream/123456789/75901/1/PROS2015_ABM4.pdf"),
    # 7.2.4 theses (p. 78): one form for print and electronic, so the URL must not print
    ref("fadillah", "thesis", author=names("Fadillah|R. A."), issued=date(2024), genre="skripsi",
        title="Penapisan aktinobakteri yang mempunyai aktivitas antibakteri melalui pendekatan ko-kultur",
        publisher="Institut Pertanian Bogor", publisher_place="Bogor", URL="https://repository.ipb.ac.id/x"),
    # 7.2.5 others (pp. 79-80)
    ref("abdi", "article-newspaper", author=names("Abdi|A. P."), issued=date(2019, 8, 29), container_title="Tirto.id",
        title="Pindah dari Jakarta, bagaimana keamanan ibu kota baru?", section="Rubrik Politik", accessed=date(2019, 9, 1),
        URL="https://tirto.id/pindah-dari-jakarta-bagaimana-keamanan-ibu-kota-baru-ehda"),
    ref("slamet", "article-newspaper", author=names("Slamet|A. S."), issued=date(2026, 5, 12), page="9",
        title="Kampus di jantung hilirisasi", container_title="Media Indonesia", section="Rubrik Opini"),
    ref("kmm", "report", author=names("KMM-IPB"), issued=date(2015), edition="2", publisher="KMM-IPB",
        title="Prosedur Operasional Baku Penyelenggaraan Program Pendidikan Sarjana Institut Pertanian Bogor",
        publisher_place="Bogor"),
    ref("uu", "legislation", issued=date(2023), title_short="UU",
        title="UU Republik Indonesia Nomor 20 Tahun 2023 Tentang Aparatur Sipil Negara"),
    # not in the PPTA text. Preprint: this project's form, with the label taken from the item's genre.
    # Same author and year: carried over from PPKI 4.
    ref("farsiqa", "article", author=names("Aghajani Asl|M.", "Minaei-Bidgoli|B."), issued=date(2025, 10, 29),
        title="FARSIQA: Faithful and advanced RAG system for Islamic question answering", publisher="arXiv", genre="pracetak",
        accessed=date(2026, 10, 1), URL="https://arxiv.org/abs/2510.25621"),
    ref("puspa", "article-journal", author=names("Puspitawati|H."), issued=date(2009), title="Alpha",
        container_title="Hayati", volume="1"),
    ref("puspb", "article-journal", author=names("Puspitawati|H."), issued=date(2009), title="Beta",
        container_title="Hayati", volume="2"),
    # shapes the guide describes without a full example: no year (7.2.1.2d, p. 71); a meeting name with no book title (7.2.3.1)
    ref("nodate", "book", author=names("Permi"), title="Buku Tanpa Tahun", publisher="Permi"),
    ref("event", "paper-conference", author=names("Rahayu|G."), issued=date(2010), page="9", publisher="Permi Cabang Bogor",
        title="Microbial aspects of agarwood production in Indonesia", event_place="Bogor, Indonesia",
        event="International Seminar of Indonesian Society for Microbiology"),
    ref("rahayu", "paper-conference", author=names("Rahayu|G."), issued=date(2011), page="9", publisher="Permi Cabang Bogor",
        title="Microbial aspects of agarwood production", container_title="Book of Abstracts",
        event="International Seminar of Indonesian Society for Microbiology", publisher_place="Bogor, Indonesia",
        event_date={"date-parts": [[2010, 10, 4], [2010, 10, 7]]}),
    # 7.2.2.1 (p. 76): no publisher. 7.2.1.2 (p. 71): a journal without volume and issue takes the month and day;
    # with no pages either, the URL is all there is to find it by, so it prints
    ref("nopub", "book", author=names("Rusli|S."), issued=date(2013), title="Buku Tanpa Penerbit"),
    ref("greule", "article-journal", author=names("Greule|M."), issued=date(2025, 8, 21), container_title="J Agric Food Chem",
        title="An article not yet in a volume", URL="https://example.org/x", accessed=date(2026, 10, 7)),
    # 7.2.1.1 (p. 69): particles stay in front, hyphenated given names lose the hyphen, "Jr" follows the initials
    ref("korn", "article-journal", issued=date(2020), title="Names", container_title="Nature", volume="1", page="1",
        author=[{"family": "Korn", "given": "K. H.", "non-dropping-particle": "van der"},
                {"family": "Lagrot", "given": "Jean-Louis"}, {"family": "DeVita", "given": "Vincent T.", "suffix": "Jr"}]),
    # not in the guide: the usual shape of this project's proceedings entries (ACL Anthology through Zotero)
    ref("ma", "paper-conference", author=names("Ma|X.", "Gong|Y.", "He|P.", "Zhao|H.", "Duan|N."), issued=date(2023),
        title="Query rewriting in retrieval-augmented large language models", page="5303-5315",
        container_title="Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
        event_title="EMNLP 2023", event_place="Singapore", publisher_place="Singapore",
        publisher="Association for Computational Linguistics", DOI="10.18653/v1/2023.emnlp-main.322",
        URL="https://aclanthology.org/2023.emnlp-main.322", accessed=date(2026, 10, 1)),
    # p. 75: accepted article without volume and pages; p. 77: a volume with its own title (the guide lists all 6 editors; the rule says 5)
    ref("resmeiliana", "article-journal", author=names("Resmeiliana|I."), issued=date(2025), container_title="Chem Biodivers",
        title="Phytochemicals and antibacterial activity of leaf and twig of three Fabaceae species", status="siap terbit"),
    # the same with a full date in the data: p. 75 prints the bare year
    ref("resmeiliana2", "article-journal", author=names("Achmadi|S. S."), issued=date(2025, 3, 5), status="siap terbit",
        container_title="Chem Biodivers", title="A second accepted article"),
    ref("kingdon", "book", editor=names("Kingdon|J.", "Happold|D.", "Butynski|T.", "Hoffmann|M.", "Happold|M.", "Kalina|J."),
        issued=date(2013), title="Mammals of Africa", volume="6", publisher="Bloomsbury Publishing",
        volume_title="Pigs, Hippopotamuses, Chevrotain, Giraffes, Deer and Bovids"),
    # 7.2.5a patent (p. 79): inventors, "penemu", the holder as publisher; the country in authority (Zotero: Issuing Authority)
    ref("ramadhan", "patent", author=names("Ramadhan|W.", "Santoso|J.", "Trilaksani|W.", "Rieuwpassa|F. J."), issued=date(2025, 3, 10),
        title="Proses pembuatan surimi kering beku (tepung surimi) ikan nila dengan penambahan cryoprotectant",
        publisher="Institut Pertanian Bogor", authority="Indonesia", number="ID S000010062"),
    # records as Mendeley hands them over (Reference Manager 2.144 and Mendeley Cite, read 2026-10-07): a Generic document
    # arrives as "article" with no genre, an organization as a family name, a patent's Country as publisher-place
    ref("bsn", "article", author=[{"family": "BSN", "given": "", "parse-names": False}], issued=date(2020),
        title="Dokumen dari Mendeley", publisher="BSN", publisher_place="Jakarta"),
    ref("patenm", "patent", author=[{"family": "Santoso", "given": "J.", "parse-names": False}], issued=date(2025, 3, 10),
        title="Paten dari Mendeley", publisher="Institut Pertanian Bogor", publisher_place="Indonesia", number="ID S000010063"),
]

CITES = "[@syed] [@rusmana] [@aulia] [@pezzino] [@brett; @syed; @fadillah] [@syed, 284] [@syed, bab 3] [@puspa; @puspb] [@tren] [@uu] @rusmana."

# language -> substrings the rendered text must contain
EXPECTED = {
    "id-ID": [
        # in the text (7.1, and "Bentuk acuan" under each example)
        "(Syed 2024)", "(Rusmana dan Nedwell 2024)", "Rusmana dan Nedwell (2024)", "(Aulia et al. 2024)",
        "(Pezzino et al. 2026)", "(Syed 2024:284)", "(Syed 2024, bab 3)", "(Tren ... 2026)", "(UU 2023)",
        "(Fadillah 2024; Syed 2024; Brett 2025)", "(Puspitawati 2009a, 2009b)",
        # Daftar Pustaka
        "Syed J. 2024. Enhancement of heat transfer using water/graphene nanofluid and the impact of passive techniques—experimental, numerical and ML approaches. Energies. 18(1):1–26. doi:10.3390/en18010077.",
        "comparison with other disciplines. J Engl Acad Purp. 77:1–11. doi:10.1016/j.jeap.2025.101545.",
        "Rusmana I, Nedwell DB. 2024. Denitrifier",
        "Aulia G, Rachman F, Untari F, Rasyid A, Hapsari Y. 2024. Utilizing",
        "marine bacteria. J Appl Pharm Sci. 14(1):286–290. doi:10.7324/JAPS.2024.136305.",
        # rule (7.2.1.1): no extra period after "et al."; the guide's example prints "et al.."
        "Pezzino V, Berbary C, McKinney C, Sangiorgio C, Moriuchi E, et al. 2026. Working",
        "Hunter J, Duff G. 2016. GM crops—lessons from medicine [editorial]. Science. 353(6305):1187. doi:10.1126/science.aaj1764.",
        "Tren kemasan praktis & inovatif. 2026. Food Rev Indones. 1(1):19–21.\n",
        "Rusli S. 2012. Pengantar Ilmu Kependudukan. Ed 2. LP3ES.",
        "Wahyudi AT, Astuti RI, Priyanto JA. 2022. Metode Eksperimen dalam Genetika Bakteri. Nugraha B, editor. IPB Press.",
        "IPB. 2026. Pedoman Penyajian Tugas Akhir. IPB Press.",
        "Teknologi Satellite-Tracking. Syartinilia, penerjemah. IPB Press.",
        "Buchori D, Puspitasari S, Sahari B, Rizali A. 2017. Insect pollinators in decline: conservation challenges in the tropics. Di dalam: Aguirre AA, Sukumar R, editor. Tropical Conservation: Perspectives on Local and Global Priorities. Oxford University Press. hlm 290–300.",
        "Di dalam: Maharijaya A, Efendi D, Slamet S, editor. Prosiding Seminar Nasional Perhimpunan Hortikultura Indonesia; 2015 Okt 19–20; Bogor, Indonesia. Pusat Kajian Hortikultura Tropika. hlm 37–42.",
        # the guide's template has "halaman artikel. Lokasi (URL)"; its example prints "hlm 167-175; [diakses ...]"
        "Tanaman II; 2014 Nov 13; Bogor, Indonesia. Pusat Kajian Pengendalian Hama Terpadu. hlm 167–175. [diakses 2026 Mei 12]. https://repository.ipb.ac.id/bitstream/123456789/75901/1/PROS2015_ABM4.pdf.",
        "melalui pendekatan ko-kultur [skripsi]. Bogor: Institut Pertanian Bogor.\n",
        # the guide prints "baru?. Tirto.id" (p. 79); the processor drops the period after a question mark
        "Abdi AP. 2019 Agu 29. Pindah dari Jakarta, bagaimana keamanan ibu kota baru? Tirto.id. Rubrik Politik. [diakses 2019 Sep 1]. https://tirto.id/pindah-dari-jakarta-bagaimana-keamanan-ibu-kota-baru-ehda.",
        "Slamet AS. 2026 Mei 12. Kampus di jantung hilirisasi. Media Indonesia. Rubrik Opini: 9.",
        "KMM-IPB. 2015. Prosedur Operasional Baku Penyelenggaraan Program Pendidikan Sarjana Institut Pertanian Bogor. Ed 2. Bogor: KMM-IPB.",
        "UU Republik Indonesia Nomor 20 Tahun 2023 Tentang Aparatur Sipil Negara. 2023.",
        "Aghajani Asl M, Minaei-Bidgoli B. 2025. FARSIQA: Faithful and advanced RAG system for Islamic question answering [pracetak]. arXiv. [diakses 2026 Okt 1]. https://arxiv.org/abs/2510.25621.",
        "Puspitawati H. 2009a. Alpha.", "Puspitawati H. 2009b. Beta.",
        "(Permi [tahun terbit tidak diketahui])", "Permi. [tahun terbit tidak diketahui]. Buku Tanpa Tahun. Permi.",
        "Di dalam: International Seminar of Indonesian Society for Microbiology; Bogor, Indonesia. Permi Cabang Bogor. hlm 9.",
        "Resmeiliana I. 2025. Phytochemicals and antibacterial activity of leaf and twig of three Fabaceae species. Chem Biodivers., siap terbit.",
        "(Ramadhan et al. 2025)", "Ramadhan W, Santoso J, Trilaksani W, Rieuwpassa FJ, penemu; Institut Pertanian Bogor. 2025 Mar 10. Proses pembuatan surimi kering beku (tepung surimi) ikan nila dengan penambahan cryoprotectant. Paten Indonesia ID S000010062.",
        "(Kingdon et al. 2013)", "Happold M, et al., editor. 2013. Mammals of Africa. Vol 6: Pigs, Hippopotamuses, Chevrotain, Giraffes, Deer and Bovids. Bloomsbury Publishing.",
        "Achmadi SS. 2025. A second accepted article. Chem Biodivers., siap terbit.",
        "Di dalam: Book of Abstracts. International Seminar of Indonesian Society for Microbiology; 2010 Okt 4–7; Bogor, Indonesia. Permi Cabang Bogor. hlm 9.",
        "Rusli S. 2013. Buku Tanpa Penerbit. [penerbit tidak diketahui].",
        "Greule M. 2025 Agu 21. An article not yet in a volume. J Agric Food Chem. [diakses 2026 Okt 7]. https://example.org/x.",
        "BSN. 2020. Dokumen dari Mendeley. Jakarta: BSN.\n",
        "Santoso J, penemu; Institut Pertanian Bogor. 2025 Mar 10. Paten dari Mendeley. Paten Indonesia ID S000010063.",
        "van der Korn KH, Lagrot JL, DeVita VT Jr. 2020. Names. Nature. 1:1.",
        "Di dalam: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. EMNLP 2023; Singapore. Association for Computational Linguistics. hlm 5303–5315. doi:10.18653/v1/2023.emnlp-main.322.\n",
    ],
    "en-US": [
        "(Rusmana and Nedwell 2024)", "Rusmana and Nedwell (2024)", "(Syed 2024:284)",
        "In: Aguirre AA, Sukumar R, editors. Tropical Conservation: Perspectives on Local and Global Priorities. Oxford University Press. p 290–300.",
        "; 2015 Oct 19–20; Bogor, Indonesia.", "Syartinilia, translator. IPB Press.", "[accessed 2026 May 12]. https://",
        "question answering [pracetak]. arXiv. [accessed 2026 Oct 1].", "Buku Tanpa Penerbit. [publisher unknown].",
        "Rieuwpassa FJ, inventor; Institut Pertanian Bogor. 2025 Mar 10.", "Patent Indonesia ID S000010062.",
    ],
}
# italics (pp. 72-77): journal names, book and volume titles, "et al."
EXPECTED_HTML = ["<em>Energies</em>. 18(1):1–26", "<em>Pengantar Ilmu Kependudukan</em>. Ed 2.", "(Aulia <em>et al.</em> 2024)",
                 "Moriuchi E, <em>et al.</em> 2026.", "editor. <em>Tropical Conservation: Perspectives on Local and Global Priorities</em>.",
                 "<em>Mammals of Africa</em>. Vol 6: <em>Pigs, Hippopotamuses, Chevrotain, Giraffes, Deer and Bovids</em>."]
# 7.2: the list is alphabetical by first author; these openings must appear in this order
ORDER = ["Abdi AP. 2019", "Aulia G,", "Brett DF.", "IPB. 2026", "Rusli S. 2012", "Syed J. 2024", "van der Korn KH", "Wahyudi AT"]

with tempfile.TemporaryDirectory() as tmp:
    bib = pathlib.Path(tmp, "refs.json")
    bib.write_text(json.dumps(REFS), encoding="utf-8")
    text = CITES + " " + " ".join(f"[@{r['id']}]" for r in REFS)
    for lang, expected in EXPECTED.items():
        run = subprocess.run(
            ["pandoc", "--citeproc", f"--bibliography={bib}", f"--csl={CSL}", "-M", f"lang={lang}", "-t", "html", "--wrap=none"],
            input=text, capture_output=True, text=True, encoding="utf-8")
        if run.returncode or run.stderr:  # a broken style, or a warning such as "citation not found"
            sys.exit(f"{lang}: pandoc said:\n{run.stderr}")
        out = html.unescape(run.stdout)
        plain = html.unescape(re.sub(r"<[^>]+>", "", run.stdout))
        missing = [e for e in expected if e not in plain]
        if lang == "id-ID":
            missing += [e for e in EXPECTED_HTML if e not in out]
            at = [plain.find(o) for o in ORDER]
            if -1 in at or at != sorted(at):
                missing.append(f"list order {ORDER}")
        if missing:  # sys.exit, not assert: python -O must not turn the check off
            sys.exit(f"{lang}: missing {missing}\n--- output ---\n{plain}")
        print(f"{lang}: ok ({len(expected)} forms)")
