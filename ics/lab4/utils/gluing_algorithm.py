from typing import Iterator
from dataclasses import dataclass

from .func import (
    TabelFunction,
    TabelRow
)
from .mx_models import MultiplexorResultInput


@dataclass(frozen=True)
class MxData:
    glue_size: int
    count_addresses: int
    count_row: int
    count_used_row: int
    count_var: int


@dataclass
class FunctionData:
    result: int
    vars: list[str]


class GluingAlgorithm:
    def __init__(self, tabel: TabelFunction, data: MxData, sign: bool = False) -> None:
        self.tabel = tabel
        self.gluing: list[FunctionData] = []
        self.mx = data
        self.sign: bool = sign

    def for_equivalent_size(self) -> Iterator[tuple[int, MultiplexorResultInput]]:
        for index_row in range(0, self.mx.count_row, self.mx.glue_size):
            value = self.__row_result(index_row)
            result = MultiplexorResultInput(f"{value}", f"!{1 if value else 0}")
            yield index_row, result

    def for_smaller_size(self) -> Iterator[tuple[int, MultiplexorResultInput]]:
        for index_row in range(0, self.mx.count_row, self.mx.glue_size):
            index_glue = index_row // self.mx.glue_size
            self.__generate_glue(index_row)
            result = self.__address_smaller_var()
            yield index_glue, result

    def __generate_glue(self, index_row: int) -> None:
        self.gluing = [
            FunctionData(self.__row_result(index), self.__row_vars(index))
            for index in range(index_row, index_row + self.mx.glue_size)
        ]
    
    def __row_result(self, index: int) ->  int:
        return self.tabel.rows[index].result.value

    def __row_vars(self, index: int) ->  list[str]:
        return self.tabel.rows[index].get_string_vars

    def __address_smaller_var(self) -> MultiplexorResultInput:
        correct_result: list[list[str]] = []
        wrong_result: list[list[str]] = []
        unit_r, zero_r = "", ""

        # We divide the results with one and zero into 2 heaps
        for part_glue in self.gluing:
            current_list = wrong_result if part_glue.result == 0 else correct_result
            vars = part_glue.vars[self.mx.count_addresses::]
            current_list.append(vars)

        if all([i.result == 0 for i in self.gluing]):
            # all glue is zero
            unit_r, zero_r = "0", "!(1)"
        elif all([i.result == 1 for i in self.gluing]):
            # all glue is one
            unit_r, zero_r = "1", "!(0)"
        else:
            # glue with random results
            unit_r, zero_r = self.__identify_glue(
                correct_result,
                wrong_result
            ) 
        return MultiplexorResultInput(zero_r, unit_r)
    
    def __identify_glue(self, correct_result: list[list[str]], wrong_result: list[list[str]]):
        unit_results: list[str] = []
        zero_results: list[str] = []

        # select equivalent symbols in the gluing taking into account the result
        for i in range(0, self.mx.count_var - self.mx.count_addresses):
            local_unit: set[str] = set(map(lambda chars: chars[i], correct_result))
            local_zero: set[str] = set(map(lambda chars: chars[i], wrong_result))
            if len(local_unit) == 1:
                unit_results.append(local_unit.pop())
            if len(local_zero) == 1:
                zero_results.append(local_zero.pop())
        
        sign = ["", " * "][self.sign]
        concat = sign.join

        # default answers
        zero_r = concat(zero_results)
        unit_r = concat(unit_results)

        # answers if we cannot minimize gluing as much as possible
        if len(unit_results) == 0:
            unit_r = " + ".join(map(concat, correct_result))
        if len(zero_results) == 0:
            zero_r = " + ".join(map(concat, wrong_result))
        
        return unit_r, f"!({zero_r})"
