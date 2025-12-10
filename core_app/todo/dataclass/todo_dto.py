from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class TodoData:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    completed: bool = False

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TodoData":
        return TodoData(
            id=data.get("id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            completed=bool(data.get("completed", False)),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
