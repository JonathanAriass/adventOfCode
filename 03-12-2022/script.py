file = open("input.txt", "r")
lines = file.readlines()

# First part

resLines = []

for line in lines:
    n = len(line)
    aux = ["", ""]
    if n > 0:
        aux[0] = line[:n//2]
        aux[1] = line[n//2:]
        aux[1] = aux[1].strip()
    resLines.append(aux)
    

# Check if left and right has some char in common
res = 0

for i in range(len(resLines)):
    chars = []
    for j in range(len(resLines[i][0])):
        letter = resLines[i][0][j]
        
        if letter in resLines[i][1] and letter not in chars:
            # print(letter)
            aux = ord(letter.lower()) - 96
            if (letter.isupper()):
                aux += 26
            res += aux
            chars.append(letter)

print ("First part:", res)


# Second part
res = 0

file = open("input2.txt", "r")
lines = file.readlines()

# Get groups of 3 lines
groups = []
aux = []
for i in range(len(lines)):
    aux.append(lines[i].strip())
    if (i+1) % 3 == 0:
        groups.append(aux)
        aux = []

# Check if groups has badge in common
for group in groups:
    chars = []
    for i in range(len(group[0])):
        
        letter = group[0][i]
        if letter in group[1] and letter in group[2] and letter not in chars:
            aux = ord(letter.lower()) - 96
            if (letter.isupper()):
                aux += 26
            res += aux
            chars.append(letter)

print("Second part:", res)
