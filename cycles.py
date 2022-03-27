from lum_chars import lums, r_lums
import delay

def cycle_one(base, helix):      
    while base < helix:

        print(" "*(45-base), end="")
        print(lums[:base], end="")
        print(r_lums[base::-1], end="")

        delay.time_delay(0.1)
        base += 1
    return base


def cycle_two(helix):   
    while helix > 0:

        print(" "*(45-helix), end="")
        print(lums[:helix], end="")
        print(r_lums[helix::-1], end="")

        delay.time_delay(0.1)
        helix -= 1
    return helix


def cycle_three(base, helix):  
    while helix < base:
        print(" "*(45-helix), end="")
        print(r_lums[:helix], end="")
        print(lums[helix::-1], end="")

        delay.time_delay(0.1)
        helix += 1
    return helix
        
def cycle_four(base):  

    while base > 0:

        print(" "*(45-base), end="")
        print(r_lums[:base], end="")
        print(lums[base::-1], end="")

        delay.time_delay(0.1)
        base -= 1
    return base