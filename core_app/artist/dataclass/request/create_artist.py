from dataclasses import dataclass


@dataclass
class CreateArtistRequest:
    name: str
    age: int
