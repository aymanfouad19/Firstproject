print("*********Calculator***************")
print("Enter your first number :")
try :
 print("Enter your first number")
 line= float(input())
except ValueError : 
    print("Please enter a valid number : ")
    line=float(input())
try :
    print("Enter second number :")
    second_line=float(input())
except ValueError :
    print("Please enter a valid number :")
    second_line=float(input())
addition= line+second_line
multiplication=line*second_line
subtraction = line-second_line
devision= line/second_line
print("**CHOOSE THE OPERATION**")
print("1""-addition(+)")
print("2""-subtraction(-)")
print("3""-multiplication(x)")
print("4""-devision(/)")
operation = input()
if operation == "1" : result = addition
elif operation == "2" : result = subtraction
elif operation == "3" : result = multiplication
elif operation == "4" : result = devision
else : operation=input("choose a number from 1 to 4 : ")
if operation == "1" : result = addition 
elif operation == "2" : result = subtraction
elif operation == "3" : result = multiplication
elif operation == "4" : result = devision
print("Your result is ")
print(result)
  



