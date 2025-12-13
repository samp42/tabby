"""
Docstring for tests.test_query_building
Tests for query building
"""

import pytest
import tabby as tab
from tabby.token import Token
from tabby.tokentype import TokenType

def test_select_query_building():
    df = tab.DataFrame()
    df = df.select('col1', 'col2', 'col3')
    
    expected_query = [
        TokenType.SELECT,
        # Token('col1'),
        # Token('col2'),
        # Token('col3')
    ]
    
    assert df.query == expected_query

def test_where_query_building():
    df = tab.DataFrame()
    df = df.where(tab.col('col1') > 10)
    
    expected_query = [
        TokenType.WHERE,
        TokenType.GT,
    ]
    
    assert df.query == expected_query


if __name__ == "__main__":
    pytest.main()
