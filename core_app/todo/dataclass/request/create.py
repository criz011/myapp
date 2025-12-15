from dataclasses import dataclass


@dataclass
class CreateTodoData:
    title: str
    description: str = ""
    completed: bool = False
