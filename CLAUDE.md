# App Fundamental Math: panduan untuk Claude

Baca file ini dan `RENCANA.md` sebelum mengubah apa pun. Dokumen konsep lengkap ada di `konsep.md`.

## Tentang pemilik
- Faiq: pejuang UTBK-SNBT April 2027, non-saintek, cemas dengan matematika, bukan orang teknis.
- Selalu jawab dalam **Bahasa Indonesia**, ringkas (kira-kira satu layar HP).
- Faiq tidak sempat menguji semua game sendiri. **Uji sendiri** setiap perubahan sebelum menyerahkan.
- Cara kerja: usulan singkat dulu (cocokkan dengan dokumen konsep), kode sesudah Faiq setuju, kecuali ia bilang "langsung terapkan".

## Inti app
- App **mini games & puzzle, bukan app materi**. Pemain berperan sebagai peneliti yang **menemukan bagaimana rumus dibangun** dari masalah sehari-hari.
- **Jangan melenceng dari dokumen konsep**: tabel 64 subchapter dan tabel game "Temuan F → I → E". Cocokkan setiap rancangan dengan tabel itu.

## Aturan yang tidak boleh dilanggar
1. **Tidak ada clue yang mengarah ke jawaban.**
   - App tidak menghitung sesuatu yang seharusnya ditemukan pemain.
   - Pesan tidak menyiratkan langkah ("kurang/kelebihan" diganti "tidak pas").
   - Alat di papan bukan urutan langkah.
   - **Daftar pilihan jadi juga dihitung sebagai clue.**
2. **Nama konsep tidak muncul sebelum pemain menemukannya.** Pakai bahasa sehari-hari.
3. **Semua bagian bercerita**, maksimal 3 kalimat.
4. Anti otak-atik mekanis: rencana dulu, jatah kesempatan, angka di luar papan, kasus harian berisi klaim, jawaban "Tidak bisa ditentukan" dan "Tidak mungkin".
5. Pemilih angka 1–9. Latihan hanya di awal game. Tombol "?" berisi petunjuk tombol, bukan cara memecahkan.
6. Tampilan minimalis, elemen kecil, tidak menggelembung.

## Struktur yang sudah tetap
- 4 materi: Bilangan (7 game), Aljabar (9), Geometri & Pengukuran (6), Data & Ketidakpastian (5).
- Tingkat: Fundamental (F), Intermediate (I), Expert (E).
- **Tingkat = tangga temuan per game.** Tiap tingkat punya:
  - 3 misi sendiri (makin sulit);
  - kasus harian bertanda tingkat itu (minimal 3);
  - rumus Aturan milik tingkat itu.
- Tingkat dipilih **di dalam game** (chip di layar Pilih mode). Game membuka tingkat terakhir yang dimainkan.
- Mini Games 2 langkah: pilih subject → pilih game.
- Bintang per game per tingkat:
  - ★1: semua misi selesai;
  - ★2: tepat 8 dari 10 kasus terakhir;
  - ★3: satu aturan lolos uji.
- Tab bawah: Beranda, Mini Games, Progres, Jurnal, Temuan.
- Semua halaman non-game membaca progres asli lewat `FMP`. Jangan menulis angka contoh lagi.
- Kasus harian per tingkat per hari: 1 kasus cerita (bergilir, termasuk kasus tempelan) + 2 kasus "Angka baru" buatan `FMP.genCase`. Lihat RENCANA.md.

## Struktur kode `index.html`
Satu file, tanpa build. Pendamping: `sw.js` (menyimpan app di perangkat untuk GitHub Pages; buka dari salinan, versi baru dipakai pada pembukaan berikutnya) dan layar muat `#fm-splash` di awal `<body>`.
- **`<template id="tpl-Nama">`**: tampilan satu layar.
  - `{{nilai}}` diisi dari `renderVals()`.
  - `<sc-for list="{{daftar}}" as="x">` untuk mengulang.
  - `<sc-if value="{{kondisi}}">` untuk menampilkan bersyarat.
  - Hanya nama/jalur (`a.b`) yang boleh di dalam `{{ }}`, bukan ekspresi.
  - Tombol memakai `onClick="{{namaFungsi}}"`.
- **`GAMES["Nama"] = (function(){ class Component extends DCLogic {...} return Component; })();`**: logika layar yang sama.
  - `renderVals()` mengembalikan objek nilai untuk template.
  - Game memakai `this.gmWrap(this.gmRender())`.
- **Navigasi:** tautan `href="Nama.dc.html"` otomatis dibuka sebagai `#Nama`. Layar awal `Main`.
- **Data tersimpan (localStorage):**
  - `fm.minigames.return` {mat, lvl, g, t}
  - `fm.lastLvl` {namaGame: lvl}
  - `fm.settings` (termasuk `anim`, `music`, `sfx`: saklar animasi, musik, efek suara; bawaan nyala)
  - `fm.progress` (progres pemain, lihat modul `FMP` dan RENCANA.md)
  - `fm.anim.seen` (bintang yang sudah pernah dianimasikan, lihat RENCANA.md bagian "Animasi")
- **Pola tingkat (contoh di 7 game Bilangan):**
  - `this.T = {F:[...3 misi], I:[...], E:[...]}`;
  - `initLvl()`, `curLvl()`, `setLvl(l)`;
  - `mission(i)` mengambil dari tingkat aktif;
  - `todayIdx` memilih kasus harian `tingkat === curLvl()`;
  - chip `gmTiers` di Pilih mode.
- **Adegan harus masuk akal (permintaan Faiq 16 Nov):** tidak ada benda melayang, perspektif konsisten (kursi di belakang meja, bukan tertutup kaki meja), tiap benda berbentuk jelas (kubis bulat, telur lonjong, karung berbentuk karung). Periksa setiap gambar adegan sebelum menyerahkan.
- **Gaya benda (Faiq 18 Nov, dari referensi ikon pixel):** tiap papan dan benda = alat atau benda nyata di tempat game itu, **bukan semuanya kayu**. Ciri gaya: garis tepi biru tua tebal (#1A1C2C), sisi depan terlihat (tebal 3D), bayangan dan kilau berlapis (3–4 warna), kilap diagonal di layar/kaca. Contoh yang sudah disetujui: kalkulator Meja Hajatan, mesin kasir Kasir Kilat. Bingkai 9-potong ada di modul PX (`--px-cBody`, `--px-kDark/kCream/kOrange/kRed/kGreen`, `--px-lcdBez`).
- **Lihat sendiri hasilnya, jangan formalitas (Faiq 18 Nov):** setelah mengubah tampilan, buka tangkapan layarnya (ukuran ponsel dan iPad) dan nilai dengan jujur: apakah benda itu benar-benar terasa pixel art dan seperti benda aslinya, atau hanya kotak yang diberi tepi? Kalau masih terasa prototipe, perbaiki sebelum menyerahkan.
- **Warna benda harus cocok dengan teks.** Sebelum mengganti warna benda, cari teks bantuan/keterangan yang menyebut warnanya ("koin biru", "abu-abu = bangunan", "tombol oranye"); isi tidak boleh diubah, jadi warnanya yang menyesuaikan.
- **Huruf (ditetapkan Faiq 18 Nov):** **seluruh teks memakai huruf pixel lembut Jersey 15** (disisipkan; kelas `fm-pxtext` di `<html>`, ukuran disamakan dengan `font-size-adjust`), termasuk cerita, angka, dan isi soal. Jangan pakai Pixelify Sans/Tiny5 (B terbaca G). Jangan menghapus `fm-pxtext`.
- **Tema pixel sungguhan (koreksi Faiq 17 Nov):** tombol dan kotak harus pixel art asli (bingkai sprite 9-potong `fWhite/fGold/fGreen/fWood/fPaper/fRed/fOrange`, hati/lencana/panah sprite), bukan sudut membulat gaya game kasual.
- **Latar tenang (permintaan Faiq 16 Nov):** jangan pakai pola yang bikin pusing (kotak-kotak kontras, garis rapat). Lantai dan dinding polos atau bergaris samar. Tidak ada elemen yang tumpang tindih (pemandangan tidak boleh di belakang tombol; taruh di ujung bawah). Tiap layar sederhana, tidak terlihat penuh.
- **Tema pixel (sudah di Beranda, Mini Games, Kasir Kilat):** kelas CSS `.px-*`, bingkai `px-fw` (putih), `px-fg` (emas), `px-fs` (kayu); gambar dari modul `PX` (`{{px.nama}}` lewat `px: PX.U` di `renderVals`). Desain boleh diubah bebas, isi tidak.
- **Nama tampilan game (Faiq 18 Nov):** Ubin → Tata Barisan, Jadwal Bus → Kapan Bareng?, Martabak Topping → Pesanan Martabak, Kebun Pagar → Kebun & Lintasan, Gudang Kardus → Isi Wadah, Cetak Spanduk → Perbesar Gambar, Loker OSIS → Pilihan OSIS. **Nama lama tetap kunci di kode dan progres tersimpan**; teks di layar diganti oleh `relabel()` (peta `GAME_DN`, dipanggil tiap render di `show()`). Tambah nama baru di `GAME_DN`, jangan ganti kunci.
- **Animasi (dirancang bersama Faiq sejak 19 Nov):** kelas `fm-noanim` di `<html>` tetap mematikan semua animasi lama. Hanya animasi yang disetujui Faiq yang jalan: blok CSS "Animasi yang sudah disetujui Faiq" dan modul `FMA`. Prinsip dan daftar momen ada di RENCANA.md bagian "Animasi". Saklar Animasi di Pengaturan yang menentukan (bukan "Kurangi gerakan" iPad, keputusan Faiq 19 Nov). Jangan menambah animasi di luar daftar yang disetujui.
- **Sebelum menyisipkan kode yang sama ke banyak game, cek nama variabel di tiap game.** Game Aljabar, Geometri, dan Data dibuat terpisah, jadi strukturnya berbeda.

## Cara menguji
- **Faiq memakai iPad mini 7 (744 × 1133).** Uji di ukuran itu dan di ukuran ponsel (390 × 844). **Sejak 17 Nov (permintaan Faiq): di layar ≥ 600 px app dikunci ke bingkai HP 430 × 874** (sedikit lebih lebar dari iPhone 17/18 Pro 402 × 874, permintaan Faiq; sudut kotak) yang diperbesar sampai setinggi layar (`body.fm-phone`, `transform: scale` pada `#root`, skrip di akhir `index.html`). Di luar bingkai (disetujui Faiq 18 Nov): **latar netral tetap** krem #EFE9DE dengan titik samar, sama di semua layar; bingkai bergaris tipis gelap (1,5 px) dan bayangan lembut (Faiq: garis tebal terlalu berat) (Faiq 18 Nov, setelah blur, warna dominan, dan perpanjangan tepi semuanya ditolak: terlalu ramai, tidak cocok, atau membuat pusing/tersendat). **Jangan membuat latar yang mengikuti isi layar lagi** kecuali Faiq memintanya. **Jangan pakai `filter: blur` CSS atau salinan DOM untuk latar ini**: membuat gulir patah-patah (laporan Faiq 17 Nov). Di skrip uji ketuk lewat koordinat (`mouse.click`) dengan pemilih `#root …`. Aturan lama kolom 560 px/`--padX` tidak aktif lagi (`--padX` = 0). Peta Beranda: inti 195 × 330 kotak + 80 kotak kiri-kanan (`PX.WORLD`); letak tempat dan titik jalan tokoh di `NODES`/`SPOTS` layar Main.
- Buka `index.html` di browser. Pastikan setiap layar tampil (tidak muncul kotak merah "Layar … gagal dibuka").
- Ketuk tombol-tombolnya. Tidak boleh ada error di console.
- Periksa juga aturan anti-clue di atas.
