import math
import string
import sys

file_path = sys.argv[1]
position = int(sys.argv[2])
cycle = int(sys.argv[3])
length = int(sys.argv[4])

with open(file_path, 'r') as file:
    lines = [line[:-1] for line in file.readlines()]
    extract = ''
    ELS = ''
    cycle_dir = int(math.copysign(1, cycle))
    cycle_len = abs(cycle)
    acc = 0
    for i, line in enumerate(lines):
        line_len = len(
            "".join(filter(lambda char: char in string.ascii_letters, line)))
        if acc + line_len > position:
            break
        acc += line_len
    line_index = 0
    char_index = 0
    lbrace = '[' if cycle_dir == 1 else ']'
    rbrace = ']' if cycle_dir == 1 else '['

    def increment_char(direction):
        global extract, line_index, char_index
        char_index += direction
        while char_index < 0 if direction == -1 else char_index >= len(lines[line_index]):
            extract += '\n'
            line_index += direction
            while len(lines[line_index]) == 0:
                line_index += direction
            if direction == 1:
                char_index = 0
            else:
                char_index = len(lines[line_index]) - 1

    def skip_letters(n, direction):
        global extract, line_index, char_index
        skipped = 0
        while True:
            char = lines[line_index][char_index]
            if char in string.ascii_letters:
                if skipped == n:
                    break
                skipped += 1
            extract += char
            increment_char(direction)
    skip_letters(position - 1, 1)
    if cycle_dir == 1:
        extract = lines[line_index][:char_index]
    else:
        extract = lines[line_index][char_index+1:][::-1]
    extract += lbrace + lines[line_index][char_index] + rbrace
    ELS += lines[line_index][char_index]
    for _ in range(length - 1):
        increment_char(cycle_dir)
        skip_letters(cycle_len - 1, cycle_dir)
        extract += lbrace + lines[line_index][char_index] + rbrace
        ELS += lines[line_index][char_index]
    if cycle_dir == 1:
        extract += lines[line_index][char_index+1:]
    else:
        extract = lines[line_index][:char_index] + extract[::-1]
    print(extract)
    print()
    print(ELS)
