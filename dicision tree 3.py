print("DIAMOND EXPERT SYSTEM")
q1=input("DNoes the stone float in water? (Y/N)")
if q1 == 'Y' :
    print("Fake")
else :
    q2 = input("Does it scratch glass?")
    if q2 == 'N' :
        print("Fake")
    else :
        q3 = input("Does the stone conduct Electricity?")
        if q3 == "Y":
            print("Fake")
        else :
            print("Could be real.")