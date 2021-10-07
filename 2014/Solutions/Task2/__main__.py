import sys

letters = set(('V', 'S', 'D'))


def solve(n, start, end):
    if n == 1:
        return [start, end]
    if n == 2:
        return [f'{start} {end}', f'{end} {end}']
    medium = next(iter(letters - set((start, end))))
    lines = []
    to_left = solve(n - 1, start, medium)
    to_left = [line + f' {start}' for line in to_left]
    lines += to_left
    lines += [(f'{medium} ' * (n - 1)) + end]
    to_left = solve(n - 1, medium, end)
    to_left = [line + f' {end}' for line in to_left]
    lines += to_left
    return lines


n = int(sys.argv[1])
print(' '.join(['V'] * n))
for line in solve(n, 'V', 'S'):
    print(line)
