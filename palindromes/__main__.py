import sys
import string


def isp(s):
    return s == s[::-1]


n = int(sys.stdin.readline())
for _ in range(n):
    l = sys.stdin.readline().strip()
    lp = ''.join(s for s in l.lower()
                 if s in string.ascii_lowercase)
    if isp(lp):
        print(f'Yes "{l}"')
    else:
        print(f' No "{l}"')
