from ..dataframe import DataFrame
from ..tokentype import TokenType
from ..token import Token

def from_db(query: str, options=None) -> Dataframe:
    df = DataFrame()
    df.query.append(Token(TokenType.DB_SCAN, query))

    return df
