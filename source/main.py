#!/usr/bin/python3

"""
BOBNET - THE BRIDGE
Excellent work! Thanks to you, we have managed to hijack four motorbikes! Their source code has been modified to carry our virus back to Bobnet.

Bobnet's headquarters are on the other end of the next bridge, but a recent acid rain storm has gravely damaged the structural integrity of the road, leaving it scattered with many holes.
The motorbikes are perfectly capable of crossing the damaged bridge but, because of our virus, it's up to you to code the evasive maneuvers of the motorbikes.

Humankind is relying on you to see as many motorbikes safely across the bridge as possible!
"""
import sys
import math
from bike_ai import Bike_AI


def output(statement):
    print(statement, file=sys.stdout, flush=True)


def debug(statement):
    print(statement, file=sys.stderr, flush=True)


def main():
    debug("Start of simulation")

    m = int(input())  # the amount of motorbikes to control
    v = int(input())  # the minimum amount of motorbikes that must survive

    debug(f"m: {m}")
    debug(f"v: {v}")

    # L0 to L3 are lanes of the road. A dot character . represents a safe
    # space, a zero 0 represents a hole in the road.
    l0 = input()
    l1 = input()
    l2 = input()
    l3 = input()

    sim_data = {
        "total_bikes": m,
        "required_bikes": v,
        "lanes": [
            list(l0),
            list(l1),
            list(l2),
            list(l3),
        ],
    }

    bike_ai = Bike_AI(sim_data)

    # game loop
    while True:
        active_bikes = False
        s = int(input())  # the motorbikes' speed

        run_data = {"speed": s, "bikes": []}

        for i in range(m):
            # x: x coordinate of the motorbike
            # y: y coordinate of the motorbike
            # a: indicates whether the motorbike is activated "1" or detroyed "0"
            x, y, a = [int(j) for j in input().split()]
            debug(f"x: {x}, y: {y}, a: {a}")
            run_data["bikes"].append([x, y, a])
            if a > 0:
                active_bikes = True
        if not active_bikes:
            debug("Exit: no more active_bikes")
            break

        command = bike_ai.process(run_data)
        if command == "":
            debug("Exit: end of commands")
            break
        else:
            output(command)

    debug("End of simulation")


if __name__ == "__main__":
    main()
