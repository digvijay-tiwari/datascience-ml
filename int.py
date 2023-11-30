listval = [2,5,8,5,2,0,7,9,3,2,4,6,9,7,1,2,3,6,5,4,7,8,9,0]
listUnique = []
for number in listval:
    if number %2 == 0:
        if number not in listUnique:
            listUnique.append(number)

listUnique.sort(reverse=True)
print(listUnique)
