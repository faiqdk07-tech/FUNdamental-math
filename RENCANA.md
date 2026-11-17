# Rencana kerja

Perbarui file ini setiap kali ada pekerjaan selesai atau keputusan baru dari Faiq.

## Sudah selesai
- **17 Nov: evaluasi E tahap 1 (contoh di Meja Hajatan dan Kasir Kilat), menunggu cek Faiq sebelum disebar ke game lain.** Faiq menolak versi gaya "game kasual" (sudut membulat): **semua harus tetap pixel art sungguhan** seperti referensinya (tombol kayu/emas bersudut tangga, hati pixel, kotak dialog pixel, papan nama kayu).
  - Kerangka baru (kelas `px-v2` di `.px-screen`, nilai dari `PX.v2(comp, v, {face, name})`): bilah judul papan kayu (`fWood`) dengan hati pixel (`SPR.hati`/`hati0`) pengganti teks kesempatan; pilih misi jadi jalur level (lencana emas `lvA`, selesai = hijau `lvB` + bendera); tokoh berbingkai + papan nama kayu, balon putih pixel, tombol "Lanjut ▶"; papan permainan baru tampil setelah Lanjut (`v2wait`); kartu Tugas kertas kuning (`fPaper`); tombol angka keping kayu, hapus merah, Cek hijau (`fGreen`); jendela hasil dialog pixel dengan wajah tokoh + tombol Misi berikutnya; catatan percobaan, papan kapur, kertas tempel bergaya pixel.
  - Revisi Faiq: jarak antarkotak 26 px, hati di kanan papan judul, label misi menempel di tepi atas balon, kartu tugas jadi kertas bergaris dengan garis tepi merah, paku merah, dan sudut terlipat.
  - Langkah penyebaran: pola sisipan template ada di skrip pembuat (`tplv2.py` di sesi ini): `common()` untuk baris atas, pilih misi, jendela hasil; per game: blok cerita, pesan, tombol Cek, tombol khusus.
- **17 Nov: ukuran iPad diubah** atas permintaan Faiq (ia lebih suka tampilan jendela iPad ±555 pt): kolom isi 470 → 560 px, perbesaran maks. 1,2× → 1,05×. Peta Beranda/Mini Games ikut batas 560 px. Layar Pilih mode di iPad diperbesar 1,25× (`zoom` pada `.px-mid:has(> .px-modes)`) karena papan tingkat dan panel mode berukuran tetap sehingga terlihat kecil.
- **17 Nov: evaluasi D (layar Pilih mode) selesai** untuk 26 template game.
  - D2: gambar Intermediate jadi semak (`SPR.semak`), papan tingkat diperkecil.
  - D3/D5: papan gantung "Pilih mode" dihapus; 4 mode dalam satu panel putih bertepi biru berlabel kuning (`.px-modes`), tiap mode tombol pendek dengan blok warna + ikon (`.px-mode2`, `.px-m-Misi` oranye, Harian biru, Lab hijau, Aturan ungu).
  - Masukan lanjutan: panel Pilih mode, kartu Pengenalan games, dan kotak "?" di layar Pilih mode dibatasi 362 px di tengah (tidak melebar); jarak antartombol mode 12–14 px dan ruang dalam panel lebih lega supaya tidak berdempetan.
  - D7: kotak tombol "?" (menu dan saat bermain) jadi `.px-helpbox`: label kuning "Cara main · …", tombol tutup ×, tiap petunjuk satu baris berpenanda, tombol "Ulangi hari pertama". Isi petunjuk tidak berubah.
  - Catatan teknis "Timbangan Balon membuka game Timbangan…" di Mini Games Aljabar dihapus (pemain tidak perlu tahu).
- **17 Nov: evaluasi C (Mini Games) selesai**, disetujui Faiq.
  - Langkah 1 jadi peta pilih subject (`PX.mgMap`, 195 × 300 + tepi 80): langit, bukit, air mancur, kolam bebek, kebun bunga, gapura desa; 4 gedung dengan papan nama (nama + jumlah game tuntas, tanpa tali). Tokoh berjalan dari gapura ke gedung yang diketuk (`MG_NODES`), lalu masuk ke langkah 2.
  - Langkah 2: pemandangan gedung subject di atas (`PX.mgTop`), rak game ala tas RPG (`.px-gslot`, ikon besar, nama, bintang ★1 tiap tingkat), panel bawah cerah berisi tugas singkat, bintang F/I/E, dan tombol Main.
  - **Revisi Faiq 17 Nov:** rak kotak diganti jalan desa per subject (`PX.mgStreet`, letak `PX.PLACE_AT`, 3 tempat per baris): tiap game = tempatnya sendiri (`PLACES`), mis. warung (Kasir Kilat), gudang + beban (Timbangan), halte + bus (Jadwal Bus), tenda hajatan, gerobak martabak, dua mesin minuman, pangkalan ojek, kebun berpagar bambu, tembok bata + tangga, dermaga + kapal, panggung, dll. Papan nama di depan pintu: ikon + nama (+ bintang bila sudah dimainkan).
  - **Revisi Faiq 17 Nov (2):** jalan desa langkah 2 bisa digeser ke kiri-kanan (`.px-mgscroll`, skala `--stU`). Tempat berselang-seling di dua sisi: urutan genap di atas jalan utama, ganjil di bawahnya dengan jalan kecil kedua di bawah, dihubungkan jalan tegak (`PLACE_AT`, `streetW`).
  - Judul jadi pita biru bertulisan putih bergaris tepi (`.px-ribbon2`) dengan ikon stik game; ikon tab Mini Games di semua layar diganti stik (`SPR.stik`).
  - Pita merah "Baru" diganti gelembung "!" kuning. Baris aturan bintang dipindah ke tombol bintang di samping judul (kotak keterangan kecil).
- **17 Nov: evaluasi A dan B Faiq selesai** (dokumen "Urutan App Fundamental Math", tab Evaluasi per bagian). Bagian C–J belum dinilai Faiq.
  - A4/A5 iPad: latar penuh selebar layar, isi di kolom 470 px tengah (`--padX`), gambar ruangan atas ikut melebar (maks. 260/170 px tinggi supaya tidak raksasa saat mendatar).
  - B1/B10 peta desa baru (`PX.world`, 195 × 330 + tepi 80): alun-alun dengan papan pengumuman, 4 gedung, gudang dan menara di baris bawah, peti di taman kecil; tambahan dermaga, perahu nelayan, sumur, jemuran, sawah + orang-orangan, kolam bebek; di tepi (iPad) kandang ayam, padang sapi, jerami, gerobak sayur, kebun wortel, kincir.
  - Masukan lanjutan: pohon di peta Beranda dikurangi dari 24 jadi 7 dan tidak ada yang menempel ke bangunan, sawah, atau menara.
  - B12 tokoh berjalan menyusuri jalan tanah (graf `NODES`/`EDGES`, rute terpendek), menghadap arah jalan; tempat terpilih diberi siku putih; tanda seru lebih besar, bertepi putih, di pojok kanan atas gedung.
  - B2 sapaan jadi kartu pemain (wajah, nama, jumlah bintang asli). B3 "Mulai hari ini" jadi tombol api hari beruntun (abu-abu bila 0); diketuk, pemandu menjelaskan.
  - Masukan lanjutan 17 Nov: kartu pemain, target, api, dan pengaturan dipindah ke bilah atas kuning muda (`.px-topbar`, serasi dengan tab bawah) supaya tidak menyatu dengan laut; peta tidak ikut tertutup. Tokoh latar dibedakan sesuai peran dan hanya dua: nelayan bercaping di perahu (`SPR.nelayan`), petani (Bu Wati) di sawah.
  - B13/B15 panel bawah cerah: kotak putih bertepi biru, nama pembicara di label kuning, tombol tutup; "Lanjutkan" memakai ikon game. B14 gulungan "Coba berikutnya" lebih kecil, disembunyikan saat tempat dipilih.
- **16 Nov:** Faiq menolak hasil tahap 2–3 ("cuma ditambah kotak-kotak, masih format prototipe"). **Arah baru: tiap game dirancang ulang jadi adegan game pixel sungguhan** (template baru seperti Kasir Kilat), isi tetap. Kulit umum (`px-skin`) hanya sementara untuk layar yang belum dirancang ulang.
  - **Masukan Faiq (16 Nov): kotak soal di tengah, lebar, huruf lebih besar, jarak antar kotak lega.** Diterapkan: `.px-npc` jadi kolom (tokoh di atas, balon dialog lebar penuh, teks rata tengah 15px), jarak antar bagian 14–16px; Kasir Kilat disamakan. Pakai pola ini di semua game berikutnya.
  - **Latar dibuat tenang (permintaan Faiq 16 Nov):** lantai Kasir Kilat dari kotak-kotak jadi kayu polos, dinding warung tanpa garis, rumput dan dinding gudang lebih samar, petunjuk "ketuk = taruh" Timbangan jadi satu baris di bawah timbangan (tadinya dua kali dan tertimpa barang), pemandangan Jadwal Bus dipindah ke ujung bawah (`.px-endscene`) supaya tidak di belakang tombol.
  - **Perbaikan anti-clue Timbangan (laporan Faiq 16 Nov):** kotak/kardus di piringan sebelumnya menulis beratnya di tingkat F (misi dan kasus harian yang ceritanya menyebut berat). Sekarang kotak selalu "?" di semua mode; berat yang diketahui hanya ada di cerita. Pengecualian: Lab, saat pemain sendiri memilih "Tunjukkan isi". Diaudit di 9 misi dan 9 kasus harian.
  - **Jadwal Bus selesai dirancang ulang:** adegan terminal (langit, halte, bus kuning di latar bawah, `PX.scene`), Kepala Terminal bertopi biru bercerita, papan keberangkatan biru tua dengan jalur aspal bergaris kuning dan bus kecil sebagai tanda keberangkatan (garis bertitik = menit yang dicek tanpa bus), tiang merah = menit pilihan, pita merah di meja kayu (I), kalender berbingkai (E), meteran kuning untuk garis waktu. Diuji: misi F1 menit 12 salah, menit 24 "Tepat!", I, E, Harian, Lab, Aturan.
  - **6 game Geometri dirancang ulang (16 Nov)** lewat `conv.py` + `conf.py` (kerangka sama dengan Aljabar). Tempat dan tokoh: Rute Kurir = kantor kurir (motor, tumpukan paket, peta), kurir bertopi oranye; Pasang Lantai = ruangan dipasang ubin, Pak Darto; Gudang Kardus = rak kardus dan akuarium, Bu Ratna; Cetak Spanduk = percetakan spanduk, perancang berbaret; Tangga Bangunan = tembok bata, tangga bersandar, perancah, Mandor Joko; Pelabuhan = dermaga, laut, kapal, menara suar, syahbandar. Gambar diagram di papan diberi bahan per game lewat CSS atribut SVG (`.px-ge-*`): ubin krem, air biru, logo merah di kain, tangga kayu, peta laut biru, rumah abu-abu (warna dijaga sesuai keterangan "abu-abu = bangunan").
  - **5 game Data dirancang ulang (16 Nov)** lewat `conv.py` + `conf.py`. Tempat dan tokoh: Loker OSIS = ruang OSIS (loker, gantungan seragam), Bu Wina; Pentas Seni = panggung bertirai merah, Kak Dimas; Undian Doorprize = meja hadiah (kipas angin, kotak kupon, dadu, kado), Pak RT berpeci; Rapor Kelas = ruang kelas (papan tulis, bangku), Bu Sinta; Grafik Viral = ruang komputer (layar grafik, rak buku), Mbak Rara. Benda papan (`.px-da-*`): gambar baju/celana di pilihan seragam, slot panggung gelap bergaris lampu, kartu nama, kupon tiket bertakik (tetap merah/putih), bola bulat merah/biru (dibedakan dari kupon lewat `:has()` wadahnya), kotak kupon, kantong kain, kartu rapor bergaris merah, kertas tempel data, batang grafik biru/kuning.
  - **Semua 27 game sudah adegan pixel.**
  - **Ukuran layar (laporan Faiq 16 Nov: Progres, Jurnal, Temuan terpotong di kanan; Faiq memakai iPad mini 7):** app tidak lagi dikunci 480/390 px; mengikuti lebar perangkat sampai 834 px (`#root>div>div{width:100%}`). Gambar ruangan mengikuti lebar (rasio 195:50), peta desa dibatasi supaya seluruh desa muat setinggi layar, daftar game 3 kolom di layar ≥ 600 px. Diuji di 744 × 1133 dan 390 × 844.
  - **Faiq (16 Nov): masih kaku di papan Aljabar/Geo/Data, Beranda/Mini Games, dan layar non-game.** Dikerjakan bertahap. **Tahap 1 selesai: Beranda dan Mini Games.** Beranda: kotak dialog gaya RPG (biru tua bertepi emas, wajah pemandu desa `SPR.pemandu`), "Coba berikutnya" jadi gulungan kertas misi (`.px-scroll`), target harian jadi bintang pixel (`.px-star`). Mini Games: pilihan materi jadi bangunan di pulau rumput dengan papan nama kayu (`.px-signplate`); daftar game jadi papan toko kayu (`.px-shopboard`) dengan tugas di kertas, bintang pixel per tingkat, pita merah "Baru". **Berikutnya: tahap 2 layar non-game (daftar dan kartu jadi benda), tahap 3 papan Aljabar/Geo/Data disusun ulang total per materi.**
  - **8 layar non-game jadi ruangan (16 Nov):** gambar ruangan di atas (`::before` pada area gulir, `PX.alView`), latar polos tanpa pemandangan di belakang kartu, isi jadi benda khas (`#root.px-p-Nama`): Progres = ruang piala (piala emas/perak/perunggu, plakat bertepi emas); Jurnal = meja peneliti (kertas buku bergaris tepi merah); Temuan = pohon berbuah (subbab berbentuk daun); Pengaturan = panel kontrol logam; Tantangan = papan gabus (kertas kuning ditancap pin merah); Bengkel = meja kerja dengan dinding alat (label perbaikan); Cek celah = menara teropong di malam berbintang (buku log); Kasus baru = kantor pos (amplop, kertas surat bergaris).
  - **Warna disesuaikan dengan teks isi (16 Nov):** semua teks yang menyebut warna diperiksa. Koin uang Kasir Kilat jadi biru (pengenalan: "koin biru (uang)"), kotak isian Aturan biru (bantuan: "Ketuk kotak biru"), tombol "Tidak bisa ditentukan"/"Tidak mungkin" oranye (`.px-fo`, bantuan Timbangan: "tombol oranye"), potongan sisa pizza abu-abu, bangunan Rute Kurir dan perabot Pasang Lantai abu-abu. **Aturan: sebelum mengganti warna benda, cari teks yang menyebut warna itu.**
  - **Revisi Bilangan (laporan Faiq 16 Nov: masih ada bentuk prototipe):** papan tombol angka (mesin kasir, jumlah porsi, jumlah lapis, total diskon, hitungan blok Ubin, lompatan hari Jadwal Bus) jadi alat berbadan logam dengan tombol tuts (`.px-calc`); harga di struk Kasir Kilat E jadi baris tulisan bergaris putus, harga terpilih distabilo kuning; mesin lipat jadi panel mesin hijau dengan tombol kuning (`.px-machine`); kartu pecahan Bagi Pizza I jadi tiket kertas bertakik; hasil cicip Racik Resep diberi cangkir teh; pizza Bagi Pizza E berkeju seperti tingkat lain. Pizza terpotong tidak lagi berupa diagram lingkaran warna-warni: semua potongan berkeju dengan garis potong saus, potongan sisa berwarna adonan pucat, pemilik ditandai lencana nomor berwarna piring (`PZFILL`); potongan di baris piring berbentuk potongan pizza berkerak.
  - **8 game Aljabar dirancang ulang (16 Nov)** (Timbangan Balon memakai layar Timbangan). Skrip `alj.py`: papan asli tiap game (bagian `gmInPlay` tanpa bantuan, cerita, pesan, tombol berikutnya) dipindah utuh ke `shell()` dalam `<div class="px-inner">`; gaya prototipe di dalamnya dibuat pixel oleh CSS `.px-inner` (salinan kulit umum). Logika game tidak diubah.
    - Tempat dan tokoh: Dua Struk = meja kasir koperasi, Bu Sari berhijab; Meja Hajatan = tenda hajatan, Pak Harun berpeci; Martabak Topping = gerobak martabak, Bang Udin berikat kepala; Mesin Minuman = dua mesin minuman, Bu Rina; Argo Ojek = pangkalan ojek, Pak Yanto berhelm; Rekap Grosir = toko grosir, Bu Lina; Kebun Pagar = kebun berpagar bambu, Bu Wati bertopi caping; Dapur Roti = oven dapur, Bu Mira bertopi koki. Gambar: `PX.alView(nama)`.
    - Diuji: 8 game semua tingkat, Harian, Lab, Aturan, Pengenalan tanpa error; Meja Hajatan misi 1 "Tepat! 22".
    - **Benda papan digambar ulang per game (Faiq menolak versi "kotak-kotak" 16 Nov)**, lewat CSS per kelas adegan (`.px-al-*`), logika tidak diubah: Dua Struk meja kayu + struk bergerigi + kalkulator + label harga tag kuning; Meja Hajatan meja bertaplak + kursi sprite; Martabak peti kayu + tiket bergambar martabak; Mesin Minuman panel logam + kabel tebal + tombol arkade merah (emas saat dipilih) + gelas; Argo Ojek argo dasbor + jalan aspal; Rekap Grosir kertas tempel + buku besar bergaris; Kebun Pagar penggaris bambu + petak tanah; Dapur Roti nampan berisi roti + kartu resep.
    - Batas yang tersisa: tata letak papan Aljabar masih mengikuti urutan prototipe (bendanya sudah khas). Kalau Faiq ingin, tiap papan bisa ditulis ulang total seperti Bilangan.
  - **Bagi Pizza, Racik Resep, Lipat Kertas selesai dirancang ulang (16 Nov), jadi ketujuh game Bilangan sudah adegan pixel.** Kerangka bersama `shell()` di skrip pembuat (`common.py`): kepala, menu berikon, tokoh + cerita di tengah, jendela adegan `.px-view`, papan, papan tulis Aturan, pesan, lantai polos.
    - Bagi Pizza: kedai pizza (papan menu, tungku bata menyala, tumpukan kotak pizza; `PX.kedai()`), Ketua Panitia bertopi merah, pizza di meja kayu, piring per baris, kotak sisa berbentuk kardus pizza, pisau pixel. Diuji: potong 4 "Adil tanpa sisa!".
    - Racik Resep: kedai teh (rak toples, ketel mengepul di tungku, teko; `PX.kedaiteh()`), barista bercelemek, takaran teh = daun, gula = kubus, air = gelas biru, struk kertas, kupon tiket kuning. Diuji: semua ×2 "Pas! Teh untuk 8 orang".
    - Lipat Kertas: percetakan (rol kertas, mesin cetak hijau, tumpukan kertas; `PX.cetakView()`), Kepala Percetakan berkacamata, tumpukan lembar di meja kayu, catatan di kertas bergaris. Diuji: 2, 3, 2, 2 "Tepat 24 lapis".
  - **Jadwal Bus diperbaiki (laporan Faiq: "belum berubah"):** setelah pemandangan dipindah ke ujung bawah, layar main jadi biru polos. Sekarang ruang tunggu terminal: dinding abu-biru polos, jendela besar ke peron dengan halte dan bus kuning (`PX.peron()`, `.px-view`) di bawah cerita, lantai ubin polos.
  - **Huruf pixel diganti ke Tiny5** (OFL): di Pixelify Sans huruf besar B terbaca seperti G ("Gilangan"). `font-synthesis: none` supaya judul tebal tidak kabur.
  - **Bangunan khas materi (masukan Faiq 16 Nov):** Bilangan = pasar (lapak belang, papan koin, dagangan), Aljabar = bengkel (roda gigi, pintu gulung, kardus "?"), Geometri = proyek bangunan (bata, perancah, derek), Data = observatorium (kubah, antena, papan grafik). Fungsi `t.building(id, a, b)` di `PX.pen`, dipakai peta Beranda dan tombol materi Mini Games.
  - **Ikon (masukan Faiq 16 Nov):** tiap mode punya ikon pixel (Misi gulungan tugas, Harian kalender, Lab labu, Aturan papan tulis) lewat `PX.modeIcons(v)`; tiap game di Mini Games punya ikon sendiri (`PX.gameIcon(nama)`, tabel `GAMEIC`) dan tombol "Main" emas. Game yang dirancang ulang berikutnya wajib memanggil `PX.modeIcons`.
  - **Ubin selesai dirancang ulang:** gedung serbaguna berhias bendera segitiga, Pak Darto bercerita lewat balon dialog, kue di nampan logam (F), kursi biru di lantai kayu aula (I/E), blok berwarna untuk aula yang dipotong, meteran kuning untuk baris/kolom/potong, papan tulis untuk Aturan. Diuji: misi F1 3 × 4 "Pas!", tingkat I dan E, Harian, Lab, Aturan, Pengenalan.
  - **Timbangan selesai dirancang ulang:** adegan gudang (dinding papan, lantai kayu), mandor bertopi kuning bercerita lewat balon dialog, panggung timbangan (tiang logam, batang kayu, piringan bergantung rantai, papan status), beban balok besi, kardus bersolasi, balon merah bertali, rak kayu, papan tulis hijau untuk Aturan. Bagian bersama: `head()`, `menus()`, `npc()` di skrip pembuat template; CSS `.px-npc`, `.px-bubble`, `.px-stage`, `.px-shelf`, `.px-chalk`. Diuji: misi 1 seimbang dengan 9 + 9 + 3, Batal langkah, Harian, Lab, Aturan, Pengenalan, Timbangan Balon.
- **16 Nov:** **tema pixel tahap 3: benda papan 6 game Bilangan** lewat CSS per game (`#root.px-g-Nama`, kelasnya dipasang `PX.skin`; logika game tidak diubah). Timbangan: batang kayu, tiang logam, piringan logam, beban balok logam, kardus bersolasi, hadiah berpita. Ubin: kue merah muda di nampan logam. Jadwal Bus: rel jalan, penanda bus kotak. Bagi Pizza: kerak dan keju (tanpa topping, supaya jumlah topping tidak terbaca sebagai petunjuk potongan). Racik Resep: kotak takaran, air biru. Lipat Kertas: lembar berbingkai.
- **16 Nov:** **tema pixel tahap 2: kulit pixel untuk semua layar lain** (26 game + Progres, Jurnal, Temuan, Pengaturan, Tantangan, Bengkel, Cek celah, Kasus baru). Template lama tidak diubah; CSS `#root.px-skin` membaca gaya bawaan (kartu putih, tombol biru, pilihan hitam) dan menggantinya jadi bingkai gelap, tombol emas, pilihan biru tua, tab bawah slot pixel. `PX.skin(root, nama)` dipanggil di `show()`.
  - Latar: langit, awan, bukit, rumput, jalan. 6 game Bilangan punya adegan sendiri (Timbangan: lapak dan timbangan; Ubin: toko kue dan nampan; Jadwal Bus: halte dan bus; Bagi Pizza: kedai dan papan pizza; Racik Resep: dapur dan panci; Lipat Kertas: toko kertas). Game lain dan layar non-game: rumah dengan warna atap materinya.
  - Perbaikan mesin template: spasi di sekitar `{{nilai}}` di teks tidak lagi dibuang (sebelumnya "Kesempatan cicip3 / 3").
- **16 Nov:** **tema pixel B diterapkan ke app, tahap 1: Beranda, Mini Games, Kasir Kilat.** Isi, angka, dan aturan main tidak berubah.
  - Beranda: desa satu layar (rumah 4 materi, papan Tantangan, gudang Bengkel, menara Cek celah, peti Lencana). Ketuk benda, lalu tokoh berjalan ke sana dan kotak dialog bawah menampilkan rinciannya. Tanda seru di rumah materi dari "Coba berikutnya". Tombol di rumah materi membuka Mini Games langsung di materi itu.
  - Mini Games: latar rumput, tombol materi bergambar rumah, kartu game berbingkai pixel.
  - Kasir Kilat: adegan warung (dinding, jendela, pembeli, meja kasir, laci koin, lantai). Koin uang emas, bon utang merah. Semua mode (Pengenalan, Misi, Harian, Lab, Aturan) dan 3 tingkat lolos uji main.
  - Kode: CSS `.px-*` di `<style>` kedua di `<head>` (huruf Pixelify Sans OFL disisipkan); modul `PX` sebelum "Logika tiap layar" (`PX.U` gambar kecil, `PX.world()`, `PX.shop()`, `PX.house(id)`); Kasir Kilat `pxVals()` menambah nilai tampilan.
- **16 Nov:** pratinjau desain tema dibuat di `pratinjau-tema.html` (halaman terpisah, app tidak diubah). Isinya 3 tema (A, B, C), masing-masing Beranda + Kasir Kilat F Misi 1. Faiq memilih B. Rincian di bagian "Desain tema".
- **16 Nov:** kasus tempelan diperluas ke 24 game lain (semua kecuali Timbangan). Untuk game ini angka dan kunci dibuat app, Claude hanya menulis cerita. Layar `KasusBaru` kini punya pemilih materi dan game.
- **16 Nov:** kasus harian lewat prompt → JSON → validator, **tahap 1 (Ubin saja)**. Layar baru `KasusBaru` (Pengaturan → Kasus harian baru). Rincian di bagian "Kasus tempelan".
- **16 Nov:** kasus harian berangka baru (jalan pintas sebelum prompt → JSON). Tiap hari per tingkat: 1 kasus cerita dari kumpulan lama (bergilir) + 2 kasus "Angka baru" yang angkanya berganti tiap hari. Berlaku di 25 game; **Timbangan belum** (masih kumpulan lama). Rincian di bagian "Kasus harian berangka baru".
- **16 Nov:** deskripsi Mini Games diganti: Racik Resep F "Resep 4 orang, tamunya berubah", Ubin F "Tata kue di nampan tanpa sisa", Lipat Kertas I "Kertas lewat dua mesin lipat".
- **16 Nov:** perbaikan tombol Berikutnya: Martabak Topping kini membaca tingkat aktif (sebelumnya memakai nomor misi, jadi soal survei bisa muncul di papan sortir); teks tujuan soal acak yang punya kotak jawaban selalu "Jawab pertanyaan di bawah" (`FMP.nextGoal`), supaya tidak ada lagi tujuan yang tidak cocok dengan soalnya (mis. "tiang bendera" padahal ceritanya pohon).
- **16 Nov:** tiga perbaikan dari pemeriksaan Faiq. (1) Menu dan bantuan tidak lagi menjanjikan "kasus baru setiap hari" (kumpulan kasus per tingkat baru 2–6, jadi berulang); janji itu boleh kembali setelah kasus lewat prompt → JSON → validator jadi. (2) Tombol "Catat percobaan otomatis" dan "Kirim ringkasan ke Progres Harian" disembunyikan dari Pengaturan sampai fiturnya dibuat (`toggles: []`; nilai `autoLog`/`sendPH` masih tersimpan). (3) Deskripsi Bagi Pizza di Mini Games: I "Catat sisa pizza di papan", E "Berapa porsi dari sisa loyang?".
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
0a. **Tahap 2 layar non-game (berjalan).** Sudah: Temuan jadi pohon sungguhan (buah = temuan, kuncup = belum), Jurnal jadi buku catatan (pembatas warna per materi, catatan berpaku, cap tanggal), Progres jadi papan skor (ikon, balok kayu per hari, gedung materi + bilah XP, medali tingkat dan lencana). Tampilan iPad: kolom seperti layar ponsel sedikit lebih lebar di tengah, latar luar = latar layar itu yang diburamkan (tidak direntang, tidak gepeng). Pengaturan jadi panel kendali (tombol tekan berlampu, kenop, layar LCD), Tantangan jadi papan gabus berpaku, Bengkel jadi meja kerja dan rak tunggu dengan label perbaikan, Cek celah jadi buku pengamatan langit (bulan sabit = tahap tingkat), Kasus baru jadi kantor pos (perangko game, surat prompt, kartu pos kasus). Tahap 2 selesai. Revisi sesuai referensi kebun pixel Faiq (16 Nov): Temuan jadi kebun dilihat dari atas (wortel/tomat/kubis/bunga matahari per materi, tunas = belum), Progres jadi layar tas ala RPG (bilah status, tumpukan kardus per hari, petak lencana), Jurnal jadi buku petualang (ikon barang per game, cap ditolak/lolos uji). Tahap 3: susun ulang total papan Aljabar/Geometri/Data, satu materi per sesi. Aljabar sudah: papan tiap game menyatu dengan adegannya (kelas .px-scn + .px-scn-top), kotak jawaban jadi papan jalan/perangkat (.px-clip, varian kalkulator/argometer/mesin), penyusun rumus jadi papan tulis kapur (.px-rulecard), catatan aturan jadi kertas tempel (.px-rulenote). Meja Hajatan khusus: tenda (.px-hall), gerobak meja (.px-cart). Geometri dan Data sudah juga (cara yang sama). Tahap 3 selesai untuk bingkai; berikutnya bila Faiq minta: gambar ulang isi papan per game yang masih terasa prototipe, satu per satu seperti Timbangan.
0. **Faiq mencoba alur Kasus harian baru** (salin prompt → proyek Claude → tempel) di Ubin dan beberapa game lain, lalu melaporkan kasus yang ditolak atau ceritanya janggal. Timbangan masih perlu pembuat soal acak supaya ikut kasus berangka baru dan kasus tempelan.
1. **Faiq menguji game Bilangan, game Aljabar, Geometri, dan Data per tingkat, dan Mini Games 2 langkah**, lalu mengisi lembar jawaban. Perbaiki sesuai masukan.
2. **Desain tema:** 2–3 pratinjau dulu, lalu satu set warna dan huruf untuk semua layar.
3. **Cek Celah versi tes:** 2 tantangan singkat per game yang menyarankan tingkat (ditunda, disetujui Faiq 16 Nov).
4. **Tahap berikutnya:**
   - kasus harian lewat prompt → JSON → validator (tiap kasus punya `tingkat`); **prioritas**, karena kasus harian sekarang berulang dan membuat ★2 serta Tantangan terlalu mudah;
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

## Kasus harian berangka baru (16 Nov)
- Ada di modul `FMP`: `genCase(key, tingkat, hari, slot)` membuat instance game sementara, membuka misi, menekan tombol soal acak milik misi itu ("Berikutnya", "… lain", "… berikutnya") dengan `Math.random` berbenih (game + tingkat + hari + slot), lalu menyimpan `P` hasilnya sebagai kasus ber-`id` `a<hari><tingkat><slot>`, `konteks` "Angka baru n", `gen: true`.
- `FMP.wrap` menimpa `todayIdx` (1 kasus cerita `pool[hari % n]` + 2 kasus buatan, dimasukkan ke `this.H`) dan `loadCase` (berbenih, jadi soal yang sama tampil sama sepanjang hari). `applyOpen` dan `tantangan()` mengenali id buatan; Tantangan mendahulukan kasus buatan.
- Tingkat yang misinya tidak punya tombol soal acak memakai tabel `EXTRA` di `FMP`: Jadwal Bus I (pita) dan E (hari), Ubin I (aula diperluas), Bagi Pizza I (papan sisa).
- Batas: variasi beberapa pembuat soal masih sedikit (Cetak Spanduk F dan Grafik Viral F hanya 3 bentuk, Pasang Lantai E 5, Pentas Seni I 6). Kasus buatan memakai cerita pendek umum dari tombol Berikutnya, dan tidak berisi klaim; klaim hanya ada di kasus cerita.

## Kasus tempelan: prompt → JSON → validator (16 Nov, tahap 1)
- Semua di modul `FMP`: `CASES[game][tingkat]` (teks prompt per tingkat), `casePrompt` (5 kasus, konteks diacak dari 16 pilihan, 2 kasus diminta berisi klaim atau target mustahil), `BUILD[game]` (pemeriksa per game; baru `buildUbin`), `caseAdd`, `caseStored`, `caseRemove`.
- JSON dari Claude **tidak berisi kunci dan tidak berisi tujuan**. App menulis `tujuan` dari templat tetap dan menghitung sendiri: jawaban klaim (`verdict.correct`) dan apakah target mustahil (`impossible`).
- Yang ditolak: tingkat tidak cocok, angka di luar batas papan, cerita > 3 kalimat, angka kasus tidak tertulis di cerita, kata terlarang (`LARANG`: faktor, kelipatan, rumus, dst.; tanda kali untuk Ubin F), tokoh klaim tidak ada di cerita, angka sama dengan misi/kasus yang sudah ada.
- Kasus lolos disimpan di `fm.progress.cases[game]` (ikut cadangan dan Hapus semua data), dimasukkan ke `this.H` oleh `FMP.wrap`, dan ikut bergiliran sebagai kasus cerita di tab Harian (1 per hari) serta di Tantangan. Tombol Mainkan di layar `KasusBaru` membukanya langsung.
- **Game selain Ubin (jalur umum):** `genericPrompt` membuat 5 `kode` (5 huruf acak + nomor misi awal 0–2 + `k`/`n` untuk klaim). `genericCase(key, tingkat, kode)` membuat ulang soal yang sama dari kode itu lewat `genBy` (mesin yang sama dengan kasus "Angka baru"), jadi app tidak perlu menyimpan apa pun antara salin prompt dan tempel jawaban. Kalimat cerita bawaan soal dikirim ke Claude sebagai "Fakta".
- Klaim jalur umum: hanya bila soal punya kotak jawaban angka, belum punya `verdict`, dan game lolos `claimable` (simulasi `solved` → tahap `verdict`). Nilai klaim = kunci (40%) atau kunci digeser; `verdict.correct` dihitung app.
- `buildGeneric` menolak: kode tak dikenal, angka Fakta/Klaim tidak ada di cerita, angka lain di cerita, tokoh klaim tidak ada. Kasus diberi `sl: true` supaya `loadCase` berbenih.
- Jalur khusus (Claude memilih angka) baru ada untuk Ubin: `CASES.Ubin` + `buildUbin`. Game lain bisa dinaikkan ke jalur khusus dengan menambah `CASES[game]` dan `BUILD[game]`.
- Timbangan belum bisa: tidak punya tombol soal acak, jadi `genBy` mengembalikan null.
- `proyek-claude.md` berisi instruksi proyek dan konteks proyek untuk proyek Claude milik Faiq. Kalau batas angka, kata terlarang, atau bentuk JSON di `FMP` berubah, perbarui file itu juga, dan tambah bagian game baru di sana.

## Desain tema: bahan untuk sesi berikutnya (16 Nov)
- Faiq ingin Claude bekerja sebagai app designer. Referensinya (dikirim sebagai gambar di chat, tidak tersimpan di repo): pixel art hangat bergaya desa dan kebun (hijau rumput, cokelat tanah, biru air, garis tepi gelap), ikon benda pixel (koin, makanan, peti, ransel), tombol kayu tebal.
- **Keputusan Faiq 16 Nov: tema B (Desa pixel).** Tambahan dari Faiq: semua layar memakai **latar gambar pixel**, **jangan latar cokelat/krem** (bikin mengantuk); app ini mini games interaktif, jadi tampilannya harus terasa hidup. Di pratinjau: latar langit, awan, bukit, rumput (`bgURL`), kartu putih bergaris gelap 2px, tombol utama kuning emas. **Belum diterapkan ke `index.html`**; menunggu Faiq menyetujui usulan penerapan.
- **Arahan Faiq berikutnya (16 Nov): jangan kaku mengikuti tata letak prototipe.** Rancang seperti game pixel sungguhan; **desain bebas diubah, isi (teks, angka, aturan main) tidak boleh berubah.** Pratinjau dirancang ulang: Beranda = satu layar desa penuh (papan nama pemain, target, 4 bangunan materi, papan Tantangan, gudang Bengkel, menara Cek celah, peti Lencana, tokoh pemain yang berjalan ke bangunan yang diketuk, kotak dialog di bawah berisi rincian dan tombol, tab bawah berbentuk slot); Kasir Kilat = adegan warung dari balik meja kasir (pembeli, kotak cerita, nampan logam di meja, laci koin besar 1–9, tombol Serahkan emas). Tema A dan C dibuang dari halaman pratinjau.
- Usulan awal (sebelum Faiq memilih): 3 pratinjau, masing-masing Beranda + satu layar Kasir Kilat, sebagai halaman terpisah tanpa mengubah app.
  - A. Sentuhan pixel: tata letak sekarang + warna hangat, huruf pixel untuk judul, ikon benda pixel.
  - B. Desa pixel: Beranda dan Mini Games jadi peta desa, tiap game sebuah bangunan; layar game tetap sederhana. (Saran Claude.)
  - C. Pixel penuh: semua tombol, panel, dan benda di papan bergaya pixel dan kayu.
- **Pratinjau sudah ada** di `pratinjau-tema.html` (tombol A/B/C di atas). Pixel art digambar lewat kode di file itu (`SPR` untuk ikon, `mapURL` untuk peta desa). Huruf judul dan label di app: Fredoka (bulat, halus, OFL). Huruf pixel (Pixelify, lalu Tiny5) dihapus: Faiq bilang terlalu banyak huruf pixel bikin pusing.
- Gambar referensi Faiq diterima 16 Nov; pratinjau disesuaikan: rumput kotak-kotak cerah, pohon bulat besar, sungai berbuih dengan dermaga, pagar, tunggul, batu, bunga, koin berkilau di semua tema, dan bingkai kayu (panel, tombol, papan nama) lewat `border-image`.
- Temuan saat membuat pratinjau: angka huruf pixel mudah salah baca (5 mirip S, 2 mirip 8, 7 mirip 1). Jadi **angka dan cerita soal selalu memakai huruf biasa**, di tema mana pun.
- Setelah Faiq memilih: terapkan ke `index.html` sebagai satu set warna dan huruf; `pratinjau-tema.html` boleh dihapus sesudahnya.
- Batasan: pixel art digambar sendiri, tidak menyalin gambar referensi (sebagian dari game dan paket aset orang lain). Aturan "tampilan minimalis, elemen kecil" tetap berlaku; angka dan teks soal harus tetap mudah dibaca di HP.

## Catatan
- Rotasi kasus harian memakai hari UTC, jadi berganti pukul 07.00 WIB.
