import socket

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(65535)
        print(f"Reçu {len(data)} octets de {addr}")
        print(f"Message : {data.decode('utf-8', errors='replace')}")
        s.sendto(b"Message recu", addr)