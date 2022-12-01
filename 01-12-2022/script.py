file = open("input.txt", "r")
lines = file.readlines()

res = 0
aux = 0

count = 0

# First part of challenge
for line in lines:
    if (line == "\n"):
        if (aux > res):
            res = aux
        aux = 0
        print("Empty line")
        count += 1
    else:
        aux += int(line)

print (res)
print(count)


# Second part of challenge

top_3 = [0, 0, 0]
aux = 0

for line in lines:
    if (line == "\n"):
        if (aux > top_3[0]):
            top_3[0] = aux
            top_3.sort()
        aux = 0
    else:
        aux += int(line)

print(top_3)
print(sum(top_3))