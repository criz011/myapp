from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateArtistRequest:
    name: Optional[str] = None
    age: Optional[int] = None
