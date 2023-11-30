from math import log2, ceil


class CodingMachine:
    def __init__(self, states: list[str], exits: list[str], inputs: list[str]) -> None:
        self.A = states
        self.W = exits
        self.Z = inputs

        self.I = self.get_vector_size(len(states))
        self.L = self.get_vector_size(len(inputs))
        self.N = self.get_vector_size(len(exits))

        # {(state/exits/inputs): vector}
        self.v_state: dict[str, str] = self.__get_vector_data(self.I, self.A)
        self.v_exits: dict[str, str] = self.__get_vector_data(self.N, self.W)
        self.v_inputs: dict[str, str] = self.__get_vector_data(self.L, self.Z)
    
    def __get_vector_data(self, size_vector: int, elements: list[str]) -> dict[str, str]:
        return {
            value: bin(e)[2:].rjust(size_vector, "0")
            for e, value in enumerate(elements)
        }

    @property
    def vector_states(self) -> str:
        return ''.join(map(lambda i: f"q{i}", range(1, self.I + 1)))
    
    @property
    def vector_inputs(self) -> str:
        return ''.join(map(lambda i: f"x{i}", range(1, self.L + 1)))
    
    @property
    def vector_exits(self) -> str:
        return ''.join(map(lambda i: f"y{i}", range(1, self.N + 1)))

    @staticmethod
    def get_vector_size(count_unique_elements: int) -> int:
        return ceil(log2(count_unique_elements))
