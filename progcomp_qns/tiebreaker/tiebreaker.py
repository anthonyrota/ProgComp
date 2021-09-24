import sys
from math import floor


def combs(items, n):
    if n == 0:
        yield []
    for i, item in enumerate(items[:len(items) - n + 1]):
        for comb in combs(items[i + 1:], n - 1):
            yield [item] + comb


def solve(n, s, R):
    if n == 1:
        if R < 1:
            return []
        return [s]
    solutions = []
    for smallest in range(1, floor(s / n)):
        for largest in range(smallest + 1, floor(smallest * R) + 1):
            remaining = list(range(smallest + 1, largest))
            if len(remaining) < n - 2:
                continue
            for middle in combs(remaining, n - 2):
                numbers = [smallest] + list(middle) + [largest]
                if sum(numbers) != s:
                    continue
                subset_sums = [sum(subset) for i in range(1, n) for subset in combs(
                    numbers, i)]
                if len(set(subset_sums)) == len(subset_sums):
                    solutions.append(numbers)
    return solutions


if __name__ == '__main__' and len(sys.argv) > 1:
    solutions = solve(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
    solutions.sort()
    for solution in solutions:
        print(" ".join([str(n) for n in solution]))
