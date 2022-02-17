#print pattern of star with the help of input function and for loop.
n=int(input("Enter Number of line: "))
l=n+1
for i in range (1, l):
    for j in range (1, l-i):
        print(" ",end="")
    for k in range (1,( 2*i-1)+1):
        print("*",end="")
    print("\n",end="")


print(" reverse star pattern .")

h=int(input("Enter Number of line: "))
g=h+1
for i in range (h,0,-1):
    for j in range (1, g-i):
        print(" ",end="")
    for k in range (1,( 2*i-1)+1):
        print("*",end="")
    print("\n",end="")
