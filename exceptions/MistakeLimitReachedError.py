class MistakeLimitReachedError(Exception):
    """
    
    """
    def __init__(self, correct_answer):
        super(MistakeLimitReachedError, self).__init__(f"Maximum mistakes reached. The correct answer was: {correct_answer}")
        self.correct_answer = correct_answer
