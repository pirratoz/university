from .base_trigger import Trigger


class TriggerRS(Trigger):
    def __init__(self) -> None:
        ...
    
    @property
    def moves(self) -> dict[str, str]:
        return {
            "00": "0*",
            "01": "10",
            "10": "01",
            "11": "*0",
        }
