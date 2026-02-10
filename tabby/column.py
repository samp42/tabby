from typing import Any

class Column():
    name: str

    def __init__(self, name):
        self.name = name

    def gte(self, val: Any) -> Expr:
        pass