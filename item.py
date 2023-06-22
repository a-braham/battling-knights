from dataclasses import dataclass

from position import Position


@dataclass
class Item:
    name: str
    rank: int
    pos: Position
    attack: int
    defence: int
