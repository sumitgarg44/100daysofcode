"""Morse decoder utility"""

from .constants import MORSE_CODE_DICT

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def morse_to_text(morse: str) -> str:
    """
    Converts Morse code into plain text

    Args:
        morse (str): Input Morse code to decode

    Returns:
        str: Decoded text
    """

    if not isinstance(morse, str):
        raise TypeError("text must be a string")

    if morse:
        return " ".join(
            "".join(
                REVERSE_MORSE_CODE_DICT.get(symbol, "?")
                for symbol in code.split(sep=" ")
            )
            for code in morse.split(sep="   ")
        )
    return ""
