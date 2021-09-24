import sys


alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def solve_problem(positions):
    print(' '.join(list(alph[:len(positions)])))
    new_positions = [None] * len(positions)
    for i, x in enumerate(positions):
        if x != 0:
            new_positions[x-1] = alph[i]
    empty = [i for i, x in enumerate(new_positions) if x is None]
    for i, x in enumerate(positions):
        if x == 0:
            new_positions[empty.pop(0)] = alph[i]
    print(' '.join(new_positions))


num_lines = int(sys.stdin.readline())
for i in range(num_lines):
    line = sys.stdin.readline().strip()
    solve_problem([int(n) for n in line.split(' ')[1:]])
    if i != num_lines - 1:
        print()
