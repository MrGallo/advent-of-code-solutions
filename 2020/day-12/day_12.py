from typing import List, Tuple


class Ship:
    DIRECTIONS = ['E', 'S', 'W', 'N']

    DIRECTION_VECTORS = {
        'E': (1, 0), 
        'S': (0, 1),
        'W': (-1, 0),
        'N': (0, -1)
    }

    def __init__(self, instructions: List[Tuple[str, int]]):
        self.instructions = instructions
        self.x = 0
        self.y = 0
        self.direction = 0
        self.dx = self.dy = None
        self.change_direction(0)

        self.MOVEMENT_FUNCS = {
            'N': self.cardinal_move('N'),
            'E': self.cardinal_move('E'),
            'W': self.cardinal_move('W'),
            'S': self.cardinal_move('S'),
            'L': self.left,
            'R': self.right,
            'F': self.forward
        }
    
    def change_direction(self, change: int) -> None:
        """CW +1, CCW +3"""
        self.direction = (self.direction + change) % len(Ship.DIRECTIONS)
        self.dx, self.dy = Ship.DIRECTION_VECTORS[Ship.DIRECTIONS[self.direction]]
    
    def right(self, amount: int):
        units = amount // 90
        self.change_direction(units)
    
    def left(self, amount: int):
        self.right(amount * 3)
    
    def forward(self, amount: int):
        self.x += self.dx * amount
        self.y += self.dy * amount
    
    def cardinal_move(self, direction: str):
        def inner(amount: int):
            dx, dy = Ship.DIRECTION_VECTORS[direction]
            self.x += dx * amount
            self.y += dy * amount
        return inner

    def execute(self, ins: Tuple[str, int]):
        movement, amount = ins
        self.MOVEMENT_FUNCS[movement](amount)
    

    def execute_instructions(self):
        for ins in self.instructions:
            self.execute(ins)


class ShipWithWaypoint(Ship):
    def __init__(self, instructions: List[Tuple[str, int]]):
        super().__init__(instructions)
        self.x = 10
        self.y = -1
        self.ship_x = 0
        self.ship_y = 0
    
    def forward(self, amount: int):
        self.ship_x += self.x * amount
        self.ship_y += self.y * amount
    
    def change_direction(self, times: int):
        """Rotate clockwise 90 degrees.
        
        Args:
            times: number of times to rotate 90 degrees CW.
        """
        for _ in range(times):
            self.x, self.y = -self.y, self.x


def main():
    with open('input.txt', 'r') as f:
        instructions = [(line[0], int(line[1:])) for line in f.readlines()]
    
    ship = Ship(instructions)
    ship.execute_instructions()
    print(abs(ship.x) + abs(ship.y))  # Part 1: 319

    ship2 = ShipWithWaypoint(instructions)
    ship2.execute_instructions()
    print(abs(ship2.ship_x) + abs(ship2.ship_y))  # Part 2: 50157



def tests():
    s = Ship([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
    assert s.direction == 0
    assert s.dx == 1
    assert s.dy == 0

    s.right(90)
    assert s.direction == 1
    assert s.dx == 0
    assert s.dy == 1


    s.left(360)
    assert s.direction == 1
    assert s.dx == 0
    assert s.dy == 1

    s.left(90)
    assert s.direction == 0
    assert s.dx == 1
    assert s.dy == 0

    s.forward(10)
    assert s.x == 10
    assert s.y == 0

    s.right(90)
    s.forward(10)
    assert s.x == 10
    assert s.y == 10

    s.left(180)
    s.forward(10)
    assert s.x == 10
    assert s.y == 0

    s.cardinal_move('W')(10)
    assert s.x == 0
    assert s.y == 0

    s.cardinal_move('E')(10)
    assert s.x == 10
    assert s.y == 0

    s.cardinal_move('N')(10)
    assert s.x == 10
    assert s.y == -10

    s.cardinal_move('S')(10)
    assert s.x == 10
    assert s.y == 0


    s = Ship([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
    s.execute(('F', 10))
    assert s.x == 10
    assert s.y == 0

    s = Ship([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
    s.execute_instructions()
    assert s.x == 17
    assert s.y == 8

    swwp = ShipWithWaypoint([])
    assert swwp.x == 10
    assert swwp.y == -1
    
    swwp.execute(('F', 10))
    assert swwp.ship_x == 100
    assert swwp.ship_y == -10

    swwp.execute(('N', 3))
    assert swwp.x == 10
    assert swwp.y == -4
    
    swwp.execute(('F', 7))
    assert swwp.ship_x == 170
    assert swwp.ship_y == -38
    
    swwp.execute(('R', 90))
    assert swwp.ship_x == 170
    assert swwp.ship_y == -38
    assert swwp.x == 4
    assert swwp.y == 10
    
    swwp.execute(('F', 11))
    assert swwp.ship_x == 214
    assert swwp.ship_y == 72

    swwp = ShipWithWaypoint([])
    swwp.x = 5
    swwp.y = 0
    swwp.left(90)
    assert swwp.x == 0
    assert swwp.y == -5
    swwp.left(90)
    assert swwp.x == -5
    assert swwp.y == 0
    swwp.left(90)
    assert swwp.x == 0
    assert swwp.y == 5

if __name__ == "__main__":
    tests()
    main()