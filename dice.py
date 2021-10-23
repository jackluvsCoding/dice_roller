import random


def die_roll(die_type: int, modifier: int):
    roll = random.SystemRandom().randint(1, die_type)
    print(f'd{die_type} = [{roll}] + {modifier} ({roll+modifier})')
