from dataclasses import dataclass
from datetime import date

@dataclass
class SongData:
    title: str
    artist: str
    duration: int
    release_date: date
