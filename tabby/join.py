from enum import Enum, auto

class JoinType(Enum):
    LEFT = auto()
    LEFT_OUTER = auto()
    LEFT_INNER = auto()
    LEFT_ANTI = auto()
    LEFT_SEMI = auto()
    
    RIGHT = auto()
    RIGHT_OUTER = auto()
    RIGHT_INNER = auto()
    RIGHT_ANTI = auto()
    RIGHT_SEMI = auto()

    INNER = auto()
    OUTER = auto()

    def __str__(self) -> str:
        return self.name
