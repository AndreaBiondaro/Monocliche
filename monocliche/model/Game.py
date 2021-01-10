from uuid import uuid4

from monocliche.LinkedPlayers import LinkedPlayers
from monocliche.Uitls import Utils
from monocliche.model.Board import Board
from monocliche.model.Dice import Dice
from monocliche.model.DiceRollResult import DiceRollResult
from monocliche.model.Player import Player
from monocliche.model.enum.GameStatus import GameStatus


class Game:

    def __init__(self):
        self.__id = uuid4()
        # Code used by players who want to connect to this games. Id is not used because it is too long to write
        self.code = Utils.random_string(6)
        self.status = GameStatus.NEW
        self.board: Board = Board()
        self.players: LinkedPlayers = LinkedPlayers()
        self.dice = Dice()
        self.dice_roll_result = DiceRollResult()

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False

        return self.__id == other.__id

    def add_player(self, player_name: str) -> Player:
        """Add a new player to the game."""

        if self.status == GameStatus.RUNNING:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("It is not possible to participate in a game that has already started")
        elif self.status == GameStatus.COMPLETED:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("It is not possible to participate in a match that has already ended")

        if self.players is None:
            self.players = LinkedPlayers()

        new_player = Player(player_name)
        self.players.add(new_player)

        return new_player

    def remove_player(self, player_to_remove: Player) -> None:
        """Remove a player from the game."""

        if self.status == GameStatus.RUNNING:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("It is not possible to leave a game that has already started")

        start_len = self.players.size

        self.players.remove(player_to_remove)

        if start_len == self.players.size:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("Error removing player from game")

    def passes_turn(self) -> Player:
        """Manages the passing of the turn to the next player."""
        self.players.current_player.my_turn = False

        next_player = self.players.next_player()

        next_player.my_turn = True

        return next_player

    def start_game(self) -> None:
        """Update the game status, and initialize the card decks and board boxes"""

        self.board.initialize_board()

        self.status = GameStatus.RUNNING

    def check_game_is_over(self) -> bool:
        """Check if all but one of the players are bankrupt, if so then the remaining player is the winner."""

        # TODO : implements

        # TODO : to be removed because it is not needed
        return self.status == GameStatus.COMPLETED

    def complete_match(self) -> Player:
        """Forces the match to complete and returns the player who is richer."""

        # TODO : implements

        self.status = GameStatus.COMPLETED

        return self.players.iterate()[0]
