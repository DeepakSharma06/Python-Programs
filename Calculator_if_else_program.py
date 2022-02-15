#Create a calculator with if else program. 
fn=int(input("Enter Frist Number: "))
sn=int(input("Enter Second Number: "))
#Oprators
print("Choose Opration oprator:-")
print("Sum(add)= +,")
print("Substract= -,")
print("Divide= /,")
print("Multiply= *,")
print("Selected oprator put in down")
op=str(input("Enter opration operator: "))
if op=='+':
    print("The sum of Frist and Second Number is: ", float(fn+sn))
elif op=='-':
     print("The Substraction of Frist and Second Number is: ", float(fn-sn))
elif op=='/':
     print("The Division of Frist and Second Number is: ", float(fn/sn))
elif op=='*':
    print("The Multiplication of Frist and Second Number is: ",float(fn*sn))
else: print("Error, Please Enter valid oprator. ")
