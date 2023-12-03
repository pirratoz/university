from .fsm import Fsm
from .vector import Vector


class StructuralMachine(Fsm):
    def __init__(
        self,
        headers: list[str],
        inputs: list[str],
        states: list[list[str]],
        exits: list[list[str]]
    ) -> None:
        super().__init__(headers, inputs, states, exits)
        self.__update_machine()
    
    def __update_machine(self) -> None:
        states = Vector(self.headers, "q")
        exits = Vector(self.__get_sorted_unique_values(self.exits), "y")
        inputs = Vector(self.inputs, "x")

        self.__update_headers(states)
        self.__update_inputs(inputs)
        self.__update_exits(exits)
        self.__update_states(states)

    @staticmethod
    def __get_sorted_unique_values(matrix: list[list[str]]) -> list[str]:
        values = []
        for line in matrix:
            for element in line:
                if element not in values:
                    values.append(element)
        return sorted(values)
    
    def __update_headers(self, states: Vector) -> None:
        self.headers = [
            states.binary_map[state]
            for state in self.headers
        ]

    def __update_inputs(self, inputs: Vector) -> None:
        self.inputs = [
            inputs.binary_map[_input]
            for _input in self.inputs
        ]

    def __update_exits(self, exits: Vector) -> None:
        self.exits = [
            [
                exits.binary_map[_exit]
                for _exit in line
            ]
            for line in self.exits
        ]

    def __update_states(self, states: Vector) -> None:
        self.states = [
            [
                states.binary_map[state]
                for state in line
            ]
            for line in self.states
        ]
