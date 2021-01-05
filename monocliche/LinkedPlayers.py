from typing import Any

from monocliche.model import Player


class Node:

    def __init__(self, data: Player, next: Any = None, prev: Any = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedPlayers:
    """
    Personalized implementation of a circular linked list.
    The purpose is to manage the player list, to keep track of the player of the current turn
    and to calculate the player of the next turn.
    """

    def __init__(self):
        self.__last = None
        self.__current_node = None
        # It keeps track of where the last iteration stopped
        self.__temp_iterator = None
        self.size = 0

    @property
    def current_player(self) -> Player:
        """
        Returns the player of the current turn.
        """
        if self.__current_node is not None:
            return self.__current_node.data
        else:
            return None

    @property
    def first_player(self) -> Player:
        """
        Returns the first player on the list.
        """
        if self.__last is not None and self.__last.next is not None:
            if self.__current_node is None:
                self.__current_node = self.__last.next

            return self.__last.next.data
        else:
            return None

    def add(self, player: Player):
        """
        Add the input player to the list.
        """
        node = Node(player)

        if self.__last is None:
            self.__last = node
            node.next = self.__last
        else:
            head = self.__last.next

            self.__last.next = node
            node.prev = self.__last
            node.next = head
            head.prev = node
            self.__last = node

        self.size += 1

    def remove(self, player: Player):
        """
        Remove the input player from the list.
        """
        if self.__last is not None:
            if self.__last.next == self.__last:
                self.__last = None
            else:
                head = self.__last.next
                temp = head

                while temp.next != head:
                    if temp.data == player:
                        prev = temp.prev
                        next = temp.next

                        prev.next = next
                        next.prev = prev

                        self.size -= 1
                        break
                    else:
                        temp = temp.next

    def next_player(self) -> Player:
        """
        Calculate the next player.
        """
        if self.__current_node is None:
            if self.__last is not None:
                self.__current_node = self.__last.next
        else:
            self.__current_node = self.__current_node.next

        return self.current_player

    def iterate(self):
        """
        Iterates through the linked list and returns the list of players present.
        """
        if self.__last is not None:
            # It starts from the last element, but on the first iteration, it will point to the first element
            if self.__temp_iterator is None:
                self.__temp_iterator = self.__last

            head = self.__last.next

            iterate = True
            while iterate:
                # Point to the next node
                self.__temp_iterator = self.__temp_iterator.next
                temp = self.__temp_iterator
                # if the next element is the first again, then it blocks the iteration
                if self.__temp_iterator.next == head:
                    # So for the next iteration, it forces the element to point to the last one, If this is not done,
                    # each time we start from the last element in which we remained.
                    self.__temp_iterator = None
                    iterate = False
                yield temp.data
        else:
            # Nothing to iterate
            self.__temp_iterator = None
            yield
