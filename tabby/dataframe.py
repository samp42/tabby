from typing import List, Any
from .token import Token, get_token
from .tokentype import TokenType

class DataFrame():
    cols: List[str]
    query: List[Token] = []

    def __init__(self):
        self.cols = []
        self.query = []

    def select(self, *cols: List[str]) -> DataFrame:
        if cols == '*':
            return self

        self.query.append(get_token(TokenType.SELECT))
        self.query.append(get_token(TokenType.LPAREN))
        for col in cols:
            self.query.append(TokenType.COLUMN_LITERAL)

        self.query.append(TokenType.RPAREN)

        return self

    def where(self, condition: Any) -> DataFrame:
        self.query.append(get_token(TokenType.WHERE))



        return self
