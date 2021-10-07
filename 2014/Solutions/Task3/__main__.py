import sys

file_name = sys.argv[1]

with open(file_name) as file:
    lines = file.readlines()
    values = {}

    def parse_var(tokens):
        name = tokens.pop(0)
        return values[name]

    def parse_string_literal(tokens):
        s = tokens.pop(0)[1:]
        while True:
            token = tokens.pop(0)
            if token[-1] != "\"":
                s += token
                continue
            s += token[:len(tokens)-1]
            break
        return s

    def parse_var_or_string_literal(tokens):
        token = tokens[0]
        if token[0] == "\"":
            return parse_string_literal(token)
        else:
            return parse_var(token)

    def parse_arith_expre():
        pass
    in_comment = False
    in_cond = False
    in_loop = 0
    line_number = 0
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        tokens = line.split(' ')
        command = tokens.pop(0)
        if in_comment:
            if command != 'TLDR':
                continue
            in_comment = False
            continue
        if in_loop == 2:
            if command != 'NO':
                continue
            in_loop = 3
            continue
        if in_loop == 3:
            in_loop = 0
            continue

        if command in ['HAI', 'KTHXBYE', 'BTW']:
            continue
        if command == 'OBTW':
            in_comment = True
            continue
        if command == 'VISIBLE':
            print(parse_var_or_string_literal(tokens))
            continue
        if command == 'GIMMEH':
            token = tokens.pop(0)
            value = input()
            values[token] = float(value)
            continue
        if command.islower():
            if tokens.pop(0) != 'R':
                raise ValueError('expected R')
            value = parse_arith(tokens)
            values[command] = value
            continue
        if command == 'I':
            if tokens.pop(0) != 'HAS':
                raise ValueError('expected HAS')
            if tokens.pop(0) != 'A':
                raise ValueError('expected A')
            name = tokens.pop(0)
            if tokens.pop(0) != 'ITZ':
                raise ValueError('expected ITZ')
            values[name] = parse_arith_expre(tokens)
        if command == 'IZ':
            if parse_bool(tokens):
                in_loop = 1
                continue
            else:
                in_loop = 2
