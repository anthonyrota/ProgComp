import math
target = 100/99


def p1():
    def L(x):
        return math.sqrt(x**3-x**2+3*x)/(math.sqrt(x**3)-math.sqrt(x**2)+math.sqrt(3*x))
    print(L())

# def function(x): return math.sqrt(x**3 - x**2 + 3*x) / \
#     (math.sqrt(x**3)-math.sqrt(x**2)+math.sqrt(3*x))


# trueval = 100/99


# def bisection(f, a, b, N, trueval):
#     if f(a)*f(b) >= trueval:
#         print("Bisection method fails.")
#         return None
#     an = a
#     bn = b
#     for n in range(1, N+1):
#         mn = (an + bn)/2
#         fmn = f(mn)
#         if f(an)*fmn < trueval:
#             an = an
#             bn = mn
#         elif f(bn)*fmn < trueval:
#             a_n = mn
#             b_n = bn
#         elif fmn == trueval:
#             print("Found exact solution.")
#             return mn
#         else:
#             print("Bisection method fails.")
#             return None
#     return (an + bn)/2


# approxlim = bisection(function, 1, 2, 1, trueval)
# print(approxlim)
