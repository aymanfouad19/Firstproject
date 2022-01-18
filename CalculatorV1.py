print("*********Calculator***************")
print("first number")
line=int(input())
print("second number")
second_line=int(input())
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
if operation == "2" : result = subtraction
if operation == "3" : result = multiplication
if operation == "4" : result = devision
print("Your result is ")
print(result)
  



