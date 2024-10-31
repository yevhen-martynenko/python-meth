class MistakeLimitReachedError(Exception):
    """
    Exception raised when the number of allowed mistakes is reached.

    Attributes:
        correct_answer (int | float): The correct answer to the problem.
    """

    def __init__(self, correct_answer):
        super().__init__(f"Maximum mistakes reached. The correct answer was: {correct_answer}")
        self.correct_answer = correct_answer

