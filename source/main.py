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


def output(statement):
    print(statement, file=sys.stdout, flush=True)


def debug(statement):
    print(statement, file=sys.stderr, flush=True)


debug(f"main.py invoked")
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

debug(f"l0 parse: {list(l0)}")

debug(f"l0 {l0}")
debug(f"l1 {l1}")
debug(f"l2 {l2}")
debug(f"l3 {l3}")

s = int(input())  # the motorbikes' speed
for i in range(m):
    # x: x coordinate of the motorbike
    # y: y coordinate of the motorbike
    # a: indicates whether the motorbike is activated "1" or detroyed "0"
    x, y, a = [int(j) for j in input().split()]
    debug(f"x: {x}, y: {y}, a: {a}")

# # game loop
# while True:
#     print(f"l0 {l0}", file=sys.stderr, flush=True)
#     print(f"l1 {l1}", file=sys.stderr, flush=True)
#     print(f"l2 {l2}", file=sys.stderr, flush=True)
#     print(f"l3 {l3}", file=sys.stderr, flush=True)
#     print(f"-------------", file=sys.stderr, flush=True)
#     s = int(input())  # the motorbikes' speed
#     for i in range(m):
#         # x: x coordinate of the motorbike
#         # y: y coordinate of the motorbike
#         # a: indicates whether the motorbike is activated "1" or detroyed "0"
#         x, y, a = [int(j) for j in input().split()]

#     # Write an action using print
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)


#     # A single line containing one of 6 keywords: SPEED, SLOW, JUMP, WAIT, UP, DOWN.
#     print("SPEED")

output("SPEED")
debug(f"main.py closed")
