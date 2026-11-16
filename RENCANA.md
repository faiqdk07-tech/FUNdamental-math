# Rencana kerja

Perbarui file ini setiap kali ada pekerjaan selesai atau keputusan baru dari Faiq.

## Sudah selesai
- **16 Nov:** audit soal acak (tombol Berikutnya/…lain) di semua game. Diperbaiki: Kasir Kilat "Koin menipis" (kembalian mustahil), jatah kesempatan soal acak (Kasir, Ubin, Jadwal Bus), Bagi Pizza "Pisau tumpul" (tujuan berganti), dan teks tujuan soal acak yang masih memakai klaim atau angka lama (lewat `FMP.nextGoal`).
- **16 Nov:** progres nyata. Hasil main disimpan di `fm.progress`, dan Beranda, Mini Games (bintang), Progres, Jurnal, Pohon Temuan, Tantangan, Bengkel, Cek Celah (versi saran), serta Pengaturan (unduh/pulihkan cadangan, hapus) memakai data itu. Semua angka contoh dihapus. Tombol Lanjutkan, Tantangan, Bengkel, dan saran membuka misi/kasus yang tepat. Tanda ✓ misi kini per tingkat dan tetap ada setelah app ditutup.
- **16 Nov:** tingkat F/I/E diterapkan ke 5 game Data (rincian di bawah). Sekarang semua 27 game punya tingkat.
- **16 Nov:** tingkat F/I/E diterapkan ke 6 game Geometri (rincian di bawah). Lolos uji otomatis seperti Aljabar.
- **16 Nov:** tingkat F/I/E diterapkan ke 9 game Aljabar (rincian di bawah). Tiap tingkat: 3 misi, minimal 3 kasus harian, rumus Aturan sendiri. Lolos uji otomatis: semua misi, kasus harian, dan tombol Berikutnya bisa diselesaikan.
- **16 Nov:** semua layar dipindah dari kanvas ke satu `index.html`. Kanvas v4 sekarang hanya arsip.
- **16 Nov:** crash tombol "?" diperbaiki di semua game. Panel bantuan sekarang memakai `this.state.help` dan `this.state.gmMenu`.
- **15 Nov:**
  - 7 game Bilangan direvisi dan diberi tingkat F/I/E (rincian di bawah).
  - Mini Games dibuat 2 langkah.
  - Tombol "?" ditambahkan ke semua game.

## Berikutnya (urut)
1. **Faiq menguji game Bilangan, game Aljabar, Geometri, dan Data per tingkat, dan Mini Games 2 langkah**, lalu mengisi lembar jawaban. Perbaiki sesuai masukan.
2. **Desain tema:** 2–3 pratinjau dulu, lalu satu set warna dan huruf untuk semua layar.
3. **Cek Celah versi tes:** 2 tantangan singkat per game yang menyarankan tingkat (ditunda, disetujui Faiq 16 Nov).
4. **Tahap berikutnya:**
   - kasus harian lewat prompt → JSON → validator (tiap kasus punya `tingkat`);
   - Koleksi Rumus;

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

## Rincian tingkat 9 game Aljabar (sudah diterapkan 16 Nov)
- **Dua Struk** (`this.T`): F dua struk cukup ×3 · I struk perlu digandakan ×3 · E tiga barang (biasa, puluhan ribu, tampilan tabel). Harian F f1–f4 · I d1,d2,d4,d7,d8 · E d3,d5,d6. Aturan F selisih struk, I gandakan, E coret harga.
- **Meja Hajatan** (`this.T`): F 10/25/40 meja · I baris ke-15, total 15, total 20 baris · E meja dari 100 kursi, undangan 5 gelombang, sampai 1.000 orang. Harian F f1–f3 · I m1,m2,m5,m6,m8 · E m3,m4,m7.
- **Martabak Topping** (`this.TM`): F sortir sederhana, "dan", daftar vs syarat · I racikan 3/4/6 topping · E survei 40, 60, yang tidak memilih. Aturan F baru: n(A saja) = n(A) − n(A ∩ B).
- **Mesin Minuman**: F kabel 3/4/5 tombol · I 2 komponen, tabel kedua (urutan ditukar), 3 komponen (12x + 5) · E pembatal ×3+2, +4×2, 3 komponen. Aturan F baru: + a lalu − a.
- **Argo Ojek**: F 23 km, 40 km, klaim < 70 ribu · I radius km 3, km 12, dua pangkalan (fitur baru `a2`, `b2`) · E 30&60, 40&60, klaim 36&45.
- **Timbangan Balon** (`this.MA`): 3 misi balon per tingkat; kasus harian balon baru hb1–hb7 (F hb1–3, I h11,hb4,hb5, E h12,hb6,hb7).
- **Rekap Grosir**: F tabel 2×2, 3×3, 3×4 · I 2 pelanggan, 3 pelanggan, 3 barang · E luas label 5, 10, 0 (gepeng).
- **Kebun Pagar**: F pagar 24, 28, 40 m (28 dipakai, bukan 30, supaya jawabannya bulat) · I roket jatuh detik 22, 18, 30 · E kebun 299, 187, 351 m².
- **Dapur Roti**: F satu bahan ×3 · I memilah catatan ×3 · E dua bahan ×3.
- Kerangka 6 game terbaru: `this.TM`/`this.TN`/`this.TO` per tingkat (misi, nama, aturan), `curM()`, `genMission` membaca tingkat aktif. Tombol Berikutnya membuang klaim (`verdict`) dari soal acak.
- Teks Mini Games untuk Timbangan Balon, Meja Hajatan E, dan Rekap Grosir E disesuaikan.

## Rincian tingkat 6 game Geometri (sudah diterapkan 16 Nov)
Kerangka sama dengan 6 game Aljabar terbaru (`this.TM`, `this.TN`, `this.TO`). Tiap tingkat F mendapat 1 kasus harian klaim baru (`f3`).
- **Rute Kurir:** F antar paket (2, 3, 4 jalan ditutup) · I langkah Andi/Budi, tali rafia, klaim Budi · E bundaran 36 pojok, taman 12 pojok, taman 7 pojok tak beraturan. Aturan F baru: blok terpendek = x + y. Kasus harian E baru: r9.
- **Pasang Lantai:** F kamar, gudang, ruang rapat (dengan aula di luar papan) · I 2 teras miring, taman segitiga · E kaca meja r 50, 30, 70.
- **Gudang Kardus:** F kardus sabun, mi, jumbo · I akuarium L, segitiga, kolam · E wadah lancip 6×6×10, 9×9×8, 12×12×15.
- **Cetak Spanduk:** F logo dibesarkan (8, tegak 6), dikecilkan (8→4) · I tinta 6×, 3×, klaim 2× · E pohon, menara air, tiang bendera.
- **Tangga Bangunan:** F persegi 3-4/6-8, 2-4/5-12, 1-3/8-15 · I kaki tangga 3 soal, klaim 13−12 · E miring 30°, 45°, 60°. Teks `tujuan` f1/f2 yang salah sisi diperbaiki.
- **Pelabuhan:** F peta laut 3 soal · I radar 3 soal · E dua menara 3 soal. Urutan I/E tetap seperti di game (radar dulu), berbeda dengan tabel konsep.

## Rincian tingkat 5 game Data (sudah diterapkan 16 Nov)
Kerangka sama (`this.TM`, `this.TN`, `this.TO`). Tiap tingkat F mendapat 1 kasus harian `f3`.
- **Loker OSIS:** F outfit 2 jenis, 3 jenis, klaim 2+3+2 · I paket kantin 2 grup, 3 grup, klaim 5×4 · E PIN boleh kembar, tanpa kembar, klaim 10+10+10.
- **Pentas Seni:** F urutan 4&6, 5&8, klaim 6×6 · I papan dari 5, dari 8, klaim 8×720 · E 8 calon, 10 calon, 4 jabatan dari 7. Aturan I baru: urutan n = n × urutan (n − 1).
- **Undian Doorprize:** F peluang kupon 3 kotak (klaim "4 persen") · I dadu, kupon 250 peserta, koin 500 (klaim "pasti tepat") · E bola, genap atau kelipatan 3, setidaknya satu biru. Aturan F baru: m ÷ n × 100. `genMission` menyesuaikan jenis papan.
- **Rapor Kelas:** F rekap 10 nilai, 12 nilai (KKM 75), klaim selisih · I meratakan, nilai keempat, siswa pindahan · E 11 nilai, 10 nilai (genap), skor ekstrem 25. Aturan F baru: selisih = a − b.
- **Grafik Viral:** F garis, batang, lingkaran · I sumbu terpotong 3 grafik (klaim "dua kali lipat") · E judul naik 300%, naik 3 kali lipat, anjlok tiga perempat.
- Teks `tujuan` f1/f2 Pentas Seni yang salah jumlah kelompok diperbaiki.

## Progres nyata (16 Nov)
- Modul `FMP` (di atas blok Navigasi) menyimpan `fm.progress`: `ev` (setiap misi/kasus: game, tingkat, benar/gagal), `tiers` (misi selesai dan aturan lolos per game-tingkat), `journal`, `guesses` (dugaan ditolak), `bengkel`, `fixed`, `last`, `tant`, `lab`.
- Game tidak diubah satu per satu: `show()` membungkus kelas game dengan `FMP.wrap`, yang mengamati `setState` (stage selesai, "Kesempatan habis", `rules` bertambah, `customs` bertambah) dan tombol Uji di Aturan.
- Bintang: ★1 misi 1–3 selesai, ★2 ≥ syarat Pengaturan (default 8) dari 10 kasus harian terakhir, ★3 satu aturan lolos.
- Tautan langsung: `FMP.go({key, g, l, mode, idx, id, regen})` lalu `FMP.applyOpen` di `show()`. Kasus harian dibuka dengan mengganti `todayIdx` sementara.
- Pohon Temuan: subbab menyala bila game itu punya aturan lolos di tingkat yang sama dengan level subbab.
- Batas: Timbangan belum mencatat dugaan yang ditolak (Aturannya berbeda bentuk). Kasus harian di Bengkel dibuka dengan soal yang sama.

## Catatan
- Rotasi kasus harian memakai hari UTC, jadi berganti pukul 07.00 WIB.
