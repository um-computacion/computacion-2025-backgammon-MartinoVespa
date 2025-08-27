import random

def tirar_dados():
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    return [d1, d2]*2 if d1 == d2 else [d1, d2]

