#!/usr/bin/env python
# server.py

# ===== Import Module =====
import socket            # Untuk membuat server socket
import select            # Untuk menunggu event dari socket (non-blocking)
import queue             # Untuk antrian tugas (thread-safe queue)
from threading import Thread  # Untuk multi-threading
from time import sleep   # Untuk delay simulasi proses
from random import randint     # Untuk memberikan waktu delay random
import sys               # Untuk akses ke stdout (output terminal)


# ===== Kelas untuk Thread Pemrosesan Data =====
class ProcessThread(Thread):
    """
    Thread yang berjalan paralel untuk memproses data yang diterima dari client.
    Menggunakan queue untuk menerima data dari thread utama (server).
    """

    def __init__(self):
        Thread.__init__(self)
        self.running = True              # Flag untuk menghentikan thread
        self.q = queue.Queue()           # Queue thread-safe untuk menampung data dari client

    def add(self, data):
        """
        Fungsi untuk menambahkan data ke dalam queue.
        Dipanggil dari thread utama.
        """
        self.q.put(data)

    def stop(self):
        """
        Fungsi untuk menghentikan thread.
        """
        self.running = False

    def run(self):
        """
        Fungsi utama yang dijalankan saat thread dimulai.
        Ambil data dari queue dan proses.
        """
        q = self.q
        while self.running:
            try:
                # Mengambil data dari queue (maksimal tunggu 1 detik)
                value = q.get(block=True, timeout=1)
                process(value)  # Proses data
            except queue.Empty:
                # Jika tidak ada data dalam 1 detik, print titik sebagai heartbeat
                sys.stdout.write('.')
                sys.stdout.flush()

        # Jika thread dihentikan, namun masih ada data tersisa di queue, tampilkan
        if not q.empty():
            print("Elements left in the queue:")
            while not q.empty():
                print(q.get())


# ===== Mulai Thread Pemroses Data =====
t = ProcessThread()
t.start()


# ===== Fungsi untuk Memproses Data dari Client =====
def process(value):
    """
    Fungsi ini dipanggil oleh thread ProcessThread untuk memproses data.
    Di sini hanya print data dan delay beberapa detik untuk simulasi.
    """
    print(value)
    sleep(randint(1, 5))  # Simulasi waktu proses antara 1–5 detik


# ===== Fungsi Utama Server =====
def main():
    s = socket.socket()             # Membuat socket object (default: IPv4 + TCP)
    host = socket.gethostname()     # Mendapatkan nama host lokal
    port = 5001                     # Port yang digunakan untuk listen koneksi
    s.bind((host, port))            # Bind socket ke host dan port
    print("Listening on port {p}...".format(p=port))

    s.listen(5)  # Maksimal 5 koneksi dalam antrean
    while True:
        try:
            # Menerima koneksi dari client
            client, address = s.accept()

            # Gunakan select untuk menunggu apakah ada data dari client (dalam 2 detik)
            ready = select.select([client, ], [], [], 2)
            if ready[0]:
                data = client.recv(4096)  # Menerima data sampai 4096 byte
                t.add(data)               # Kirim data ke thread pemroses
        except KeyboardInterrupt:
            # Jika user menekan Ctrl+C, keluar dari loop
            print("Stop.")
            break
        except socket.error:
            # Jika terjadi error pada socket
            print("Socket error!")
            break

    cleanup()


# ===== Fungsi Cleanup untuk Menutup Thread dengan Benar =====
def cleanup():
    t.stop()    # Set flag running=False
    t.join()    # Tunggu thread selesai sebelum keluar


# ===== Entry Point =====
if __name__ == "__main__":
    main()
