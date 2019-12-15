from typing import List, Dict, DefaultDict, Tuple
from collections import defaultdict


class Container:
    def __init__(self, id: int):
        self.id = id
        self.cargo = []

    @classmethod
    def get_or_create(cls, container_id: int) -> 'Container':
        try:
            return cls.objects[container_id]
        except KeyError:
            return cls(container_id)


class Bot(Container):
    objects = {}

    def __init__(self, id):
        super().__init__(id)
        self.high = None
        self.low = None
        Bot.objects[self.id] = self

    def do_hand_off(self: 'Bot') -> None:
        if len(self.cargo) < 2:
            return

        # part 1
        if set(self.cargo) == set([17, 61]):
            print(self.id)  # answer: 47

        a, b = self.cargo
        if b < a:
            a, b = b, a

        self.low.cargo.append(a)
        if type(self.low) is Bot:
            self.low.do_hand_off()

        self.high.cargo.append(b)
        if type(self.high) is Bot:
            self.high.do_hand_off()


class Output(Container):
    objects = {}

    def __init__(self, id):
        super().__init__(id)
        Output.objects[self.id] = self


with open("input.txt", "r") as f:
    instructions = f.read().split("\n")


for ins in instructions:
    words = ins.split()
    if ins.startswith("value"):
        chip_num = int(words[1])
        bot_id = int(words[-1])
        bot = Bot.get_or_create(bot_id)
        bot.cargo.append(chip_num)
    else:
        bot_id = int(words[1])
        bot = Bot.get_or_create(bot_id)
        low_type = words[5]
        low_id = int(words[6])
        high_type = words[10]
        high_id = int(words[11])

        if low_type == "output":
            bot.low = Output.get_or_create(low_id)
        else:
            bot.low = Bot.get_or_create(low_id)

        if high_type == "output":
            bot.high = Output.get_or_create(high_id)
        else:
            bot.high = Bot.get_or_create(high_id)


start_bot = None
for id, bot in sorted(Bot.objects.items()):
    if len(bot.cargo) == 2:
        start_bot = bot

start_bot.do_hand_off()

# part 2
total = 1
for i in range(3):
    total *= Output.objects[i].cargo[0]

print(total)  # ansert: 2666
