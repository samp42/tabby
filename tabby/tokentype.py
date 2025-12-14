from enum import Enum, auto

class TokenType(Enum):
    # Input Sources
    CSV_SCAN = auto()
    PARQUET_SCAN = auto()
    DB_SCAN = auto()

    # Literals
    COLUMN_LITERAL = auto()
    STRING_LITERAL = auto()
    NUMERIC_LITERAL = auto()
    BOOLEAN_LITERAL = auto()
    NULL_LITERAL = auto()
    IDENTIFIER = auto()

    # Statements
    SELECT = auto()
    WHERE = auto()

    # Binary Operators
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    AND = auto()
    OR = auto()
    XOR = auto()

    # Unary Operators
    NEG = auto()
    NOT = auto()

    # Comparison Operators
    EQ = auto()
    NEQ = auto()
    LT = auto()
    LTE = auto()
    GT = auto()
    GTE = auto()

    # Grouping
    LPAREN = auto()
    RPAREN = auto()

    def __str__(self) -> str:
        return self.name
