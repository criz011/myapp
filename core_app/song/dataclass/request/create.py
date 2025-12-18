from dataclasses import dataclass
from datetime import date


@dataclass
class CreateSongData:
    title: str
    artist: str
    duration: int
    release_date: date
