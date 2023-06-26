
from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # gera length bytes aleatorios
    tb: bytes = token_bytes(length)
    # converte esses bytes em uma cadeia de bits e a devolve
    return int.from_bytes(tb, "big")

