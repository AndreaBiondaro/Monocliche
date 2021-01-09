from random import shuffle

from monocliche.model import Deck, Card


class DeckService:

    def shuffle_cards(self, deck: Deck) -> None:
        shuffle(deck.cards)

    def draw_card(self, deck: Deck) -> Card:
        """
        Draw the top card from the input deck. The drawn card is moved under the deck (bottom of the list).
        """
        card = deck.cards.pop(0)
        deck.cards.append(card)
        return card
