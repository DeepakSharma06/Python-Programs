n= int(input("Enter number of rows: "))
boll= int(input("Enter number 1 or 0: "))
if boll==0 and boll==1:
    boll=bool(boll)
elif boll==True :
    for i in range (1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print("")
elif boll==False:
    for i in range (n, 0,-1):
        for j in range(1, i+1):
            print("*", end=" ")
        print("")
