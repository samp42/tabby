from ..dataframe import DataFrame
from ..tokentype import TokenType
from ..token import Token

def read_csv(path: str, options=None) -> Dataframe:
    df = DataFrame()
    df.query.append(Token(TokenType.CSV_SCAN, path))

    return df
