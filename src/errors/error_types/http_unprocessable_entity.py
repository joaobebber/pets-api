class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

        self.status_code = 422
        self.name = "Unprocessable Entity"
        self.message = message
