"""Morse code encoder utility"""

from .constants import MORSE_CODE_DICT


def text_to_morse(text: str) -> str:
    """
    Converts plain text into Morse code

    Output Rules:
    - Letters separated by single space
    - Words separated by three spaces
    - Unknown characters replaced with "?"

    Args:
        text (str): Input text to convert

    Returns:
        str: Morse encoded string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return "   ".join(
        " ".join(MORSE_CODE_DICT.get(char, "?") for char in word.upper())
        for word in text.split()
    )
