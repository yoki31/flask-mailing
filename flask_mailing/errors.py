class ConnectionErrors(Exception):
    def __init__(self, expression:str) -> None:
        self.expression:str = expression


class WrongFile(Exception):
    def __init__(self, expression:str) -> None:
        self.expression:str = expression


class PydanticClassRequired(Exception):
    def __init__(self, expression:str) -> None:
        self.expression:str = expression


class TemplateFolderDoesNotExist(Exception):
    def __init__(self, expression:str) -> None:
        self.expression:str = expression
