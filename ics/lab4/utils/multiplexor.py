from math import log2

from .func import TabelFunction
from .placeholder import RowPlaceholder
from .gluing_algorithm import (
    MxData,
    GluingAlgorithm
)
from .mx_models import (
    InputHashMap,
    MultiplexorCountInput
)


class Multiplexor:
    def __init__(self, count_input: MultiplexorCountInput, row_placeholder: RowPlaceholder) -> None:
        self.count_input: int = count_input.value
        self.row_placeholder = row_placeholder
        self.tabel = TabelFunction([])
        self.sign: bool = False

    def __get_inputs(self) -> InputHashMap:
        map = InputHashMap()

        data = MxData(
            int(len(self.tabel.rows) / self.count_input),
            int(log2(self.count_input)),
            len(self.tabel.rows),
            2 ** int(log2(self.count_input)),
            len(self.tabel.rows[0].variables)
        )

        algorithm = GluingAlgorithm(self.tabel, data, self.sign)

        iter_algorithm = algorithm.for_smaller_size

        if data.count_row == data.count_used_row:
            iter_algorithm = algorithm.for_equivalent_size

        for index, result in iter_algorithm():
            map[f"X{index}"] = result

        return map

    @property
    def inputs(self) -> InputHashMap:
        self.tabel = TabelFunction([])
        self.row_placeholder.fill_rows(self.tabel)
        return self.__get_inputs()
