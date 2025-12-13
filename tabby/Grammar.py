from lark import Lark

GRAMMAR = r"""
    start: select_stmt  
    select_stmt: "SELECT" column_list "FROM" table_ref where_clause? join_clause* group_by_clause? agg_clause?
    column_list: "*" | column ("," column)*
    column: CNAME
    table_ref: CNAME
"""