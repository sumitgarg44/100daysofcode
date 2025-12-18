import unittest

from morse_code.decoder import morse_to_text


class TestTextToMorse(unittest.TestCase):

    def test_basic_word(self):
        self.assertEqual(morse_to_text("... --- ..."), "SOS")

    def test_multiple_words(self):
        self.assertEqual(
            morse_to_text(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."), "HELLO WORLD"
        )

    def test_unknown_character(self):
        self.assertEqual(morse_to_text(".... .. ?"), "HI?")

    def test_empty_string(self):
        self.assertEqual(morse_to_text(""), "")


if __name__ == "__main__":
    unittest.main()
