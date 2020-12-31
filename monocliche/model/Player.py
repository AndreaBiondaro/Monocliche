import uuid


class Player:
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = None
        self.budget = 0
        self.properties = []
        self.in_jail = False
        self.my_turn = False
        self.position = 0
        self.prison_release_card = False
        self.exchanges = []

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False

        return self.id == other.id
