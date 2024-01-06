from math import log2

from .func import TabelFunction
from .placeholder import RowPlaceholder
from .gluing_algorithm import GluingAlgorithm
from .mx_models import (
    InputHashMap,
    MultiplexorCountInput
)


class Multiplexor:
    def __init__(self, count_input: MultiplexorCountInput, row_generator: RowPlaceholder) -> None:
        self.count_input: int = count_input.value
        self.row_generator = row_generator
        self.tabel = TabelFunction([])
    
    def __get_inputs(self) -> InputHashMap:
        map = InputHashMap()

        GLUE_SIZE = int(len(self.tabel.rows) / self.count_input)
        COUNT_ADDRESSES = int(log2(self.count_input))
        COUNT_ROW = len(self.tabel.rows)
        COUNT_USED_ROW = 2 ** COUNT_ADDRESSES
        COUNT_VAR = len(self.tabel.rows[0].variables)

        algorithm = GluingAlgorithm(self.tabel)

        for INDEX_ROW in range(0, COUNT_ROW, GLUE_SIZE):
            INDEX_GLUE = INDEX_ROW // GLUE_SIZE

            algorithm.generate_glue(
                INDEX_ROW, GLUE_SIZE, COUNT_ROW, COUNT_USED_ROW
            )

            if COUNT_ROW == COUNT_USED_ROW:
                # count adresses equal count var
                map[f"X{INDEX_ROW}"] = algorithm.address_equals_var()
            else:
                # count adersses smaller then var
                map[f"X{INDEX_GLUE}"] = algorithm.address_smaller_var(COUNT_ADDRESSES, COUNT_VAR)
        return map

    @property
    def inputs(self) -> InputHashMap:
        self.tabel = TabelFunction([])
        self.row_generator.fill_rows(self.tabel)
        return self.__get_inputs()
