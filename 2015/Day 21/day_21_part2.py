from typing import List


boss_stats = """Hit Points: 104
Damage: 8
Armor: 1"""

class Character:
    def __init__(self, health: int, damage: int, armor: int):
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def attack(self, other: "Character") -> None:
        other.health -= max(self.damage - other.armor, 1)


class Player(Character):
    def __init__(self):
        super().__init__(100, 0, 0)
        self._inventory = []
        self.total_spent = 0
    
    def equip(self, item: List[int]) -> None:
        cost, dam, arm = item
        self.total_spent += cost
        self.damage += dam
        self.armor += arm
        self._inventory.append(item)
    

weapons = [  # pick one
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]

armors = [  # pick 0 or one
    [0, 0, 0],
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5]
]

rings = [  # pick 0-2
    [0, 0, 0],
    [0, 0, 0],
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3]
]

highest_cost = None
for weapon in weapons:
    for armor in armors:
        for i, first_ring in enumerate(rings):
            for second_ring in rings[i+1:]:
                boss = Character(104, 8, 1)
                player = Player()
                player.equip(weapon)
                player.equip(armor)
                player.equip(first_ring)
                player.equip(second_ring)

                if highest_cost is not None and highest_cost > player.total_spent:
                    continue
                
                # do the battle
                while True:
                    player.attack(boss)
                    if boss.health < 1:  # victory
                        break
                    
                    boss.attack(player)
                    if player.health < 1:  # defeat
                        if highest_cost is None or player.total_spent > highest_cost:
                            highest_cost = player.total_spent
                        break

print(highest_cost)

# answer: 148