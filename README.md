# ipb-ppta-csl

Gaya sitasi [CSL](https://citationstyles.org/) **tidak resmi** untuk *Pedoman Penyajian Tugas Akhir IPB* (PPTA 2026, Peraturan Rektor IPB Nomor 48 Tahun 2025), Bab VII Kepustakaan: sistem Harvard (nama-tahun) mengikuti CSE edisi ke-9. Dipakai di Zotero dan pandoc.

[English version of this README](README.en.md)

> **Status.** Tidak resmi dan bukan produk IPB. Ditulis dari teks Bab VII (hlm. 67–80) dan diuji terhadap contoh-contoh di dalamnya. Jika hasil gaya ini berbeda dengan pedoman, pedoman yang benar: laporkan lewat *Issues*. Jika IPB menerbitkan CSL resmi untuk PPTA, pakailah yang resmi.

## Isi repositori

| Berkas | Keterangan |
|---|---|
| `ipb-ppta.csl` | Gaya sitasi, bahasa Indonesia sebagai bawaan |
| `ipb-ppta-en.csl` | Gaya yang sama dengan bahasa Inggris sebagai bawaan, untuk Zotero. Lihat [Versi bahasa Inggris](#versi-bahasa-inggris) |
| `check_ipb_csl.py` | Pengujian: merender contoh-contoh Bab VII lewat pandoc dan memastikan hasilnya sama dengan pedoman |
| `make_en.py` | Membuat `ipb-ppta-en.csl` dari `ipb-ppta.csl` |

Pedomannya sendiri tidak disertakan: hak ciptanya milik IPB dan dilarang diperbanyak tanpa izin tertulis. Acuan gaya ini: *Pedoman Penyajian Tugas Akhir IPB* (Peraturan Rektor IPB Nomor 48 Tahun 2025; IPB Press, cetakan 1, Januari 2026), Bab VII, hlm. 67–80. Pada berkas PDF resminya, halaman cetak N ada di halaman PDF N + 20. Suplemen resminya ada di <https://ipb.link/suplemen-ppta>.

## Templat dokumen

- Templat resmi PPTA (Word) dan suplemen lainnya: **<https://ipb.link/suplemen-ppta>** (Google Drive, perlu masuk dengan akun Google). Suplemen 1 adalah templat; Suplemen 7–8 memuat penulisan nama penulis; Suplemen 9 daftar singkatan nama penerbit.
- **Templat LaTeX: sedang dikerjakan.** Akan ditambahkan ke repositori ini.

## Pemasangan

### Zotero

1. Unduh [`ipb-ppta.csl`](ipb-ppta.csl): buka berkasnya, klik *Raw*, lalu simpan.
2. Zotero 7: **Edit → Settings → Cite → Styles → +**, pilih berkas itu. Zotero 6: Edit → Preferences → Cite → Styles → +.
3. Di Word, LibreOffice, atau Google Docs: **Zotero → Document Preferences**, pilih *IPB: Pedoman Penyajian Tugas Akhir 2026 (PPTA, tidak resmi)*.

Gaya ini menetapkan bahasa Indonesia sebagai bawaan, sehingga pilihan *Language* di Zotero tidak aktif. Untuk bahasa Inggris pasang `ipb-ppta-en.csl`.

### pandoc

```sh
pandoc naskah.md --citeproc --bibliography=pustaka.json --csl=ipb-ppta.csl -M lang=id-ID -o naskah.docx
```

Satu berkas untuk dua bahasa: `-M lang=en-US` menghasilkan versi Inggris dari berkas yang sama. Rujukan halaman ditulis `[@kunci, 284]` dan dirender `(Naim 1984:284)`; rujukan selain halaman, misalnya `[@kunci, bab 3]`, dirender `(Naim 1984, bab 3)`. Ekspor pustaka dari Zotero sebagai **CSL JSON**, bukan BibTeX, agar jenis *Preprint* dan isian *Extra* ikut terbawa.

### Mendeley

PPTA (hlm. 67) menyebut CSL IPB terpasang di Mendeley. Per 7 Oktober 2026, gaya "Institut Pertanian Bogor" di repositori CSL publik, yang dipakai Mendeley dan Zotero, masih versi PPKI Edisi ke-3 (2016): 10 penulis, tempat terbit, "[diunduh …]". Jika versi Mendeley Anda bisa menambah gaya dari URL, pakai
`https://raw.githubusercontent.com/Raphcel/ipb-ppta-csl/main/ipb-ppta.csl`.

## Bentuk yang dihasilkan

Dalam teks: (Syed 2024) atau Syed (2024); (Rusmana dan Nedwell 2024); (Aulia *et al.* 2024); (Naim 1984:284); (Sunarti 2005, 2006); (Puspitawati 2009a, 2009b); (IPB 2026); (UU 2023); (Tren ... 2026).

Daftar pustaka, dari contoh-contoh pedoman:

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

Pracetak (arXiv) tidak ada di pedoman. Gaya ini memakai pola `[ulasan]`/`[editorial]` dari hlm. 74–75: Aghajani Asl M, Minaei-Bidgoli B. 2025. FARSIQA: Faithful and advanced RAG system for Islamic question answering [pracetak]. arXiv. [diakses 2026 Okt 1]. https://arxiv.org/abs/2510.25621.

## Mengisi data di Zotero

Gaya mencetak data apa adanya. Hal-hal berikut diatur di Zotero:

| Hal | Cara |
|---|---|
| Huruf kapital judul | Artikel, bab, skripsi: kapital hanya di awal judul dan pada nama diri. Buku: kapital di awal setiap kata kecuali kata tugas. Tulis begitu di kolom *Title*. |
| Singkatan nama jurnal | Isi *Journal Abbr* dengan singkatan ISO tanpa titik. Tanpa isian itu, nama lengkap yang dicetak. |
| Organisasi sebagai penulis | Nama satu bidang (*single field*) berisi akronimnya: `IPB`, `KMM-IPB`. Kepanjangannya ditulis di badan teks. |
| Jenis artikel | *Extra*: `genre: ulasan` (atau `editorial`, `komunikasi singkat`, `catatan penelitian`, `ulas balik`). |
| Skripsi, tesis, disertasi | *Type*: `skripsi`, `tesis`, `disertasi` (juga `perangkat lunak`, `studi kasus`, dan jenis lain di hlm. 78). Isi *University* dan *Place*. |
| Tanpa penulis | *Short Title* berisi bentuk dalam teks: `Tren ...`, `UU`, `Melepas`. |
| Pracetak | Jenis item *Preprint*, *Repository* `arXiv`. |
| Prosiding | *Place* = kota pertemuan. Tanggal pertemuan lewat *Extra*: `event-date: 2015-10-19/2015-10-20` (berfungsi dari CSL JSON; belum diuji lewat Zotero). |
| Paten | Penemu sebagai *Inventor*. *Issuing Authority* = nama negara (`Indonesia`), *Patent Number* = kode negara dan nomor (`ID S000010062`), *Issue Date* = tanggal publikasi. Pemegang paten lewat *Extra*: `publisher: Institut Pertanian Bogor`, karena Zotero tidak mengekspor kolom *Assignee* dan *Country*. |
| Artikel diterima, belum terbit | *Extra*: `status: siap terbit`. |
| Volume berjudul | *Extra*: `volume-title: Pigs, Hippopotamuses, …`. |
| Tahun tidak diketahui | Kosongkan tanggal; gaya mencetak `[tahun terbit tidak diketahui]`. Untuk laman web, pedoman meminta tanggal pemutakhiran. |
| Penerbit tidak diketahui | Kosongkan *Publisher*; gaya mencetak `[penerbit tidak diketahui]`. |

## Keputusan pada bagian yang tidak jelas di pedoman

| Hal | Di pedoman | Gaya ini |
|---|---|---|
| Jumlah penulis | Aturan: 5, selebihnya *et al.* (hlm. 69). Beberapa contoh memuat 7–10 nama (hlm. 74–75) | 5, lalu *et al.* |
| Titik setelah *et al.* | Aturan: tanpa titik tambahan (hlm. 69). Contoh mencetak `et al..` (hlm. 73) | `et al. 2026.` |
| Prosiding daring | Templat: `halaman artikel. Lokasi (URL)`. Contoh: `hlm 167–175; [diakses …]. URL` (hlm. 78) | `hlm 167–175. [diakses …]. URL.` |
| Tempat terbit | Hilang dari buku (hlm. 76); tetap ada pada dokumen dan skripsi (hlm. 78–79) | Mengikuti contoh, per jenis pustaka |
| DOI selain artikel jurnal | Dicontohkan untuk artikel jurnal saja (7.2.1.6) | `doi:` dicetak untuk jenis apa pun yang memilikinya; jika tidak ada, `[diakses …]. URL` |
| Pracetak | Tidak ada bentuk | `[pracetak]` setelah judul |
| Beberapa acuan sekaligus; penulis yang sama | Tidak dibahas di teks PPTA | Urut tahun, dipisah `;`; (Sunarti 2005, 2006); (Puspitawati 2009a, 2009b), diwarisi dari PPKI Edisi 4 |
| Bahasa Inggris | PPTA berlaku untuk kelas internasional, tetapi tidak memberi bentuk Inggris | Kata penghubung mengikuti CSE: "and", "In:", "editors", "accessed", "p", "inventor" |

## Versi bahasa Inggris

Satu gaya, dua bahasa. Yang berubah hanya kata penghubung dan nama bulan; bentuk nama, urutan, dan tanda baca tetap mengikuti PPTA.

| Indonesia | Inggris |
|---|---|
| (Rusmana dan Nedwell 2024) | (Rusmana and Nedwell 2024) |
| Di dalam: Aguirre AA, Sukumar R, editor. | In: Aguirre AA, Sukumar R, editors. |
| Syartinilia, penerjemah. | Syartinilia, translator. |
| [diakses 2026 Mei 12] | [accessed 2026 May 12] |
| hlm 290–300 | p 290–300 |
| [pracetak] | [preprint] |
| …, penemu; … Paten Indonesia ID … | …, inventor; … Patent Indonesia ID … |
| [tahun terbit tidak diketahui] | [date unknown] |
| Agu, Okt, Des, Mei | Aug, Oct, Dec, May |

Cara memakainya:

- **pandoc:** berkas yang sama dengan `-M lang=en-US`, atau `lang: en-US` di metadata YAML dokumen.
- **Zotero:** pasang `ipb-ppta-en.csl` dan pilih *IPB: Pedoman Penyajian Tugas Akhir 2026 (PPTA, unofficial, English)* di Document Preferences. Berkas ini dibuat dari `ipb-ppta.csl` oleh `make_en.py`; hanya bahasa bawaan, nama, dan id gaya yang berbeda.

Judul, nama jurnal, dan nama penerbit dicetak seperti di data; judul berbahasa Indonesia tidak diterjemahkan.

## Pengujian

```sh
python check_ipb_csl.py      # butuh pandoc 3 di PATH
python make_en.py --check    # ipb-ppta-en.csl sinkron dengan ipb-ppta.csl
```

Setelah mengubah `ipb-ppta.csl`: jalankan `python check_ipb_csl.py`, lalu `python make_en.py` untuk memperbarui versi Inggris.

## Lisensi dan kredit

- Berkas `.csl`: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Dikembangkan dari gaya Zotero "Institut Pertanian Bogor" (PPKI Edisi ke-3) karya Auriza Rahmad Akbar dan M. Rachmatarramadhan.
- Pedoman PPTA: hak cipta IPB / IPB Press; tidak disertakan di repositori ini.
- Dibuat untuk sebuah tugas akhir di IPB dengan bantuan Claude Code; setiap bentuk diuji terhadap contoh-contoh pedoman lewat `check_ipb_csl.py`.
