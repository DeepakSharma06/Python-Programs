#It is not a question its my imagination program. 

i=0
print("Do you want learn python? ")
a=input("SAY YES(y) OR NO(n) : ")
if a=="y":
    print("JUST DO IT")
elif a=="n":
    while i<=5:
        print("Do you want learn python? ")
        b=input("SAY YES(y) OR NO(n) : ")
        if b=="n":
            continue
            i+=1
        else:print("Okay, JUST DO IT")
        break
