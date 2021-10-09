
import itertools


def gen(n):
    trestles = []
    start = 10**(n-1)
    end = 10**n
    for i in range(start, end):
        for j in range(i, end):
            if (i % 10 == 0 and j % 10 == 0):
                continue
            prod = i * j
            if len(str(prod)) != (n*2):
                continue
            for num in set(itertools.permutations(list(str(i) + str(j)))):
                if num[0] == '0':
                    continue
                if prod == int(''.join(num)):
                    trestles.append((''.join(num), i, j))
    trestles.sort(key=lambda x: x[0])
    return trestles


def print_parallel(trestles, n, a):
    print(' '.join([x[0] for x in trestles]))
    if a == 2:
        print(' '.join([str(x[1])[0] + (' ' * n) + str(x[2])[0]
                        for x in trestles]))
        print(' '.join([str(x[1])[1] + (' ' * n) + str(x[2])[1]
                        for x in trestles]))
    elif a == 3:
        print(' '.join([str(x[1])[0] + (' ' * n) + str(x[2])[0]
                        for x in trestles]))
        print(' '.join([str(x[1])[1] + (' ' * n) + str(x[2])[1]
                        for x in trestles]))
        print(' '.join([str(x[1])[2] + (' ' * n) + str(x[2])[2]
                        for x in trestles]))


trestles = gen(2)
print_parallel(trestles, 2, 2)

trestles = gen(3)

print()
for i in range(0, len(trestles), 10):
    L = [x[0] for x in trestles[i:i+10]]
    print(' '.join(L))

print()
print('Total 6 digit:', len(trestles))

seen = set()
for n in trestles:
    if n[0] in seen:
        duplicate = n
        break
    seen.add(n[0])

ways = []
for n in trestles:
    if n[0] == duplicate[0]:
        ways.append(n)

print()
print_parallel(ways, 4, 3)
