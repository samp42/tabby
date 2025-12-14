from typing import Optional
from .tokentype import TokenType

class Token():
    type: TokenType
    lexeme: str
    literal: Optional[str]

    def __init__(self, type: TokenType, lexeme: str, literal: Optional[str] = None):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Token):
            return False
        return self.type == other.type and self.lexeme == other.lexeme and self.literal == other.literal


def get_token(type: TokenType) -> Token:
    return Token(type, type.__str__(), None)
