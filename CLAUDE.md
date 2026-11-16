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
Satu file, tanpa build.
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
  - `fm.settings`
  - `fm.progress` (progres pemain, lihat modul `FMP` dan RENCANA.md)
- **Pola tingkat (contoh di 7 game Bilangan):**
  - `this.T = {F:[...3 misi], I:[...], E:[...]}`;
  - `initLvl()`, `curLvl()`, `setLvl(l)`;
  - `mission(i)` mengambil dari tingkat aktif;
  - `todayIdx` memilih kasus harian `tingkat === curLvl()`;
  - chip `gmTiers` di Pilih mode.
- **Adegan harus masuk akal (permintaan Faiq 16 Nov):** tidak ada benda melayang, perspektif konsisten (kursi di belakang meja, bukan tertutup kaki meja), tiap benda berbentuk jelas (kubis bulat, telur lonjong, karung berbentuk karung). Periksa setiap gambar adegan sebelum menyerahkan.
- **Warna benda harus cocok dengan teks.** Sebelum mengganti warna benda, cari teks bantuan/keterangan yang menyebut warnanya ("koin biru", "abu-abu = bangunan", "tombol oranye"); isi tidak boleh diubah, jadi warnanya yang menyesuaikan.
- **Huruf (permintaan Faiq 16 Nov):** jangan pakai huruf pixel untuk teks. Judul dan label memakai Fredoka (bulat, halus), teks biasa Inter. Gambar boleh tetap pixel.
- **Latar tenang (permintaan Faiq 16 Nov):** jangan pakai pola yang bikin pusing (kotak-kotak kontras, garis rapat). Lantai dan dinding polos atau bergaris samar. Tidak ada elemen yang tumpang tindih (pemandangan tidak boleh di belakang tombol; taruh di ujung bawah). Tiap layar sederhana, tidak terlihat penuh.
- **Tema pixel (sudah di Beranda, Mini Games, Kasir Kilat):** kelas CSS `.px-*`, bingkai `px-fw` (putih), `px-fg` (emas), `px-fs` (kayu); gambar dari modul `PX` (`{{px.nama}}` lewat `px: PX.U` di `renderVals`). Angka dan cerita soal selalu Inter; judul dan label Fredoka (kelas `px-f`). Desain boleh diubah bebas, isi tidak.
- **Sebelum menyisipkan kode yang sama ke banyak game, cek nama variabel di tiap game.** Game Aljabar, Geometri, dan Data dibuat terpisah, jadi strukturnya berbeda.

## Cara menguji
- Buka `index.html` di browser. Pastikan setiap layar tampil (tidak muncul kotak merah "Layar … gagal dibuka").
- Ketuk tombol-tombolnya. Tidak boleh ada error di console.
- Periksa juga aturan anti-clue di atas.
