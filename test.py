import unittest
from arena import Arena
from knight import Knight
from item import Item
from position import Position
from fight import Fight


class TestBattlingKnights(unittest.TestCase):

    def setUp(self):
        self.arena = Arena()
        ab = self.arena.board

        self.knight1 = Knight('K1', 'red', ab[0][0])
        self.knight2 = Knight('K2', 'blue', ab[7][7])

        ab[0][0].knight = self.knight1
        ab[7][7].knight = self.knight2

        self.item1 = Item('Item1', 1, ab[1][1], 1, 1)
        self.item2 = Item('Item2', 2, ab[6][6], 2, 2)

        ab[1][1].items.append(self.item1)
        ab[6][6].items.append(self.item2)

    def test_move_knight_invalid_direction(self):
        with self.assertRaises(Exception):
            self.arena.move_knight(self.knight1, 'X')

    def test_move_knight_to_square_with_item(self):
        self.arena.move_knight(self.knight1, 'E')
        self.arena.move_knight(self.knight1, 'S')
        self.assertEqual(self.knight1.equipped, self.item1)

    def test_attack(self):
        self.knight1.attack = 2
        self.knight2.defence = 1
        winner, loser = Fight.attack(self.knight1, self.knight2)
        self.assertEqual(winner, self.knight1)
        self.assertEqual(loser, self.knight2)

    def test_kill(self):
        loot, last_pos = Fight.kill(self.knight1)
        self.assertIsNone(self.knight1.pos)
        self.assertIsNone(self.knight1.equipped)
        self.assertEqual(self.knight1.attack, 0)
        self.assertEqual(self.knight1.defence, 0)
        self.assertEqual(loot, None)

    def test_drop_loot(self):
        loot = Item('Loot', 3, self.knight1.pos, 3, 3)
        self.arena.drop_loot(loot, self.knight1.pos)
        self.assertEqual(self.knight1.pos.items, [loot])

    def test_drop_loot_empty_item_list(self):
        loot = Item('Loot', 3, self.knight1.pos, 3, 3)
        self.arena.drop_loot(loot, self.knight1.pos)
        self.assertEqual(self.knight1.pos.items, [loot])
        self.assertEqual(self.knight1.pos.items[0].name, 'Loot')

    def test_drop_loot_nonempty_item_list(self):
        loot1 = Item('Loot1', 3, self.knight1.pos, 3, 3)
        loot2 = Item('Loot2', 2, self.knight1.pos, 2, 2)
        self.arena.drop_loot(loot1, self.knight1.pos)
        self.arena.drop_loot(loot2, self.knight1.pos)
        self.assertEqual(self.knight1.pos.items, [loot2, loot1])
        self.assertEqual(self.knight1.pos.items[0].name, 'Loot2')

    def test_direction_to_pos(self):
        pos = self.arena._direction_to_pos('E', Position(1, 1))
        self.assertEqual(pos, Position(1, 2))

    def test_direction_to_pos_out_of_bounds(self):
        with self.assertRaises(Exception):
            self.arena._direction_to_pos('W', Position(0, 0))

    def test_is_empty_square_empty(self):
        pos = Position(2, 2)
        self.assertTrue(self.arena._is_empty_square(pos))

    def test_is_empty_square_with_knight(self):
        pos = Position(0, 0, self.knight1)
        self.assertFalse(self.arena._is_empty_square(pos))

    def test_is_empty_square_with_item(self):
        pos = Position(2, 2, None, [self.item1])
        self.assertFalse(self.arena._is_empty_square(pos))

    def test_is_square_with_item_with_item(self):
        pos = Position(2, 2, None, [self.item1])
        self.assertTrue(self.arena._is_square_with_item(pos))

    def test_is_square_with_item_empty(self):
        pos = Position(2, 2, None, [])
        self.assertFalse(self.arena._is_square_with_item(pos))

    def test_is_square_with_knight_with_knight(self):
        pos = Position(0, 0, self.knight1)
        self.assertTrue(self.arena._is_square_with_knight(pos))

    def test_is_square_with_knight_empty(self):
        pos = Position(0, 0, None)
        self.assertFalse(self.arena._is_square_with_knight(pos))


if __name__ == '__main__':
    unittest.main()
