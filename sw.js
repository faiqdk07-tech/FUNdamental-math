/* Penyimpan app Fundamental Math (Faiq 20 Nov).
   Halaman dibuka dari salinan di perangkat (cepat, bisa tanpa internet); versi terbaru diunduh diam-diam
   dan dipakai pada pembukaan berikutnya. Progres pemain (localStorage) tidak disentuh. */
const CACHE = 'fm-app';
const PAGE = './';

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.add(PAGE)).catch(() => {}));
});
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));

self.addEventListener('fetch', e => {
  if (e.request.mode !== 'navigate') return; // hanya halaman app; huruf dan lainnya lewat jaringan biasa
  // minta versi terbaru dari server (alamat halaman, bukan objek permintaan navigasi yang tidak boleh diubah)
  const fresh = caches.open(CACHE).then(c => fetch(new URL(PAGE, self.registration.scope), { cache: 'no-cache' }).then(r => { if (r.ok) c.put(PAGE, r.clone()); return r; }));
  e.waitUntil(fresh.catch(() => {}));
  e.respondWith(caches.open(CACHE).then(c => c.match(PAGE)).then(hit => hit || fresh));
});
