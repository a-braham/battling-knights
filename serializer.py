from pathlib import Path
from json import dumps


class Serialize:
    @staticmethod
    def read_moves():
        _contents = Path('./moves.txt').read_text()
        moves = _contents.strip().split('\n')
        if moves[0] == 'GAME-START':
            moves.pop(0)
        if moves[-1] == 'GAME-END':
            moves.pop()
        return tuple(tuple(m.split(':')) for m in moves)

    @staticmethod
    def serialize_gamestate(knights: list, items: list):
        result = {}

        for knight in knights:
            result = (
                knight.pos.to_json() if knight.pos else None, knight.status
            )
            if knight.equipped:
                result += (
                    knight.equipped.name,
                    knight.attack + knight.equipped.attack,
                    knight.defence + knight.equipped.defence,
                )
            else:
                result += (None, knight.attack, knight.defence)
            result[knight.color] = result

        for item in items:
            result = (item.pos.to_json(), item.pos.knight is not None)
            result[item.name] = result

        return result

    @staticmethod
    def commit(state):
        return Path('./final_state.json').write_text(dumps(state))
