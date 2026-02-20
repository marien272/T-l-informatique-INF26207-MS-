import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12345
NONCE_SIZE = 16
HASH_SIZE = 32

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(65535)
        print(f"Recu {len(data)} octets de {addr}")

        body, hash_recu = data.rsplit(b"\x00", 1)
        nonce  = body[:NONCE_SIZE]
        message = body[NONCE_SIZE:]

        calc = hashlib.sha256(nonce + message).digest()

        if calc == hash_recu:
            print(f"Hash valide  | Message : {message.decode('utf-8', errors='replace')}")
            s.sendto(b"Message et hachage valides", addr)
        else:
            print("Hash invalide message corrompu ou modifie")
            s.sendto(b"Erreur de hachage", addr)