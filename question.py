#!/usr/bin/python3

class Question:
    def __init__(self):
        """Base class for Questions."""
        self.question = ""
        self.answer = None

    def __str__(self):
        return str(self.question)

    def test(self, answer):
        return self.answer == answer

    def __eq__(self, other):
        return self.test(other)

    def __ne__(self, other):
        return not self.test(other)
