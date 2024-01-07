from typing import Iterator
from dataclasses import dataclass

from .func import TabelFunction
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
            result = MultiplexorResultInput(f"!{0 if value else 1}", f"{value}")
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

    def __check_big_glue(self, items: list[list[str]], max_var: int) -> list[list[str]]:
        new_items = []
        for var in set(map(lambda v: v[0], items)):
            indexs = []
            for index, vars in enumerate(items):
                if var in vars:
                    indexs.append(index)
            indexs.reverse()
            if len(indexs) == max_var:
                new_items.append([var])
                list(map(items.pop, indexs))
            else:
                list(map(lambda index: new_items.append(items.pop(index)), indexs))
        return new_items
    
    def __identify_glue(self, correct_result: list[list[str]], wrong_result: list[list[str]]) -> tuple[str, str]:
        unit_results: list[str] = []
        zero_results: list[str] = []

        max_var = int((len(correct_result) + len(wrong_result)) / 2)

        # select equivalent symbols in the gluing taking into account the result
        for i in range(0, self.mx.count_var - self.mx.count_addresses):
            local_unit: list[str] = list(set(map(lambda chars: chars[i], correct_result)))
            local_zero: list[str] = list(set(map(lambda chars: chars[i], wrong_result)))
            # the variable should also not be included in two lists at once
            if len(local_unit) == 1 and local_unit[0] not in local_zero:
                unit_results.append(local_unit[0])
            if len(local_zero) == 1 and local_zero[0] not in local_unit:
                zero_results.append(local_zero[0])
        correct_result = self.__check_big_glue(correct_result, max_var)
        wrong_result = self.__check_big_glue(wrong_result, max_var)
        return self.__generate_answer(unit_results, zero_results, correct_result, wrong_result)

    def __generate_answer(self, unit_results, zero_results, correct_result, wrong_result) -> tuple[str, str]:
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
        
        # answers, if there are 2 correct answers in total and they differ in 1 variable
        cr, wr = correct_result, wrong_result
        if len(unit_results) == 0 and len(correct_result) == 2 and all([len(cr[0]) == len(l) for l in cr]):
            chars = [cr[0][i] for i in range(len(cr[0])) if cr[0][i] == cr[1][i]]
            if any(chars):
                unit_r = "".join(chars)
        if len(wrong_result) == 0 and len(wrong_result) == 2 and all([len(wr[0]) == len(l) for l in wr]):
            chars = [wr[0][i] for i in range(len(wr[0])) if wr[0][i] == wr[1][i]]
            if any(chars):
                zero_r = "".join(chars)
        return unit_r, f"!({zero_r})"