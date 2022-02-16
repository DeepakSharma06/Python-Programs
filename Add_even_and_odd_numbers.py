#Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

add=0

n=int(input("Enter your starting number: ")) 

num= int(input("Enter your Ending number: ")) 

for i in range (n, num):

    if i%2==0:

        print(i)

        add+=i

print("The sum of Even number between",n,"and",num," is: ",add)

#second loop for odd numbers.

for i in range (n, num):

    if i%2!=0:

        print(i)

        add+=i

print("The sum of Odd number between",n,"and",num," is: ",add)
