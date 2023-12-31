from math import (
    ceil,
    log2
)


class Vector:
    def __init__(self, elements: list[str], designation: str) -> None:
        self.designation = designation
        self.values = elements
        self.size = self.__get_vector_size(len(elements))
        self.binary_map =  self.__get_vector_data(self.size, elements)
    
    @property
    def string(self) -> str:
        return ''.join(map(
            lambda i: f"{self.designation}{i}",
            range(1, self.size + 1)
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
