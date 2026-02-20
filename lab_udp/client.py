import socket
import hashlib
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12345

msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

h = hashlib.sha256(msg).hexdigest()         # str 64 caractères hex
payload = msg + b"\x00" + h.encode("ascii") # bytes

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))
    data, _ = s.recvfrom(64)
    print("Réponse:", data.decode("utf-8", errors="replace"))