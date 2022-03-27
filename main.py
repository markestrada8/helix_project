import random
import cycles
from lum_chars import lums, r_lums

# VISUALIZATION


def helix():
    helix_on = True

    while helix_on:
        base = 1
        helix = random.randint(0, 45)
        base = cycles.cycle_one(base, helix)
        helix = cycles.cycle_two(helix)
        helix = cycles.cycle_three(base, helix)
        base = cycles.cycle_four(base)


helix()
