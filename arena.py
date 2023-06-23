from operator import attrgetter

from fight import Fight
from position import Position


class Drowned(Exception):
    pass


class Arena:
    def __init__(self):
        board = []
        for y in range(0, 8):
            row = [Position(y, x) for x in range(0, 8)]
            board.append(tuple(row))

        self.board = tuple(board)

    def move_knight(self, knight, direction):
        knight.pos.knight = None
        try:
            _pos = self._direction_to_pos(direction, knight.pos)
        except Drowned:
            loot, last_pos = Fight.kill(knight, status=2)
            print('Drowned', knight)
            if self.drop_loot(loot, last_pos):
                print('')
                print('Loot dropped:', loot)
        else:
            if self._is_square_with_knight(_pos):
                winner, loser = Fight.attack(knight, _pos.knight)
                self._move_knight_pos(winner, _pos)
                loot, last_pos = Fight.kill(loser)
                print('')
                print('Knights fighting')
                print('Winner:', winner)
                print('Loser:', loser)
                print('')
                if self.drop_loot(loot, last_pos):
                    print('')
                    print('Loot dropped:', loot)
                return winner

            if self._is_empty_square(_pos):
                self._move_knight_pos(knight, _pos)
                print('Moved', knight)
            elif self._is_square_with_item(_pos):
                self._move_knight_pos(knight, _pos)
                _pos.items.sort(key=attrgetter('rank'))
                if not knight.equipped:
                    knight.equipped = _pos.items.pop()
                    print('')
                    print('Acquired', knight.equipped)

            return knight

    def drop_loot(self, item, pos):
        if item:
            item.pos = pos
            pos.items.append(item)
            pos.items.sort(key=attrgetter('rank'))
            return True

    def _move_knight_pos(self, knight, pos):
        knight.pos = pos
        pos.knight = knight
        if knight.equipped:
            knight.equipped.pos = pos

    def render(self):
        for row in self.board:
            for pos in row:
                if pos.knight:
                    print(pos.knight.id, end='')
                elif len(pos.items):
                    print(pos.items[0].name[0] if pos.items[0] else '', end='')
                else:
                    print('  ', end='')
            print('')
        print('')

    def _direction_to_pos(self, direction: str, old_pos: Position):
        dir_map = {
            'N': (old_pos.y - 1, old_pos.x),
            'S': (old_pos.y + 1, old_pos.x),
            'E': (old_pos.y, old_pos.x + 1),
            'W': (old_pos.y, old_pos.x - 1),
        }
        y, x = dir_map[direction]

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise Drowned('Knight drowned')

        return self.board[y][x]

    def _is_empty_square(self, pos):
        return not pos.knight and len(pos.items) == 0

    def _is_square_with_item(self, pos):
        return len(pos.items) > 0

    def _is_square_with_knight(self, pos):
        return pos.knight is not None
