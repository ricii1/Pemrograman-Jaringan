#!/usr/bin/env python
# client.py

import sys       # Untuk mengambil argumen dari command line
import socket    # Untuk menggunakan koneksi socket (TCP/IP)

# Fungsi utama yang menerima list `elements` (argumen yang akan dikirim ke server)
def main(elements):
    try:
        # Iterasi setiap elemen dalam list
        for e in elements:
            # Membuat objek socket
            # AF_INET = IPv4, SOCK_STREAM = TCP
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Mendapatkan nama host lokal (alamat server)
            # Catatan: jika server ada di mesin lain, ganti ini dengan IP server (misalnya: '192.168.1.100')
            host = socket.gethostname()

            # Menghubungkan ke server di host dan port 5001
            client.connect((host, 5001))

            # Mengirim data ke server (harus diubah menjadi bytes, encoding UTF-8)
            client.send(bytes(e, encoding='utf-8'))

            # Menghentikan pengiriman dan penerimaan data
            client.shutdown(socket.SHUT_RDWR)

            # Menutup koneksi socket
            client.close()
    
    # Menangani semua jenis error saat koneksi, pengiriman, dll.
    except Exception as msg:
        print(msg)


# Eksekusi fungsi utama jika file dijalankan langsung
if __name__ == "__main__":
    # Ambil argumen dari command line (sys.argv[0] adalah nama file, jadi di-skip)
    main(sys.argv[1:])
