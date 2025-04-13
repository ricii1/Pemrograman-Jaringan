#!/usr/bin/env python
# Gabungan Client TCP Socket dengan Penjelasan

import sys          # Untuk membaca argumen dari command line
import socket       # Untuk komunikasi jaringan (TCP socket)
import time         # Untuk memberi jeda (delay) antar pengiriman data


def main(elements):
    """
    Fungsi utama client.
    Menerima list `elements` sebagai pesan yang akan dikirim ke server secara berurutan.
    """
    try:
        for e in elements:
            # Buat objek socket
            # AF_INET = IPv4, SOCK_STREAM = TCP
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Hubungkan ke server yang berjalan di localhost, port 5000
            client.connect(('127.0.0.1', 5000))

            # Kirim data ke server dalam bentuk bytes dengan encoding UTF-8
            print(f"[CLIENT] Mengirim: {e}")
            client.send(bytes(e, encoding='utf-8'))

            # Tutup jalur komunikasi (shutdown dan close)
            client.shutdown(socket.SHUT_RDWR)  # Menutup koneksi dari sisi client (read & write)
            client.close()

            # Delay 1 detik sebelum mengirim data berikutnya (opsional)
            time.sleep(1)

    except Exception as msg:
        # Tangani error apapun yang terjadi saat membuat atau menggunakan koneksi
        print(f"[CLIENT] Terjadi kesalahan: {msg}")


# Fungsi akan dijalankan jika file ini langsung dieksekusi sebagai skrip
if __name__ == "__main__":
    # Ambil semua argumen setelah nama file (sys.argv[1:])
    # Misalnya: python client.py halo dunia
    # -> sys.argv = ['client.py', 'halo', 'dunia']
    main(sys.argv[1:])
