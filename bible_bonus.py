import re
import string

with open('puzzle.txt', 'r') as file:
    lines = [line[:-1] for line in file.readlines()]
    for i, line in enumerate(lines):
        if not re.search("i.*v.*a", line, re.IGNORECASE):
            continue
        for j, char in enumerate(line):
            if char.lower() != 'i':
                continue
            line_index = i
            char_index = j
            ELS = ''

            def increment_char():
                global line_index, char_index
                char_index += 1
                while char_index >= len(lines[line_index]):
                    line_index += 1
                    while len(lines[line_index]) == 0:
                        line_index += 1
                    char_index = 0

            def skip_letters(n):
                global line_index, char_index
                skipped = 0
                while True:
                    char = lines[line_index][char_index]
                    if char in string.ascii_letters:
                        if skipped == n:
                            break
                        skipped += 1
                    increment_char()

            ELS += lines[line_index][char_index]
            increment_char()
            skip_letters(11)
            if lines[line_index][char_index].lower() != 'v':
                continue
            ELS += lines[line_index][char_index]
            increment_char()
            skip_letters(11)
            if lines[line_index][char_index].lower() != 'a':
                continue
            ELS += lines[line_index][char_index]
            for _ in range(18):
                increment_char()
                skip_letters(11)
                ELS += lines[line_index][char_index]
            print(i, j, ELS)
