import random
valid = []
for i in range(100) :
    number = random.randint(1,999)
    character = chr(number)
    print(character)
    answer = input("Is this valid character? (Y/N)")
    if answer == "Y":
        valid.append(character)
print(valid)
FILENAME = 'character.txt'
with open(FILENAME, 'a') as myfile :
    for item in  valid :
        myfile.write(item)