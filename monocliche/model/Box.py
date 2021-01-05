from uuid import uuid4


class Box:

    def __init__(self, name: str):
        self.__id = uuid4()
        self.name = name

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not issubclass(type(other), Box):
            return False

        return self.__id == other.__id
