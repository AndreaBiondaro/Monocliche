from monocliche.model import AbstractAction


class Card:
    def __init__(self, title: str, description: str, action: AbstractAction):
        self._title = title
        self._description = description
        self._action = action

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action: AbstractAction):
        return self._action
