import random


def die_roll(die_type: int):
    return random.SystemRandom(34633).randint(1, die_type)
