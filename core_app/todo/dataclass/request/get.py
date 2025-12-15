from dataclasses import dataclass
from typing import Optional


@dataclass
class GetTodoData:
    todo_id: Optional[int] = None
