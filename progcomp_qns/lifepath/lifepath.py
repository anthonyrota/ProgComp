import sys


def calc(day, month, year):
    def reduce(n, c=False):
        if n % 11 == 0 and (not c):
            return n
        s = sum(map(int, str(n)))
        if s > 9:
            return reduce(s)
        return s

    day_r = reduce(day)
    month_r = reduce(month)
    year_r = reduce(year, True)
    s = day_r+month_r+year_r
    if s % 11 == 0:
        return s
    return reduce(s)


num_lines = int(sys.stdin.readline())
for _ in range(num_lines):
    date = sys.stdin.readline().strip()
    day, month, year = date.split('/')
    print(calc(int(day), int(month), int(year)), date)
