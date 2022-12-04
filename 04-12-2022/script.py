file = open("input.txt", "r")
lines = file.readlines()

# First part

count = 0

for line in lines:
    assignments = line.split(",")
    assignments = [assignment.strip() for assignment in assignments]

    # Check if the assignment colides with other elf assignments (full colision)
    aux=[]
    for assignment in assignments:
        # print(assignment)
        auxAsig = assignment.split("-")
        auxAsig = [int(x) for x in auxAsig]
        aux.append(auxAsig)

    if (aux[0][0] >= aux[1][0] and aux[0][1] <= aux[1][1]) or (aux[1][0] >= aux[0][0] and aux[1][1] <= aux[0][1]):
        count += 1
        
print("First part:", count)


# Second part

# Now we want overlapping colision (partial colision)

count = 0

for line in lines:
    assignments = line.split(",")
    assignments = [assignment.strip() for assignment in assignments]

    # Check if the assignment colides with other elf assignments (full colision)
    aux=[]
    for assignment in assignments:
        # print(assignment)
        auxAsig = assignment.split("-")
        auxAsig = [int(x) for x in auxAsig]
        aux.append(auxAsig)

   
    if (aux[0][0] in range(aux[1][0], aux[1][1]+1)) or (aux[1][0] in range(aux[0][0], aux[0][1]+1)) or (aux[0][1] in range(aux[1][0], aux[1][1]+1)) or (aux[1][1] in range(aux[0][0], aux[0][1]+1)):
        count += 1

print("Second part:", count)