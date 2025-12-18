from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class UpdateSongData:
    title: Optional[str] = None
    artist: Optional[str] = None
    duration: Optional[int] = None
    release_date: Optional[date] = None
