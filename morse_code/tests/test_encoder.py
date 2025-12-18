import unittest

from morse_code.encoder import text_to_morse


class TestTextToMorse(unittest.TestCase):

    def test_basic_word(self):
        self.assertEqual(text_to_morse("SOS"), "... --- ...")

    def test_multiple_words(self):
        self.assertEqual(
            text_to_morse("Hello World"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        )

    def test_lowercase_input(self):
        self.assertEqual(text_to_morse("sos"), "... --- ...")

    def test_unknown_character(self):
        self.assertEqual(text_to_morse("HI!"), ".... .. ?")

    def test_empty_string(self):
        self.assertEqual(text_to_morse(""), "")


if __name__ == "__main__":
    unittest.main()
