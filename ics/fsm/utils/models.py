from .forms import tabel_str


class Tabel:
    def __init__(self, headers: list[str], inputs: list[str], states: list[list[str]]) -> None:
        self.headers = headers
        self.inputs = inputs
        self.states = states
    
    def __str__(self) -> str:
        return tabel_str.format(
            H = self.headers,
            A = self.states,
            Z = self.inputs
        )

    def __repr__(self) -> str:
        return self.__str__()


class StructuralMachine(Tabel):
    def __init__(
        self,
        headers: list[str],
        inputs: list[str],
        states: list[list[str]],
        exits: list[list[str]]
    ) -> None:
        super().__init__(headers, inputs, states)
        self.exits = exits
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nW = {self.exits}"



class MemoryExcitation(Tabel):
    def __init__(
        self,
        headers: list[str],
        inputs: list[str],
        states: list[list[str]]
    ) -> None:
        super().__init__(headers, inputs, states)
