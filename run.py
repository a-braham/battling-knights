from arena import Arena
from serializer import Serialize
from item import Item
from knight import Knight


class Play:
    def setup_board(self):
        self.arena = Arena()
        ab = self.arena.board

        self.R = Knight('R', 'red', ab[0][0])
        self.Y = Knight('Y', 'yellow', ab[0][7])
        self.B = Knight('B', 'blue', ab[7][0])
        self.G = Knight('G', 'green', ab[7][7])

        ab[0][0].knight = self.R
        ab[0][7].knight = self.Y
        ab[7][0].knight = self.B
        ab[7][7].knight = self.G

        self.axe = Item('Axe', 4, ab[2][2], 2, 0)
        self.dagger = Item('Dagger', 2, ab[2][5], 1, 0)
        self.magicstaff = Item('MagicStaff', 3, ab[5][2], 1, 1)
        self.helmet = Item('Helmet', 1, ab[5][5], 0, 1)

        ab[2][2].items.append(self.axe)
        ab[2][5].items.append(self.dagger)
        ab[5][2].items.append(self.magicstaff)
        ab[5][5].items.append(self.helmet)

        return (
            self.arena,
            self.R,
            self.Y,
            self.B,
            self.G,
            self.axe,
            self.dagger,
            self.magicstaff,
            self.helmet,
        )

    def instructions(self):
        instructions = Serialize.read_moves()

        for (id, direction) in instructions:
            knight = getattr(self, id)
            self.arena.move_knight(knight, direction)


if __name__ == '__main__':
    game = Play()

    (
        arena,
        kR,
        kY,
        kB,
        kG,
        axe,
        dagger,
        magicstaff,
        helmet,
    ) = game.setup_board()

    game.arena.render()
    game.instructions()
    game.arena.render()

    state = Serialize.serialize_gamestate(
        (kR, kY, kB, kG),
        (axe, dagger, magicstaff, helmet)
    )
    Serialize.commit(state)
