from dataclasses import dataclass
from datetime import date

@dataclass
class SongData:
    title: str
    duration: int
    release_date: date
    artist_id: int

