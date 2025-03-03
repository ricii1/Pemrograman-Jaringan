import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Membuat socket bertipe TCP
socket_client.connect(('localhost', 5000)) # Melakukan koneksi ke server dengan IP localhost dan port 5000

# Di bawah ini mengirim data ke servers
# Data dikirim dalam bentuk bytes, maka perlu di encode dengan flag b
# Data yang dikirim adalah string 'Hello, world!'
socket_client.send(b'Hello, world!') 
# Menerima data dari server sebanyak 65535 bytes
data = socket_client.recv(65535)
print('Received from server:', data.decode()) # Decode bytes menjadi string dan print

socket_client.close() # Menutup koneksi ke server