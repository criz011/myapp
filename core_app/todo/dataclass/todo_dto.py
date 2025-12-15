from dataclasses import dataclass

@dataclass
class TodoData:
    title: str
    description: str = ""
    completed: bool = False
