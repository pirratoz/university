from .base_trigger import Trigger


class TriggerD(Trigger):
    def __init__(self) -> None:
        ...
    
    @property
    def moves(self) -> dict[str, str]:
        return {
            "00": "0",
            "01": "1",
            "10": "0",
            "11": "1",
        }
