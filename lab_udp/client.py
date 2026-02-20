import socket
import hashlib

def lire_fichier():
    p = Path("data/message.txt")

    # Lecture en mode texte
    s = p.read_text(encoding="utf-8")
    print("=== Partie 2 : Fichiers texte & encodage ===")
    print(f"Mode texte  → type={type(s)}, len={len(s)}")
    print(s)

    # Lecture en mode binaire
    b = p.read_bytes()
    print(f"Mode binaire → type={type(b)}, len={len(b)}")
    print(f"Premiers octets : {b[:20]}")

    # Conversion explicite
    b2 = s.encode("utf-8")
    s2 = b.decode("utf-8")
    print(f"str→bytes : len={len(b2)}, type={type(b2)}")
    print(f"bytes→str : type={type(s2)}")
    print()

    return b2 
