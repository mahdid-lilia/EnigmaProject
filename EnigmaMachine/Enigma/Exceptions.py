class PriorityExecption(Exception):
    def __init__(self, message):
        super().__init__(message)


class IncorrectMessageException(Exception):
    def __init__(self, message):
        super().__init__(message)
