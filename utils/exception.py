class HelloClientError(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)


class HelloServerError(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
