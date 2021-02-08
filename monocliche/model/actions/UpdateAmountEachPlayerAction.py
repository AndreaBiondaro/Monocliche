from monocliche.model.AbstractAction import AbstractAction


class UpdateAmountEachPlayerAction(AbstractAction):
    """
    This class represents an action where the budget of all players is updated.
    """

    def __init__(self, amount):
        self.__amount = amount

    def execute(self, game):
        current_player = game.players.current_player

        counter = 0
        for player in game.players.iterate():
            if player != current_player and not player.bankrupt:
                if not player.update_budget(-self.__amount):
                    # TODO : Need to create a system to keep track of players who cannot pay,
                    #  so that you can inform them that they have to pay.
                    # Think of an Observable that keeps track of the player and the cost to pay ??
                    continue
                counter += 1

        # Even if the player fails to pay it is not a problem because the bank pays them
        if not current_player.update_budget(counter * self.__amount):
            # TODO : Keep track that the player fails to pay that amount.
            pass
