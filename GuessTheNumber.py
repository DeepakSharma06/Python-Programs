# import random module for random number.  
import random 
## create a function for run this guessing game. 
guess= random.randint(1, a)
def number(a):
#let use of while loop for run this game.
   i=1
   while i<=10:
        
        print("You have only 10 turn")
        number= int(input("Enter number between 1 to 10: "))
        if number==guess:
            print("you win")
            break
        elif number!=guess :
            print("You lose, try again")
               #print("computer number: ",guess)
        i+=1
        #else: print("Game Over, You Lose this game ")
           
a=number(10)
