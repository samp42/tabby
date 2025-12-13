from __future__ import annotations

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
