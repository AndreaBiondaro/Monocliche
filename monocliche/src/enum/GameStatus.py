from enum import Enum


class GameStatus(Enum):
    """Indicates all states the game can be in."""

    NEW = "NEW"
    COMPLETED = "COMPLETED"
    RUNNING = "RUNNING"
