from monocliche.model import AbstractAction


class Card:
    def __init__(self, title: str, description: str, action: AbstractAction):
        self.title = title
        self.description = description
        self.action = action
