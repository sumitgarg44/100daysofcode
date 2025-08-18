"""Creates Question object"""


class Question:
    # pylint: disable=too-few-public-methods
    """Question class: Accepts a question and answer!"""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
