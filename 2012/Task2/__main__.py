import sys
from math import floor

a = 6423135
m = 16777213

S = 1
i = 0
u = S / m


def myrand():
    global i, S, u
    i += 1
    S = (a*S) % m
    u = S / m
    return u


def myrandint(N):
    myrand()
    return floor(u * N)


perm = ['car', 'goat', 'goat']


def myrandperm(N):
    global perm
    for pos in range(0, N-1):
        r = myrandint(N-pos)
        perm[pos], perm[pos+r] = perm[pos+r], perm[pos]


for i in range(10):
    myrandperm(3)
    print(' '.join(perm))


S = 1
i = 0
u = S / m

counts = [0] * 3

dormousepoints = 0
alicepoints = 0
hatterpoints = 0

for i in range(1500):
    myrandperm(3)
    car_idx = perm.index('car')
    counts[car_idx] += 1
    dormouse_door = myrandint(3)
    if dormouse_door == car_idx:
        door_idxs = list(set((0, 1, 2)) - set((car_idx,)))
        open_idx = door_idxs[myrandint(2)]
    else:
        open_idx = next(iter(set((0, 1, 2)) - set((dormouse_door, car_idx))))
    hatter_door = next(iter(set((0, 1, 2)) - set((dormouse_door, open_idx))))
    alice_door = [dormouse_door, hatter_door][myrandint(2)]
    if dormouse_door == car_idx:
        dormousepoints += 1
    else:
        hatterpoints += 1
    if alice_door == car_idx:
        alicepoints += 1


print('Appears behind first door', counts[0], "times")
print('Appears behind second door', counts[1], "times")
print('Appears behind third door', counts[2], "times")
print('Dormouse points:', dormousepoints)
print('Alice points:', alicepoints)
print('Hatters points:', hatterpoints)
