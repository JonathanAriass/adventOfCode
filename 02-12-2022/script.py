file = open("input.txt", "r")
lines = file.readlines()

res = 0

"""
# Part 1 (enemy)
    A: rock
    B: paper
    C: scissors

# Part 2 (player)
    X: rock (1 point)
    Y: paper (2 points)
    Z: scissors (3 points)

    If lose -> 0 points
    If draw -> 3 points
    If win -> +6 points
"""

lose = 0
draw = 3
win = 6

for line in lines:
    aux = line.split(" ")
    aux[1] = aux[1].strip()
    if aux[0] == 'A':
        if aux[1] == 'X':
            res += 1
            res += draw
        elif aux[1] == 'Y':
            res += 2
            res += win
        elif aux[1] == 'Z':
            res += 3
            res += lose
    elif aux[0] == 'B':
        if aux[1] == 'X':
            res += 1
            res += lose
        elif aux[1] == 'Y':
            res += 2
            res += draw
        elif aux[1] == 'Z':
            res += 3
            res += win
    elif aux[0] == 'C':
        if aux[1] == 'X':
            res += 1
            res += win
        elif aux[1] == 'Y':
            res += 2
            res += lose
        elif aux[1] == 'Z':
            res += 3
            res += draw

print(res)


# Second part

res = 0
for line in lines: 
    aux = line.split(" ")
    aux[1] = aux[1].strip()
    # Now second column is the result of the game
    if aux[1] == 'X':
        res += 0
        # need to check which piece we need
        if aux[0] == 'A':
            res += 3
        elif aux[0] == 'B':
            res += 1
        elif aux[0] == 'C':
            res += 2
    if aux[1] == 'Y':
        res += 3
        # need to check which piece we need
        if aux[0] == 'A':
            res += 1
        elif aux[0] == 'B':
            res += 2
        elif aux[0] == 'C':
            res += 3
    if aux[1] == 'Z':
        res += 6
        # need to check which piece we need
        if aux[0] == 'A':
            res += 2
        elif aux[0] == 'B':
            res += 3
        elif aux[0] == 'C':
            res += 1

print(res)
