from secrets import choice
from typing import Optional

from ..constants import NUMERIC


def numeric(length: int = 6, prefix: Optional[int] = None) -> int:
    "Generate a random number"

    charset = NUMERIC
    generated = "".join(choice(charset) for _ in range(length))

    if not isinstance(prefix, int):
        if not prefix == None:
            raise TypeError("Prefix should be of type int")
    
    if not prefix == None:
        generated = f"{prefix}{generated:}"

    return int(generated)
