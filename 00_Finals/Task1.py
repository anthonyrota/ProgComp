import sys
from itertools import cycle

# read file
file_name = sys.argv[1]
with open(file_name) as f:
    l = []
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tests = l

for test in tests:
    basicvillages = []
    villages = []
    for i in test:
        villages.append(" ")
        villages.append(i)
        basicvillages.append(i)
    villages.append(" ")

    positions = []
    moves = []

    for pos in range(0, len(test)*2 + 2, 2):
        start = pos
        left = villages[:pos] + villages[pos:][::-1]
        right = villages[pos:] + villages[:pos]
        left = [x for x in left if x != " "]
        right = [x for x in right if x != " "]
        rightcount = 0
        leftcount = 0
        encounteredBlack = False
        encounteredGreen = False
        for a, i in enumerate(right):
            if a > len(test)//2:
                break
            if i == "H":
                rightcount += 1
                continue
            elif i == "B":
                if encounteredGreen == True:
                    break
                else:
                    encounteredBlack = True
                    rightcount += 1
                    continue
            elif i == "G":
                if encounteredBlack == True:
                    break
                else:
                    encounteredGreen = True
                    rightcount += 1
                    continue
        encounteredBlack = False
        encounteredGreen = False
        for a, i in enumerate(left):
            if a >= len(test)//2:
                break
            if i == "H":
                leftcount += 1
                continue
            elif i == "B":
                if encounteredGreen == True:
                    break
                else:
                    encounteredBlack = True
                    leftcount += 1
                    continue
            elif i == "G":
                if encounteredBlack == True:
                    break
                else:
                    encounteredGreen = True
                    leftcount += 1
                    continue
        count = leftcount + rightcount
        positions.append(pos/2)
        moves.append(count)
    basicvillages.insert(moves.index(max(moves)), " ")

    print("".join(basicvillages) +
          f" start {int(positions[moves.index(max(moves))])} visits {max(moves)}")
    print(" "*moves.index(max(moves)) + "^")
