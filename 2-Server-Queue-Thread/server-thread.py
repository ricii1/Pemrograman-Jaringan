#!/usr/bin/env python
# Gabungan Server dan Client dengan Penjelasan Lengkap
# Sumber server: http://ilab.cs.byu.edu/python/threadingmodule.html

import select       # Untuk monitoring socket dan stdin
import socket       # Untuk komunikasi jaringan
import sys          # Untuk akses ke stdin dan argv
import threading    # Untuk menjalankan banyak client secara paralel (multithreading)
import time         # Untuk jeda waktu di client


# =============================
# ==== KELAS SERVER SOCKET ====
# =============================
class Server:
    def __init__(self):
        self.host = '127.0.0.1'      # Jalankan di localhost
        self.port = 5000             # Port yang digunakan
        self.backlog = 5             # Jumlah maksimum antrean koneksi
        self.size = 1024             # Ukuran buffer
        self.server = None           # Objek socket utama
        self.threads = []            # Menyimpan semua thread client

    def open_socket(self):        
        # Membuat socket TCP (IPv4)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Mengatur agar port bisa langsung digunakan ulang saat server restart
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind ke alamat host dan port
        self.server.bind((self.host, self.port))

        # Mulai menerima koneksi dengan backlog 5
        self.server.listen(5)

    def run(self):
        # Jalankan server
        self.open_socket()
        print(f"Server berjalan di {self.host}:{self.port}")
        print("Tekan Enter untuk menghentikan server...\n")

        input_list = [self.server, sys.stdin]
        running = True

        while running:
            # Tunggu sampai ada input dari socket atau terminal
            input_ready, _, _ = select.select(input_list, [], [])

            for s in input_ready:
                if s == self.server:
                    # Jika ada client yang connect
                    client_socket, client_address = self.server.accept()
                    print(f"Client terhubung: {client_address}")
                    c = Client(client_socket, client_address)
                    c.start()  # Jalankan thread client
                    self.threads.append(c)

                elif s == sys.stdin:
                    # Jika user tekan Enter
                    _ = sys.stdin.readline()
                    running = False

        # Tutup socket server
        self.server.close()
        print("Menutup semua koneksi...")

        # Tunggu semua thread selesai
        for c in self.threads:
            c.join()

        print("Server dihentikan.")


# =============================
# ==== KELAS CLIENT THREAD ====
# =============================
class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client         # Socket client
        self.address = address       # Alamat client
        self.size = 1024             # Ukuran buffer

    def run(self):
        running = True
        while running:
            try:
                # Terima data dari client
                data = self.client.recv(self.size)
                print('Diterima dari', self.address, ':', data.decode())

                if data:
                    # Kirim balik ke client (echo)
                    self.client.send(data)
                else:
                    # Tidak ada data, client tutup koneksi
                    self.client.close()
                    running = False
            except ConnectionResetError:
                print('Koneksi terputus oleh client:', self.address)
                running = False


# ==========================
# ==== FUNGSI CLIENT ====
# ==========================
def run_client(messages):
    try:
        for msg in messages:
            # Buat socket client
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Hubungkan ke server
            host = socket.gethostname()
            port = 5000
            client.connect((host, port))

            # Kirim data ke server
            print(f"[CLIENT] Mengirim: {msg}")
            client.send(bytes(msg, encoding='utf-8'))

            # Terima balasan dari server
            data = client.recv(1024)
            print(f"[CLIENT] Diterima kembali: {data.decode()}")

            # Tutup koneksi
            client.close()
            time.sleep(0.5)  # Delay sedikit antara pengiriman
    except Exception as e:
        print("Terjadi kesalahan di client:", e)


# ==========================
# ==== ENTRY POINT ====
# ==========================
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "client":
        # Jalankan sebagai client, argumen berikutnya adalah pesan
        run_client(sys.argv[2:])
    else:
        # Jalankan sebagai server
        server = Server()
        server.run()
