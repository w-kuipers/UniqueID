from secrets import choice
from typing import Optional

from ..constants import ALPHANUMERIC, URLSAFE


def urlsafe(length: int = 6, prefix: Optional[str] = None):
    "Generate a random string of letters and numbers and unreserved url characters"

    charset = ALPHANUMERIC + URLSAFE

    generated = "".join(choice(charset) for _ in range(length))

    if not prefix == None:
        generated = prefix + generated

    return generated
