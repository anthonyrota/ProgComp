def encode(g):
    k, r = 0, 0
    for c_str in g:
        c = int(c_str)
        d = (3*c+7) % 10
        r += 2**(3*d+2)+k*(8**d)
        k += 1
    return r


def match(gcode, scode):
    b = ""
    c = ""
    for k in range(0, 10):
        p = (gcode // (8**k)) % 8
        q = (scode // (8**k)) % 8
        r = p - q
        s = 2*r + 3*q
        if s > 11 and s > 2*r:
            if s == 3*p:
                b += "B"
            else:
                c += "C"
    return b + c


def solve(encoding):
    candidates = [str(i).zfill(4)
                  for i in range(10000) if len(set(str(i).zfill(4))) == 4]
    print(f'Initial candidate list size = {len(candidates)}')
    n = 1
    while True:
        candidates_left = len(candidates)
        guess = candidates[candidates_left // 2]
        encoded_guess = encode(guess)
        target = match(encoded_guess, encoding)
        candidates = [c for c in candidates if match(
            encoded_guess, encode(c)) == target]
        print(
            f'Guess {n} {guess} gives {target.ljust(4)} Candidates remaining: {len(candidates)}')
        if len(candidates) == 1:
            print('Solution:', candidates[0])
            break
        n += 1


print(encode("0586"))
print(match(941099524, 939547652))
solve(216616)
solve(12748856)
