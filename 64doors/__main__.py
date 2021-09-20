print(' '.join([str(i) for i in range(1, 65) if sum(
    1 for j in range(1, 65) if i % j == 0) % 2 == 1]))
