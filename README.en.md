# ipb-ppta-csl

An **unofficial** [CSL](https://citationstyles.org/) citation style for IPB University's *Pedoman Penyajian Tugas Akhir* (PPTA 2026, Rector's Regulation No. 48 of 2025), Chapter VII on references: the Harvard name-year system after CSE 9th edition. For Zotero and Mendeley.

[Versi bahasa Indonesia](README.md)

> **Status.** Unofficial and not an IPB product. Written from the text of Chapter VII (pp. 67–80) and tested against the examples printed there. Where this style and the guide disagree, the guide is right: please open an issue. If IPB publishes an official PPTA style, use that one.

## Contents

| File | What it is |
|---|---|
| `ipb-ppta.csl` | The style, Indonesian by default |
| `ipb-ppta-en.csl` | The same style in English, for Zotero. See [Using the English version](#using-the-english-version) |
| `tools/` | For maintainers: the test and the script that derives the English file |

The source of this style is *Pedoman Penyajian Tugas Akhir IPB* (Rector's Regulation No. 48 of 2025; IPB Press, first printing, January 2026), Chapter VII, pp. 67–80. In the official PDF, printed page N is PDF page N + 20. The official supplements are at <https://ipb.link/suplemen-ppta>.

## Document templates

- The official PPTA template (Word) and the other supplements are at **<https://ipb.link/suplemen-ppta>** (Google Drive, Google login required). Supplement 1 is the template; Supplements 7–8 cover author names; Supplement 9 lists publisher abbreviations.
- **LaTeX template: work in progress.** It will be added to this repository.

## Installing

### Zotero

1. Download [`ipb-ppta.csl`](ipb-ppta.csl): open the file, click *Raw*, and save it.
2. Zotero 7: **Edit → Settings → Cite → Styles → +**, then pick the file. Zotero 6: Edit → Preferences → Cite → Styles → +.
3. In Word, LibreOffice or Google Docs: **Zotero → Document Preferences**, choose *IPB: Pedoman Penyajian Tugas Akhir 2026 (PPTA, tidak resmi)*.

The style fixes Indonesian as its default language. For English, use `ipb-ppta-en.csl`.

### Mendeley

Mendeley adds a custom style from a URL:

`https://raw.githubusercontent.com/Raphcel/ipb-ppta-csl/main/ipb-ppta.csl`

- **Mendeley Cite (Word):** *Citation Settings → Change citation style → Add a custom style*, paste the URL above, then *Update citation style*.
- **Mendeley Reference Manager:** *Preferences* (Ctrl + ,) → *Formatted Citation Style → Add custom style*, paste the URL, then *Add*; or upload the `.csl` file.

The language follows the style, not Mendeley's language setting: `ipb-ppta.csl` always prints Indonesian. For English, use the same URL with the file name `ipb-ppta-en.csl`. Journal names are abbreviated automatically from Mendeley's own list.

PPTA (p. 67) says an IPB style is built into Mendeley. As of 7 October 2026, the "Institut Pertanian Bogor" style in the public CSL repository, which Mendeley and Zotero both use, is still the PPKI 3rd edition style from 2016: 10 authors, place of publication, "[diunduh …]".

Checked in the code of Mendeley Reference Manager 2.144.0 and Mendeley Cite, with the same citation engine (citeproc-js 1.4.61). Not yet tested by clicking through Word. See also [Entering data in Mendeley](#entering-data-in-mendeley).

## What it produces

In the text: (Syed 2024) or Syed (2024); (Rusmana dan Nedwell 2024); (Aulia *et al.* 2024); (Naim 1984:284); (Sunarti 2005, 2006); (Puspitawati 2009a, 2009b); (IPB 2026); (UU 2023); (Tren ... 2026).

Reference list, from the guide's own examples (Indonesian forms):

- Syed J. 2024. Enhancement of heat transfer using water/graphene nanofluid and the impact of passive techniques—experimental, numerical and ML approaches. *Energies*. 18(1):1–26. doi:10.3390/en18010077.
- Pezzino V, Berbary C, McKinney C, Sangiorgio C, Moriuchi E, *et al.* 2026. Working alliance and subjective engagement with a digital avatar CBT platform. *Behav Sci*. 16(5):1–21. doi:10.3390/bs16050719.
- Rusli S. 2012. *Pengantar Ilmu Kependudukan*. Ed 2. LP3ES.
- Wahyudi AT, Astuti RI, Priyanto JA. 2022. *Metode Eksperimen dalam Genetika Bakteri*. Nugraha B, editor. IPB Press.
- Buchori D, Puspitasari S, Sahari B, Rizali A. 2017. Insect pollinators in decline: conservation challenges in the tropics. Di dalam: Aguirre AA, Sukumar R, editor. *Tropical Conservation: Perspectives on Local and Global Priorities*. Oxford University Press. hlm 290–300.
- Yunindanova MB, Pujiasmanto B, Setyaningrum R. 2015. Kajian agroekologi dan upaya domestikasi sidaguri (*Sida rhombifolia*) di Kabupaten Wonogiri. Di dalam: Maharijaya A, Efendi D, Slamet S, editor. *Prosiding Seminar Nasional Perhimpunan Hortikultura Indonesia*; 2015 Okt 19–20; Bogor, Indonesia. Pusat Kajian Hortikultura Tropika. hlm 37–42.
- Fadillah RA. 2024. Penapisan aktinobakteri yang mempunyai aktivitas antibakteri melalui pendekatan ko-kultur [skripsi]. Bogor: Institut Pertanian Bogor.
- Abdi AP. 2019 Agu 29. Pindah dari Jakarta, bagaimana keamanan ibu kota baru? Tirto.id. Rubrik Politik. [diakses 2019 Sep 1]. https://tirto.id/pindah-dari-jakarta-bagaimana-keamanan-ibu-kota-baru-ehda.
- KMM-IPB. 2015. Prosedur Operasional Baku Penyelenggaraan Program Pendidikan Sarjana Institut Pertanian Bogor. Ed 2. Bogor: KMM-IPB.
- UU Republik Indonesia Nomor 20 Tahun 2023 Tentang Aparatur Sipil Negara. 2023.
- Ramadhan W, Santoso J, Trilaksani W, Rieuwpassa FJ, penemu; Institut Pertanian Bogor. 2025 Mar 10. Proses pembuatan surimi kering beku (tepung surimi) ikan nila dengan penambahan cryoprotectant. Paten Indonesia ID S000010062.

Preprints (arXiv) are not in the guide. The style follows the `[ulasan]`/`[editorial]` pattern of pp. 74–75, with the label taken from the item's *Genre*: Aghajani Asl M, Minaei-Bidgoli B. 2025. FARSIQA: Faithful and advanced RAG system for Islamic question answering [pracetak]. arXiv. [diakses 2026 Okt 1]. https://arxiv.org/abs/2510.25621.

## Entering data in Zotero

The style prints data as stored. These are set in Zotero:

| Item | How |
|---|---|
| Title case | Articles, chapters, theses: sentence case. Books: Title Case, except function words. Type the *Title* field that way. |
| Journal abbreviation | Fill *Journal Abbr* with the ISO abbreviation without periods. Without it, the full name prints. |
| Organization as author | A single-field name holding the acronym: `IPB`, `KMM-IPB`. Spell it out in the body text. |
| Article type | *Extra*: `genre: ulasan` (or `editorial`, `komunikasi singkat`, `catatan penelitian`, `ulas balik`). |
| Thesis | *Type*: `skripsi`, `tesis` or `disertasi` (also `perangkat lunak`, `studi kasus` and the other types on p. 78). Fill *University* and *Place*. |
| No author | *Short Title* holds the in-text form: `Tren ...`, `UU`, `Melepas`. |
| Preprint | Item type *Preprint*, *Repository* `arXiv`, *Genre* `pracetak`. The `[pracetak]` label prints from *Genre*, not from the item type. |
| Conference paper | *Place* is the meeting place. Meeting dates go in *Extra*: `event-date: 2015-10-19/2015-10-20` (works from CSL JSON; untested through Zotero). |
| Patent | Inventors as *Inventor*. *Issuing Authority* = the country (`Indonesia`), *Patent Number* = country code and number (`ID S000010062`), *Issue Date* = the publication date. The holder goes in *Extra*: `publisher: Institut Pertanian Bogor`, because Zotero exports neither its *Assignee* nor its *Country* field. |
| Accepted, not yet in an issue | *Extra*: `status: siap terbit` (or `in press`). |
| Volume with its own title | *Extra*: `volume-title: Pigs, Hippopotamuses, …`. |
| Unknown year | Leave the date empty; the style prints `[tahun terbit tidak diketahui]`. For a web page, the guide asks for the date it was last updated. |
| Unknown publisher | Leave *Publisher* empty; the style prints `[penerbit tidak diketahui]`. |

## Entering data in Mendeley

Mendeley has fewer fields than Zotero, so some forms need another route:

| Item | How |
|---|---|
| Thesis | *Type*: `skripsi`, `tesis` or `disertasi`. *Institution*: the university. Fill *City* and leave *Country* empty, or it prints `Bogor, Indonesia: …`. |
| Conference paper | The proceedings title in *Source*; *City* (and *Country*) = the meeting place; *Publisher*. There is no field for the meeting name or its dates. |
| Document (p. 79) | Type *Generic* with *City* and *Publisher*. The *Report* type has no *Publisher* field. |
| Preprint | Type *Generic* with *Publisher* `arXiv` and the URL, or *Journal Article* with *Journal* `arXiv`. The `[pracetak]` label does not print: Mendeley has no field for it. |
| Article type | No field for it, so `[ulasan]` and the like do not print. |
| Organization as author | The acronym in the *Last name* field. |
| No author | There is no *Short Title*: the in-text citation carries the whole title. Edit the citation in Word. |
| Edition | The bare number: `10`, not `10th`. |
| Journal abbreviation | Automatic. A journal that is not on Mendeley's list prints in full; type its abbreviation into *Journal* if needed. |
| Patent | *Number* = `ID S000010062`, *Country* = `Indonesia`, the holder in *Publisher*. |

Cite theses through Mendeley Cite in Word: *copy formatted citation* in the desktop app does not carry *Type* and *Institution*.

## Decisions where the guide is silent or inconsistent

| Point | In the guide | This style |
|---|---|---|
| Author limit | The rule says 5, then *et al.* (p. 69). Some examples list 7–10 names (pp. 74–75) | 5, then *et al.* |
| Period after *et al.* | The rule says no extra period (p. 69). The example prints `et al..` (p. 73) | `et al. 2026.` |
| Online proceedings | The template reads `halaman artikel. Lokasi (URL)`. The example prints `hlm 167–175; [diakses …]. URL` (p. 78) | `hlm 167–175. [diakses …]. URL.` |
| Place of publication | Gone from books (p. 76), kept in the document and thesis examples (pp. 78–79) | Follows the examples, by item type |
| DOI and URL | The DOI is shown for journal articles only (7.2.1.6); no journal example without a DOI prints a URL | `doi:` on any item that has one. Without a DOI: `[diakses …]. URL`, except for a journal article that has a volume or pages |
| Preprints | No form | `[pracetak]` after the title, from the item's *Genre* |
| Several works in one citation; the same author | Not covered in the PPTA text | Oldest first, joined by `;`; (Sunarti 2005, 2006); (Puspitawati 2009a, 2009b), carried over from PPKI 4th edition |
| English wording | PPTA applies to international classes but gives no English forms | Connecting words follow CSE: "and", "In:", "editors", "accessed", "p", "inventor" |

## Using the English version

One style, two languages. Only the connecting words and month names change; name forms, order and punctuation stay as PPTA prescribes.

| Indonesian | English |
|---|---|
| (Rusmana dan Nedwell 2024) | (Rusmana and Nedwell 2024) |
| Di dalam: Aguirre AA, Sukumar R, editor. | In: Aguirre AA, Sukumar R, editors. |
| Syartinilia, penerjemah. | Syartinilia, translator. |
| [diakses 2026 Mei 12] | [accessed 2026 May 12] |
| hlm 290–300 | p 290–300 |
| …, penemu; … Paten Indonesia ID … | …, inventor; … Patent Indonesia ID … |
| [tahun terbit tidak diketahui] | [date unknown] |
| Agu, Okt, Des, Mei | Aug, Oct, Dec, May |

How to get it:

- **Zotero:** install `ipb-ppta-en.csl` and choose *IPB: Pedoman Penyajian Tugas Akhir 2026 (PPTA, unofficial, English)* in Document Preferences. The file is derived from `ipb-ppta.csl` by `tools/make_en.py`; only the default language, the style name and the style id differ.

Titles, journal names and publisher names print as stored; Indonesian titles are not translated. PPTA gives no English forms of its own, so the English wording is this project's choice, following CSE.

## License and credits

- The `.csl` files: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Developed from the Zotero style "Institut Pertanian Bogor" (PPKI 3rd edition) by Auriza Rahmad Akbar and M. Rachmatarramadhan.
- The PPTA guide: copyright IPB / IPB Press; not included in this repository.
- Made for a final project at IPB with the help of Claude; every form is tested against the guide's examples by `tools/check_ipb_csl.py`.
