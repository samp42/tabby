from __future__ import annotations

from typing import List, Any
from .token import Token
from .tokentype import TokenType

class DataFrame():
    cols: List[str]
    query: List[Token] = []

    def __init__(self):
        self.cols = []
        self.query = []

    def select(self, *cols: Any) -> DataFrame:
        self.query.append(TokenType.SELECT)
        for col in cols:
            self.query.append(Token(str(col)))

        pass

    def where(self, condition: Any) -> DataFrame:
        self.query.append(TokenType.WHERE)
        self.query.append(Token(str(condition)))
        pass

