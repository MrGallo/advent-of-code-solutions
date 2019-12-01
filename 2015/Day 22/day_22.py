from typing import List, Tuple


SPELLS = [
    ("Magic Missile", 53),
    ("Drain", 73),
    ("Shield", 113),
    ("Poison", 173),
    ("Recharge", 229)
]

# incomplete
# win
# loss


def check_outcome(spell_list: List, player: List, enemy: List, hard_mode_active: bool = False) -> str:
    p_health, p_mana, p_armor, p_shield, p_poison, p_recharge = player
    e_health, e_damage = enemy

    for spell in spell_list:
        spell_name, spell_mana = spell

        if p_mana < spell_mana:
            return "loss"
        
        if hard_mode_active is True:
            p_health -= 1
            if p_health < 1:
                return "loss"

        # apply effects
        if p_shield:
            p_shield -= 1
            p_armor = 7
        else:
            p_armor = 0
        if p_poison:
            p_poison -= 1
            e_health -= 3
        if p_recharge:
            p_recharge -= 1
            p_mana += 101
        
        # player casts spell
        p_mana -= spell_mana
        if spell_name == "Magic Missile":
            e_health -= 4
        elif spell_name == "Drain":
            e_health -= 2
            p_health += 2
        elif spell_name == "Shield":
            if p_shield:
                return "loss"
            p_shield = 6
        elif spell_name == "Poison":
            if p_poison:
                return "loss"
            p_poison = 6
        elif spell_name == "Recharge":
            if p_recharge:
                return "loss"
            p_recharge = 5
        
        # Boss turn
        # apply effects
        if p_shield:
            p_shield -= 1
            p_armor = 7
        else:
            p_armor = 0
        if p_poison:
            p_poison -= 1
            e_health -= 3
        if p_recharge:
            p_recharge -= 1
            p_mana += 101
        
        damage = max(e_damage - p_armor, 1)
        p_health -= damage

        if e_health < 1:
            return "win"
        elif p_health < 1:
            return "loss"
    
    return "incomplete"


def find_first_win(player: List, enemy: List, hard_mode_active: bool = False):
    queue = [[spell] for spell in SPELLS]
    while queue:
        spell_list = queue.pop(0)
        for spell in SPELLS:
            potential_spell_list = spell_list + [spell]
            result = check_outcome(potential_spell_list, player[:], enemy[:], hard_mode_active)
            if result == "win":
                return potential_spell_list
            elif result == "incomplete":  # add to queue
                queue.append(potential_spell_list)
            elif result == "loss":
                pass  # don't go down that branch


player = [50, 500, 0, 0, 0, 0]
enemy = [51, 9]

# part 1
first_win = find_first_win(player, enemy)
mana_spent = sum([mana for name, mana in first_win])
print(mana_spent)  # answer: 900


# part 2
first_win = find_first_win(player, enemy, hard_mode_active=True)
mana_spent = sum([mana for name, mana in first_win])
print(mana_spent)  # answer: 900