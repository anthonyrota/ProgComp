import sys
from collections import defaultdict


# read file
file_name = sys.argv[1]
with open(file_name) as f:
    num_items, num_ranges = f.readline().strip().split(' ')
    num_items = int(num_items)
    r = int(num_ranges)
    letters = defaultdict(int)
    for i in range(num_items):
        thing = f.readline().strip()
        first_letter = thing[0].upper()
        letters[first_letter] += 1
    keys = list(letters.keys())
    lens = list(letters.values())
    n = len(lens)

    S = [sum(lens[i:]) for i in range(len(lens))]
    dp = [[None] * n for _ in range(n)]

    def solve(R):
        for i in range(r - R, n - R + 1):
            min_diff = 100000000
            for j in range(i + 1, n - R + 2):
                r1 = S[i] - S[j]
                r2_min, r2_max, idxs = dp[R-2][j]
                new_min = min(r1, r2_min)
                new_max = max(r1, r2_max)
                diff = new_max - new_min
                if diff < min_diff:
                    min_diff = diff
                    min_min = new_min
                    min_max = new_max
                    min_idxs = idxs
            dp[R-1][i] = (min_min, min_max, [i] + min_idxs)

    for i in range(r - 1, n):
        l = S[i]
        dp[0][i] = (l, l, [i])

    for i in range(2, r+1):
        solve(i)

    md = 1000000000
    for xmin, xmax, min_idxs in dp[r-1][:(n-r+1)]:
        d = xmax - xmin
        if d < md:
            md = d
            x = (xmax - xmin, min_idxs)

    d, min_idxs = x

    for k in range(len(min_idxs)):
        j = min_idxs[k]
        i = 0 if k == 0 else min_idxs[k - 1]+1
        print(f'{keys[i]}-{keys[j]}', S[i] - S[j] + lens[j])

    print(d, min_idxs, keys)
