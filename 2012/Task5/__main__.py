import sys

lines = sys.argv[1]

game = []
for i in lines:
    game.append([x for x in i.strip().split(" ")])

length = game[0]
game.remove(game[0])

rows = []
for row in game:
    rows.append(row)

columns = []
for number, group in enumerate(game):
    i = 0
    templist = []
    while i < len(game[number])-1:
        templist.append(game[i][number])
        i += 1
    columns.append(templist)

for i in columns:
    if int in i:


def rule1(rows, columns):
    for i in game:
        if "*" in i:
            continue
        else:
            return False
