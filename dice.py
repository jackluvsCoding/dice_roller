import random


def die_roll(die_type: int):
    return random.SystemRandom().randint(1, die_type)
