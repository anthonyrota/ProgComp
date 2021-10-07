def dp(n):
    return str(f'{n:.6f}')


val = 0
k = 1


def update_val():
    global val, k
    val += ((-1)**(k+1))*(k**2)/(k**3+1)
    k += 1


for k in range(10000000):
    update_val()
d1 = dp(val)
update_val()
d2 = dp(val)
if d1 == d2:
    print('SUCCESS!')
    print(d1)
else:
    print('FAIL! need more terms...', d1, d2)
