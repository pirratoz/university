from math import log2, ceil



class Vectors:
    def __init__(self, A: list[str], W: list[str], Z: list[str], I: int, N: int, L: int) -> None:
        self.states = self.__get_vector_data(I, A)
        self.exits = self.__get_vector_data(N, W)
        self.inputs = self.__get_vector_data(L, Z)

        self.states_string = self.__get_string_vector("q", I)
        self.exits_string = self.__get_string_vector("y", N)
        self.inputs_string = self.__get_string_vector("x", L)
    
    def __get_vector_data(self, size_vector: int, elements: list[str]) -> dict[str, str]:
        return {
            value: bin(e)[2:].rjust(size_vector, "0")
            for e, value in enumerate(elements)
        }

    def __get_string_vector(self, designation: str, size: int):
        return ''.join(map(lambda i: f"{designation}{i}", range(1, size + 1)))


class CodingMachine:
    def __init__(self, states: list[str], exits: list[str], inputs: list[str]) -> None:
        self.A = states
        self.W = exits
        self.Z = inputs

        self.I = self.get_vector_size(len(states))
        self.L = self.get_vector_size(len(inputs))
        self.N = self.get_vector_size(len(exits))

        # {(state/exits/inputs): vector}
        self.vectors = Vectors(self.A, self.W, self.Z, self.I, self.N, self.L)

    @staticmethod
    def get_vector_size(count_unique_elements: int) -> int:
        return ceil(log2(count_unique_elements))
