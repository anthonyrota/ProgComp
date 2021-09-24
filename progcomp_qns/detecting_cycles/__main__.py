def gen(current, a, b, c):
    return (a*current*current + b) % c


def cycle(a, b, c, d):
    x = d
    xs = [x]
    while True:
        x = gen(x, a, b, c)
        if x in xs:
            idx = xs.index(x)
            print(xs)
            print(f'repeat = {x}, string = {idx}, cycle = {len(xs) - idx}')
            return
        xs.append(x)


cycle(1, 3, 100, 11)
cycle(5, 5, 8888, 88)
cycle(1, 9, 666, 10)
cycle(1, 1, 31, 1)
