from secrets import token_bytes
from typing import Tuple


def random_key(lenght: int) -> int:
    tb: bytes = token_bytes(lenght)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes( (decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == '__main__':
    s = "Строка"
    k1, k2 = encrypt(s)
    d = decrypt(k1, k2)
    print(f"{s} vs {d}")
    print(f"keys: {k1}, {k2}")
