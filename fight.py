class Fight:
    @staticmethod
    def attack(attacker, defendant):
        attack_score = attacker.attack + 0.5
        defend_score = defendant.defence

        if attacker.equipped:
            attack_score += attacker.equipped.attack

        if defendant.equipped:
            defend_score += defendant.equipped.defence

        return (
            (attacker, defendant)
            if attack_score > defend_score
            else (defendant, attacker)
        )

    @staticmethod
    def kill(knight, status=1):
        loot = knight.equipped
        last_pos = knight.pos

        knight.update_status(status)
        knight.pos = None
        knight.equipped = None
        knight.attack = 0
        knight.defence = 0

        return loot, last_pos
