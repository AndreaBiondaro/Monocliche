from uuid import uuid4

from monocliche.model import Board
from monocliche.model import Player
from monocliche.model.Dice import Dice
from monocliche.model.DiceRollResult import DiceRollResult


class Game:

    def __init__(self, board: Board = None, players: list[Player] = None):
        self.__id = uuid4()
        self.completed = False
        self.board: Board = board
        self.players: list[Player] = players
        self.current_player_turn: Player = None
        self.dice = Dice()
        self.dice_roll_result = DiceRollResult()

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False

        return self.__id == other.__id
