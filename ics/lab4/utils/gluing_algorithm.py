from .func import TabelFunction

from .mx_models import MultiplexorResultInput


class GluingAlgorithm:
    def __init__(self, tabel: TabelFunction) -> None:
        self.tabel = tabel
        self.mx_glue = []

    def generate_glue(self, index_row: int, glue_size: int, count_row: int, count_used_row: int) -> list:
        self.mx_glue = []
        for index_v in range(index_row, index_row + glue_size):
            if count_row == count_used_row:
                self.mx_glue.append(self.tabel.rows[index_v].result.value)
            else:
                self.mx_glue.append([self.tabel.rows[index_v].result.value, self.tabel.rows[index_v].get_string_vars])
        return self.mx_glue
    
    def address_equals_var(self) -> MultiplexorResultInput:
        return MultiplexorResultInput(
            result_one=f"{self.mx_glue[0]}",
            result_zero=f"!{1 if self.mx_glue[0] else 0}"
        )

    def address_smaller_var(self, count_addresses: int, count_var: int) -> MultiplexorResultInput:
        correct_result, wrong_result = [], []
        unit_r, zero_r = "", ""

        # We divide the results with one and zero into 2 heaps
        for i in self.mx_glue:
            (correct_result if i[0] == 1 else wrong_result).append(i[1][count_addresses::])

        if all([i[0] == 0 for i in self.mx_glue]):
            # all glue is zero
            unit_r, zero_r = "0", "!1"
        elif all([i[0] == 1 for i in self.mx_glue]):
            # all glue is one
            unit_r, zero_r = "1", "!0"
        else:
            # glue with random results
            unit_r, zero_r = self.__identify_glue(
                count_addresses,
                count_var,
                correct_result,
                wrong_result
            ) 
        return MultiplexorResultInput(zero_r, unit_r)
    
    def __identify_glue(self, count_addresses: int, count_var: int, correct_result: list, wrong_result: list):
        unit_results, zero_results = [], []

        # select equivalent symbols in the gluing taking into account the result
        for i in range(0, count_var - count_addresses):
            local_unit: set[str] = set(map(lambda chars: chars[i], correct_result))
            local_zero: set[str] = set(map(lambda chars: chars[i], wrong_result))
            if len(local_unit) == 1:
                unit_results.append(local_unit.pop())
            if len(local_zero) == 1:
                zero_results.append(local_zero.pop())
        
        # default answers
        zero_r = f"!({' * '.join(zero_results)})"
        unit_r = ' * '.join(unit_results)

        # answers if we cannot minimize gluing as much as possible
        if len(unit_results) == 0:
            unit_results = [" * ".join(j) for j in correct_result]
            unit_r = ' + '.join(unit_results)
        if len(zero_results) == 0:
            zero_results = [" * ".join(j) for j in wrong_result]
            zero_r = f"!({' + '.join(zero_results)})"
        
        return unit_r, zero_r
