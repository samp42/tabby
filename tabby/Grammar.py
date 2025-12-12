from tkinter.constants import SEL
from enum import Enum
from typing import Dict, List

class Op(Enum):
    pass

class StatementOp(Op):
    SELECT = 'SELECT'
    FILTER = 'FILTER'
    JOIN = 'JOIN'
    GROUP_BY = 'GROUP_BY'

class BinaryOp(Op):
    ADD = 'ADD'
    SUB = 'SUB'
    MUL = 'MUL'
    DIV = 'DIV'
    AND = 'AND'
    OR = 'OR'
    XOR = 'XOR'

class UnaryOp(Op):
    NEG = 'NEG'
    NOT = 'NOT'
    GROUPING = 'GROUPING'

grammar: Dict[Op, List[Op]] = {
    StatementOp.SELECT: [BinaryOp.ADD, BinaryOp.SUB, BinaryOp.MUL, BinaryOp.DIV, BinaryOp.AND, BinaryOp.OR, BinaryOp.XOR, UnaryOp.NEG, UnaryOp.NOT, UnaryOp.GROUPING],

}
