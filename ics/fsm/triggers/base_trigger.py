class Trigger:
    def __init__(self) -> None:
        ...
    
    @property
    def moves(self) -> dict[str, str]:
        ...

    def get_new_condition(self, initial_state: str, final_state: str) -> str:
        return self.moves[f"{initial_state}{final_state}"]
