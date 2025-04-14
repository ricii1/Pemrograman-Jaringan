# Socket Programming- [Socket Programming](#socket-programming)
## Daftar Isi
- [Socket Programming- Socket Programming](#socket-programming--socket-programming)
  - [Daftar Isi](#daftar-isi)
  - [Port Number](#port-number)
  - [Tipe Socket](#tipe-socket)
    - [UDP](#udp)
    - [TCP](#tcp)
  - [Tipe Alamat](#tipe-alamat)
    - [AF\_UNIX](#af_unix)
    - [AF\_INET](#af_inet)
    - [AF\_INET6](#af_inet6)
  - [Konsep Klien - Server](#konsep-klien---server)
    - [Host](#host)
    - [Port](#port)
    - [Socket](#socket)
  - [Kesalahan yang sering terjadi](#kesalahan-yang-sering-terjadi)

## Port Number
- Diatur oleh Internet Assigned Numbers Authority (IANA)
- Tiga range
  - Well-Known Ports (0 - 1023)
  - Registered Ports (1024 - 49151)
  - Free Ports (49152 - 65535)
## Tipe Socket
### UDP 
menggunakan flag SOCK_DGRAM
### TCP
menggunakan flag SOCK_STREAM
## Tipe Alamat
### AF_UNIX
Socket antara dua proses yang berjalan dan berkomunikasi dalam satu host
### AF_INET
Socket antara dua proses yang bisa berjalan pada host yang berbeda menggunakan IPv4 (bisa juga pada host yang sama)
### AF_INET6
Sama dengan AF_INET tapi menggunakan IPv6
## Konsep Klien - Server
### Host
Host adalah sebutan untuk server dan client
### Port
Semua klien bisa terkoneksi ke 1 port server yang sama. Server hanya memiliki 1 port yang akan dilakukan multiplexing (didistribusikan). 
### Socket
Semua klien terkoneksi ke socket yang berbeda di server. Satu socket per koneksi. 
## Kesalahan yang sering terjadi
- Terdapat pesan kesalahan: _Address already in use_. 
- Hal ini disebabkan port sudah digunakan oleh service atau proses lain. 
- Solusinya adalah menambah flag socket.SO_REUSEADDR pada socket server.
