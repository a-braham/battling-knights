from dataclasses import dataclass

from item import Item
from position import Position

STATUS = ('LIVE', 'DEAD', 'DROWNED')


@dataclass
class Knight:
    id: str
    color: str
    pos: Position
    status: str = STATUS[0]
    equipped: Item = None
    attack: int = 1
    defence: int = 1

    def update_status(self, index):
        self.status = STATUS[index]
