"""
Docstring for tests.test_query_building
Tests for query building
"""

import pytest
import tabby as tab
from tabby.token import Token, get_token
from tabby.tokentype import TokenType

def test_select_query_building():
    df = tab.DataFrame()
    df = df.select('col1', 'col2', 'col3')

    expected_query = [
        get_token(TokenType.SELECT),
        get_token(TokenType.LPAREN),
        Token(TokenType.COLUMN_LITERAL, 'col1'),
        Token(TokenType.COLUMN_LITERAL, 'col2'),
        Token(TokenType.COLUMN_LITERAL, 'col3'),
        get_token(TokenType.RPAREN)
    ]

    assert df.query == expected_query

def test_select_all_query_building():
    df = tab.DataFrame()
    df = df.select('*')

    expected_query = []

    assert df.query == expected_query

@pytest.mark.skip(reason="Not implemented yet")
def test_where_query_building():
    df = tab.DataFrame()
    df = df.where(tab.col('col1') > 10)

    expected_query = [
        get_token(TokenType.WHERE),
        Token(TokenType.COLUMN_LITERAL, 'col1'),
        get_token(TokenType.GT),
        Token(TokenType.NUMERIC_LITERAL, '10')
    ]

    assert df.query == expected_query

def test_count_query_building():
    df = tab.DataFrame()
    count = df.count()

    expected_query = [
        get_token(TokenType.SELECT),
        get_token(TokenType.COUNT)
    ]

    assert df.query == expected_query
    assert count == 0  # Since count method returns 0 in the stub

if __name__ == "__main__":
    pytest.main()
