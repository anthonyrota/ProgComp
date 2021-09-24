import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    num = int(line)
    mins = num % 100
    h = num // 100
    dist = 30 - mins
    abs_dist = abs(dist)
    x = line.rstrip() + ' is'
    p = ''
    if abs_dist == 0:  # 1st branch
        x += ' half'
        p = ' past'
    elif abs_dist == 15:  # 2nd branch
        x += ' a quarter'
        p = ' past'
    elif abs_dist == 29:  # 3rd branch
        x += ' 1 minute'
        p = ' past'
    elif mins > 0:  # 4th branch
        x += f' {30-abs_dist} minutes'
        p = ' past'
    if dist >= 0:  # 5th branch
        x += p
        target = h
    else:
        x += ' to'
        target = h+1
    dist = abs(mins - 30)
    target %= 24
    if target == 0:  # 6th branch
        x += ' 12 midnight'
    elif target == 12:  # 7th branch
        x += ' 12 noon'
    elif target < 12:  # 8th branch
        x += f' {target}am'
    else:
        x += f' {target-12}pm'
    print(x)
