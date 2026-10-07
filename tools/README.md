# tools

Untuk pemelihara gaya; pengguna Zotero atau Mendeley tidak memerlukan folder ini.
*For maintainers of the style; Zotero and Mendeley users do not need this folder.*

| Skrip | Kegunaan |
|---|---|
| `check_ipb_csl.py` | Merender contoh-contoh Bab VII PPTA lewat pandoc dan memastikan hasilnya sama dengan pedoman. *Renders the Chapter VII examples through pandoc and asserts the guide's forms.* |
| `make_en.py` | Membuat `ipb-ppta-en.csl` dari `ipb-ppta.csl`. *Derives `ipb-ppta-en.csl` from `ipb-ppta.csl`.* |

```sh
python tools/check_ipb_csl.py      # butuh pandoc 3 di PATH / needs pandoc 3 on PATH
python tools/make_en.py            # setelah mengubah ipb-ppta.csl / after changing ipb-ppta.csl
python tools/make_en.py --check    # apakah ipb-ppta-en.csl sinkron? / is ipb-ppta-en.csl in sync?
```
