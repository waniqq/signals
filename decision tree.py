age = int(input("Enter your ages : "))
if age<25:
    print("high")
else:
    type_car = input("type of car : Fast Car, Family Car (fast/fam))")
    if type_car == "fam" :
        print("low")
    else:
            accident = input("Had an accident?(Y/N)")
    if accident == ("Y") :
            print("high")
    else:
            print("medium")