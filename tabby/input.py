from dataframe import DataFrame
from tokentype import TokenType
from token import Token

def read_csv(path: str) -> 'DataFrame':
    df = DataFrame()
    df.query.append(TokenType.CSV_SCAN)
    df.query.append(Token(path))
    return df

def read_parquet(path: str) -> 'DataFrame':
    df = DataFrame()
    df.query.append(TokenType.PARQUET_SCAN)
    df.query.append(Token(path))
    return df

def from_db(query: str) -> 'DataFrame':
    df = DataFrame()
    df.query.append(TokenType.DB_SCAN)
    df.query.append(Token(query))
    return df