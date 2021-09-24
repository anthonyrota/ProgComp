# to run: edit input.txt, go to "shell" by clicking "shell" button on top of terminal, and type "cat input.txt | python main.py > output.txt", then check output.txt

import sys

num_lines = int(sys.stdin.readline())
for _ in range(num_lines):
    line = sys.stdin.readline().strip()
    a, b = line.split(' ')
    if len(a) != len(b):
        print(f'{a}, {b} have different lengths')
        continue

    def get_pattern(word):
        pattern = ['0'] * len(word)
        letter_to_last_idx = {}
        for i, letter in enumerate(word):
            if letter in letter_to_last_idx:
                prev_idx = letter_to_last_idx[letter]
                distance = i - prev_idx
                pattern[prev_idx] = f'+{distance}'
            letter_to_last_idx[letter] = i
        return ' '.join(pattern)
    pattern_a = get_pattern(a)
    pattern_b = get_pattern(b)
    if pattern_a == pattern_b:
        print(f'{a}, {b} are isomorphs with repetition pattern {pattern_a}')
    else:
        print(f'{a}, {b} are not isomorphs')
