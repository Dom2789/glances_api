from dataclasses import dataclass

@dataclass(frozen=True)
class Data:
    hostname:str
    cpu_total: float
    mem_total: float
    temp: int
