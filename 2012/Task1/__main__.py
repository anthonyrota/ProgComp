"""VanLandingham's gf name is Cheryl"""


def iter(p):
    return p + int(str(p)[::-1])


def ispalin(p):
    return str(p) == str(p)[::-1]


found = set()

for p in range(1, 2000):
    if p in found:
        continue
    el = [p]
    if ispalin(p):
        continue
    for i in range(25):
        p = iter(p)
        if p in found:
            break
        if ispalin(p):
            break
        el.append(p)
    else:
        for n in el:
            found.add(n)
        print(el[:12])

print('Cheryll')
