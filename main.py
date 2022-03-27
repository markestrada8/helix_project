import random
import time
# VISUALIZATION
lums = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
r_lums = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."


def helix():
    helix_on = True

    while helix_on:
        base = 1
        helix = random.randint(0, 45)
        while base < helix:

            print(" "*(45-base), end="")
            print(lums[:base], end="")
            print(r_lums[base::-1], end="")

            print(" ")
            time.sleep(0.1)
            base += 1

        while helix > 0:

            print(" "*(45-helix), end="")
            print(lums[:helix], end="")
            print(r_lums[helix::-1], end="")

            print("")
            time.sleep(0.1)
            helix -= 1

        while helix < base:
            print(" "*(45-helix), end="")
            print(r_lums[:helix], end="")
            print(lums[helix::-1], end="")

            print(" ")
            time.sleep(0.1)
            helix += 1

        while base > 0:

            print(" "*(45-base), end="")
            print(r_lums[:base], end="")
            print(lums[base::-1], end="")

            print("")
            time.sleep(0.1)
            base -= 1


helix()
