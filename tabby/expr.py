from __future__ import annotations

class Expr:
    value: str

    def __init__(self, value: str):
        self.value = value

    def __gt__(self, other: int) -> Expr:
        return Expr(f"({self.value} > {other})")

def col(name: str) -> 'Expr':
    return Expr(f"Column({name})")

"""
class Expr:
    def __init__(self, value: any):
        self.value = value

    def select(self, columns: list[str]) -> 'Expr':
        return Expr(f"Select({self.value}, {columns})")

    def filter(self, condition: str) -> 'Expr':
        return Expr(f"Filter({self.value}, {condition})")

    def join(self, other: 'Expr', on: str, how: str = 'left') -> 'Expr':
        return Expr(f"Join({self.value}, {other.value}, on={on}, how={how})")

    def aggregate(self, group_by: list[str], aggregations: dict[str, str]) -> 'Expr':
        return Expr(f"Aggregate({self.value}, group_by={group_by}, aggregations={aggregations})")
"""