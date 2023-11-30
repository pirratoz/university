from math import log2, ceil


class Vector:
    def __init__(self, elements: list[str], designation: str) -> None:
        self.designation = designation
        self.values = elements
        self.size_binary_data = self.__get_vector_size(len(elements))
        self.values_bin =  self.__get_vector_data(self.size_binary_data, elements)
    
    @property
    def string(self) -> str:
        return ''.join(map(
            lambda i: f"{self.designation}{i}",
            range(1, self.size_binary_data + 1)
        ))
    
    @staticmethod
    def __get_vector_size(count_unique_elements: int) -> int:
        return ceil(log2(count_unique_elements))
    
    @staticmethod
    def __get_vector_data(size_vector: int, elements: list[str]) -> dict[str, str]:
        return {
            value: bin(e)[2:].rjust(size_vector, "0")
            for e, value in enumerate(elements)
        }


class CodingMachine:
    def __init__(self, states: list[str], exits: list[str], inputs: list[str]) -> None:
        self.states = Vector(states, "q")
        self.exits = Vector(exits, "y")
        self.inputs = Vector(inputs, "x")
