 #print kite shape 
n=int(input("Enter number of lines: "))
l=n+1
for i in range (1, l):
    for k in range (1, l-i):
        print(" ",end="")
    for j in range (1, (2*i-1)+1):
        print("*",end="")
    print("\n",end="")
for i in range (n-1,0,-1):
    for k in range (1, l-i):
        print(" ",end="")
    for j in range (1, (2*i-1)+1):
        print("*",end="")
    print("\n",end="")
