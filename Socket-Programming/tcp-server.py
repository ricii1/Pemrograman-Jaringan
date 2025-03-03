import socket, sys

'''
AF_UNIX is for two process which that communicate on the same host.
AF_INET is the address family for IPv4. 
AF_INET6 is the address family for IPv6.

SOCK_STREAM is the socket type for TCP.
Meanwhile, SOCK_DGRAM is the socket type for UDP.
'''
# Membuat socket server bertipe TCP dengan alamat IPv4 
# dan bisa berjalan pada host yang sama atau berbeda
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('localhost', 5000)) # Server dikonfigurasi pada alamat IP 127.0.0.1
socket_server.listen(1) # Mendengarkan koneksi klien yang masuk. Params: jumlah antrian koneksi klien

try: # Menjaga server tetap berjalan hingga terjadi KeyboardInterrupt
    while True:
        client_socket, client_address = socket_server.accept() # Menerima koneksi dari klien.
        # Client_socket adalah socket baru yang digunakan untuk berkomunikasi dengan klien
        # Client_address adalah alamat dari klien
        print('Connection from:', client_address)
        data = client_socket.recv(65535) # Menerima data dari klien sebesar 65535 bytes
        client_socket.send(data) # Mengirim kembali data ke klien
        print('Data received from client:', data.decode()) # Decode bytes menjadi string
        client_socket.close() # Tutup koneksi dengan klien
except KeyboardInterrupt:
    print('Server shutting down...')
    # Tutup socket server bila ada KeyboardInterrupt
    socket_server.close()
    sys.exit(0)