import sys


def t(s):
    a = set(s)
    if len(s) == 0 or len(a) != len(a & set('MDCLXVI')):
        print(f'Bad1 {s}')
        return
    symbols = {
        'M': (1000, False),
        'D': (500, False),
        'C': (100, True),
        'L': (50, False),
        'X': (10, True),
        'V': (5, False),
        'I': (1, True)
    }
    is_last_compound = False
    prev_comp_term_first_sym_v = 0
    v = 0
    i = 0
    tvs = []
    while True:
        a = s[i]
        if i == len(s)-1:
            if is_last_compound and symbols[a][0] >= prev_comp_term_first_sym_v:
                print(f'Bad3 {s}')
                return
            v += symbols[a][0]
            break
        b = s[i+1]
        if symbols[b][0] > symbols[a][0]:
            if not symbols[a][1]:
                print(f'Bad2 {s}')
                return
            is_last_compound = True
            prev_comp_term_first_sym_v = symbols[a][0]
            tv = symbols[b][0] - symbols[a][0]
            v += tv
            tvs.append(tv)
            i += 2
            if i == len(s):
                break
            continue
        if is_last_compound and symbols[a][0] >= prev_comp_term_first_sym_v:
            print(f'Bad3 {s}')
            return
        v += symbols[a][0]
        tvs.append(symbols[a][0])
        is_last_compound = False
        i += 1
    if list(reversed(tvs)) != list(sorted(reversed(tvs))):
        print(f'Bad2 {s}')
        return
    print(v, s)


n = int(sys.stdin.readline())
for _ in range(n):
    t(sys.stdin.readline().strip())
