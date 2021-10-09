# READ LINES FROM FILE
import sys
# ...
num_lines = int(sys.stdin.readline())
for i in range(num_lines):
    line = sys.stdin.readline().strip()

# Cycle Detection
for i in range(1, 10000):
    x = i
    nums = [x]
    while True:
        x = gen(x)  # function that makes the next term
        if x in nums:
            x_idx = nums.index(x)
            cycle = nums[x_idx:]
            # do whatever with it
            # cycles[stringify_cycle(cycle)] += 1
            break
        nums.append(x)
        if x > stop:
            break


def factorial(num):
    """RECURSION"""
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


# read file
file_name = sys.argv[1]
with open(file_name) as f:
    pass


datContent = [i.strip().split() for i in open("./flash.dat").readlines()]
