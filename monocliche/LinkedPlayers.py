from typing import Any

from monocliche.model import Player


class Node:

    def __init__(self, data: Player, next: Any = None, prev: Any = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedPlayers:

    def __init__(self):
        self.__last = None
        self.__current_node = None
        self.size = 0

    @property
    def current_player(self) -> Player:
        if self.__current_node is not None:
            return self.__current_node.data
        else:
            return None

    @property
    def first_player(self) -> Player:
        if self.__last is not None and self.__last.next is not None:
            return self.__last.next.data
        else:
            return None

    def add(self, player: Player):
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
        if self.__current_node is None:
            self.__current_node = self.__last.next
        else:
            self.__current_node = self.__current_node.next

        return self.current_player
