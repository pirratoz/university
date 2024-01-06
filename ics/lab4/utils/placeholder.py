from copy import deepcopy

from .func import (
    Alphabet,
    Bool,
    TabelRow,
    TabelFunction
)


class FunctionIsNotValid(Exception):
    ...


class RowPlaceholder:
    def fill_rows(self, tabel: TabelFunction) -> None:
        ...


class ReadyResultsPlaceholder(RowPlaceholder):

    def __init__(self, count_var: int, results: list[int], bool: Bool) -> None:
        self.count_var = count_var
        self.results = results
        self.bool = bool

    def fill_rows(self, tabel: TabelFunction) -> None:
        neg_bool = Bool.false if self.bool == Bool.true else Bool.true
        for index in range(0, 2 ** self.count_var):
            tabel.rows.append(
                TabelRow(
                    list(map(lambda value: Bool.get(value), bin(index)[2::].rjust(self.count_var, "0"))),
                    self.bool if index in self.results else neg_bool
                )
            )


class CalculatedResultsPlaceholder(RowPlaceholder):
    def __init__(self, function: str) -> None:
        self.count_var: int = 0
        self.function: str = function
    
    def check_function_valid(self) -> bool:
        alphabet = Alphabet.vars + Alphabet.neg + Alphabet.parenthesis + Alphabet.space + Alphabet.action
        for char in set(self.function):
            if char not in alphabet:
                return False
        return True
    
    def get_executable_function(self) -> str:
        func = deepcopy(self.function)
        for char in Alphabet.vars:
            func = func.replace(f"!{char}", f"not({char})")
        for char in Alphabet.vars[::-1]:
            func = func.replace(f"{char}", f"self.{char}")
        return func.replace(
            Alphabet.action[0], " or "
        ).replace(
            Alphabet.action[1], " and "
        ).replace(
            Alphabet.neg, "not"
        )

    def get_used_vars(self) -> list[str]:
        vars = [char for char in Alphabet.vars if char in self.function]
        return vars

    def execute_function(self, func: str, used_vars: list[str], values: list[Bool]) -> TabelRow:
        for _var, value in zip(used_vars, values):
            setattr(self, _var, value.value)
        try:
            return TabelRow(
                variables=values,
                result=Bool.true if eval(func) == 1 else Bool.false
            )
        except Exception:
            raise FunctionIsNotValid()

    def fill_rows(self, tabel: TabelFunction) -> None:
        if not self.check_function_valid():
            raise FunctionIsNotValid()
        used_vars = self.get_used_vars()
        function = self.get_executable_function()
        self.count_var = len(used_vars)
        for index in range(0, 2 ** self.count_var):
            tabel.rows.append(
                self.execute_function(
                    func=function,
                    used_vars=used_vars,
                    values=list(map(lambda value: Bool.get(value), bin(index)[2::].rjust(self.count_var, "0")))
                )
            )
