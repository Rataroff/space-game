from enum import Enum, auto

class State(Enum):
    MENU = auto() # automatically assigns a unique integer value to each enum member (from 1 by default)
    PLAYING = auto()
    GAME_OVER = auto()