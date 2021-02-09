from random import shuffle

from monocliche.src import Card


class Deck:

    def __init__(self, cards=None):
        self.cards: list[Card] = cards

    def shuffle(self):
        shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Draw the top card from the input deck. The drawn card is moved under the deck (bottom of the list).
        """

        card = self.cards.pop(0)
        self.cards.append(card)
        return card
