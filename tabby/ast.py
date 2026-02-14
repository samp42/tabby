from tabby import TokenType
from typing import List
from tabby import Token

class InvalidQueryException(Exception):
    def __init__(super, message):
        pass

class AST:
    token: Token
    children: List[Token]

    def __init__(self, token, children):
        self.token = token
        self.children = children

    def build_from_query(query: List[Token]):
        # Query not starting with select is valid
        # Treat literals, identifiers, and inputs as leaves
        #

        if len(query) == 0:
            raise InvalidQueryException("Query is empty.")

        if query[0] != TokenType.SELECT:
            raise InvalidQueryException("Query should start with SELECT.")

        root = AST(query[0], [])
