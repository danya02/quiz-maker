#!/usr/bin/python3

class Question:
    def __init__(self, question: str = None, answer: str = None, maxpoints: float = None):
        """Base class for Questions."""
        self.question = question
        self.answer = answer
        self.maximum_points = maxpoints
        if question is not None:
            self.question = question
        if answer is not None:
            self.answer = answer
        if maxpoints is not None:
            self.maximum_points = maxpoints

    def __str__(self):
        return str(self.question)

    def test(self, answer) -> float:
        """Grade the answer to this question."""
        return float(self.answer == answer) * self.maximum_points

    def __eq__(self, other):
        return bool(self.test(other))

    def __ne__(self, other):
        return not bool(self.test(other))


class YesNoQuestion(Question):
    def __init__(self, question: str = None, answer: str = None, points: float = None, yes: list = None,
                 no: list = None):
        """
        A question with a yes/no answer.
        :param question: The string of the question
        :param answer: The correct answer.
        :param points: This many points are awarded for correct answer.
        :param yes: What inputs are accepted as 'yes' answers.
        :param no: What inputs are accepted as 'no' answers.
        """
        super().__init__(question, answer, points)
        if no is None:
            no = [False, "N", "0", "F", "-"]
        if yes is None:
            yes = [True, "Y", "1", "T", "X"]
        self.yes = yes
        self.no = no

    def test(self, answer: str) -> float:
        """Grade the answer to this question."""
        if self.answer:
            if answer in self.yes:
                return self.maximum_points
        else:
            if answer in self.no:
                return self.maximum_points
        return 0.0
