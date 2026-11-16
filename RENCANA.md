# Rencana kerja

Perbarui file ini setiap kali ada pekerjaan selesai atau keputusan baru dari Faiq.

## Sudah selesai
- **16 Nov:** semua layar dipindah dari kanvas ke satu `index.html`. Kanvas v4 sekarang hanya arsip.
- **16 Nov:** crash tombol "?" diperbaiki di semua game. Panel bantuan sekarang memakai `this.state.help` dan `this.state.gmMenu`.
- **15 Nov:**
  - 7 game Bilangan direvisi dan diberi tingkat F/I/E (rincian di bawah).
  - Mini Games dibuat 2 langkah.
  - Tombol "?" ditambahkan ke semua game.

## Berikutnya (urut)
1. **Faiq menguji game Bilangan dan Mini Games 2 langkah**, lalu mengisi lembar jawaban. Perbaiki sesuai masukan.
2. **Terapkan tingkat F/I/E Aljabar** (disetujui Faiq 15 Nov). Pakai pola game Bilangan:
   - Dua Struk:
     - F: dua struk cukup (3 pasang)
     - I: struk perlu digandakan
     - E: tiga barang tiga struk (biasa, angka besar, tabel)
   - Meja Hajatan:
     - F: 10, 25, 40 meja
     - I: baris ke-15, total 15, total 20 baris
     - E: meja terbanyak dari 100 kursi, undangan 5 gelombang, sampai 1.000 orang
   - Martabak Topping:
     - F: sortir aturan sederhana, "dan", daftar vs aturan
     - I: racikan 3, 4, 6 topping
     - E: survei 40, 60, yang tidak memilih keduanya
   - Mesin Minuman:
     - F: kabel 3, 4, 5 tombol
     - I: berantai 2 komponen, urutan ditukar, 3 komponen
     - E: pembatal "×3 lalu +2", "+4 lalu ×2", 3 komponen
   - Argo Ojek:
     - F: ongkos 23 km, 40 km, klaim <70 ribu
     - I: radius 4 dari km 3, radius 5 dari km 12, dua pangkalan
     - E: rata-rata 30&60, 40&60, klaim 40
   - Timbangan Balon: tambah 2 misi balon per tingkat di `this.MA`.
   - Rekap Grosir:
     - F: tabel 2×2, 3×3, 3×4
     - I: total 2 pelanggan, 3 pelanggan, 3 barang
     - E: luas label ditarik ×3 (termasuk gepeng 0)
   - Kebun Pagar:
     - F: pagar 24, 30, 40 m
     - I: roket jatuh detik 22, 18, 30
     - E: tiga kebun diperluas
   - Dapur Roti:
     - F: satu bahan ×3
     - I: memilah catatan ×3
     - E: dua bahan ×3
3. **Desain tema:** 2–3 pratinjau dulu, lalu satu set warna dan huruf untuk semua layar.
4. **Tingkat Geometri, lalu Data:** cek tabel "Temuan F → I → E" di `konsep.md`, ajukan usulan singkat dulu.
5. **Tanda Selesai per tingkat** (sekarang masih per nomor misi). Bintang diambil dari progres asli, bukan data contoh.
6. **Tahap berikutnya:**
   - kasus harian lewat prompt → JSON → validator (tiap kasus punya `tingkat`);
   - Koleksi Rumus;
   - Bengkel dan Cek Celah memakai data nyata.

## Rincian tingkat 7 game Bilangan (sudah diterapkan)
- **Kasir Kilat**
  - Misi:
    - F: kembalian 50/100, maks 3 koin
    - I: laci berpasangan/campur/minus
    - E: struk 4/6 harga/kilat
  - Kasus harian: F k1,k5,k9 · I k2,k6,k8 · E k3,k4,k7
- **Timbangan**
  - Misi:
    - F: seimbangkan
    - I: tiga misi kardus
    - E: miring tanpa balon
  - Kasus harian: F h7,h13,h14 · I h1–h5,h8–h10 · E h6,h15,h16
  - Kalau dibuka dari Aljabar, memakai misi balon (`this.MA`).
- **Ubin**
  - Misi:
    - F: nampan 12/18/24
    - I: aula 4×6, 5×4, 6×7
    - E: aula 17×23, 15×24, 18×21
  - Kasus harian: F u1,u2,u7 · I u3,u6,u8 · E u4,u5,u9
- **Jadwal Bus**
  - Misi:
    - F: bus 6&8, 4&10, 9&12
    - I: pita 24&36, 30&45, 42&56
    - E: 30, 100, 60 hari
  - Kasus harian: F j1,j4,j5,j8 · I j2,j6,j9 · E j3,j7,j10
- **Bagi Pizza**
  - Misi:
    - F: 3/4, 3/6 hemat, 4/6
    - I: papan sisa, lewat 1, klaim
    - E: porsi 1/2, 1/3, 2/3
  - Kasus harian: F b1,b5,b8 · I b3,b7,b9 · E b2,b4,b6
- **Racik Resep**
  - Misi:
    - F: 4→8/12/2
    - I: 4→6, 6→9, saran tambah 3
    - E: kupon, tumpuk, tiga kupon
  - Kasus harian: F r2,r9,r10 · I r1,r3,r11 · E r4–r8
- **Lipat Kertas**
  - Misi:
    - F: 24/36/48 hemat
    - I: 4+3, 3+5, klaim 5+5
    - E: ≥100/1.000/10.000
  - Kasus harian: F l1,l2,l3 · I l4,l5,l6,l8 · E l7,l9,l10

## Catatan
- 19 game non-Bilangan belum punya pilihan tingkat.
- Rotasi kasus harian memakai hari UTC, jadi berganti pukul 07.00 WIB.
