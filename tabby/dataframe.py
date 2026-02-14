from tabby import Expr
from typing import List, Any, Tuple, Self
from .token import Token, get_token
from .tokentype import TokenType
from .join import JoinType

class DataFrame():
    cols: List[str]
    query: List[Token]

    def __init__(self):
        self.cols = []
        self.query = []

    def select(self, *cols: str) -> DataFrame:
        if cols == ('*',):
            return self

        self.query.append(get_token(TokenType.SELECT))
        self.query.append(get_token(TokenType.LPAREN))
        for col in cols:
            self.query.append(Token(TokenType.COLUMN_LITERAL, col))

        self.query.append(get_token(TokenType.RPAREN))

        return self

    def where(self, predicate: Expr) -> DataFrame:
        self.query.append(get_token(TokenType.WHERE))

        return self

    def join(self, df: Self, on: Tuple[str], how: JoinType | str):
        self.query.append(get_token(TokenType.JOIN))
        self.query.append(Token(TokenType.IDENTIFIER, df.__class__.__name__))
        self.query.append(get_token(TokenType.JOIN_ON))
        self.query.append(get_token(TokenType.LPAREN))
        for col in on:
            self.query.append(Token(TokenType.COLUMN_LITERAL, col))
        self.query.append(get_token(TokenType.RPAREN))
        self.query.append(Token(TokenType.JOIN_HOW, how.__str__()))
        return self

    def join(self, df: Self, left_on: Tuple[str], right_on: Tuple[str], how: JoinType | str):
        pass

    def count(self) -> int:
        self.query.append(get_token(TokenType.SELECT))
        self.query.append(get_token(TokenType.COUNT))
        return 0

    def collect(self) -> DataFrame:
        return self

    def show(self):
        # Print header
        # print lines
        pass

    def show_ui(self):
        # Open dataframe in UI
        pass

    # TODO: return column type
    def __getattr__(self, name: str) -> Any:
        return Token(TokenType.COLUMN_LITERAL, name)
