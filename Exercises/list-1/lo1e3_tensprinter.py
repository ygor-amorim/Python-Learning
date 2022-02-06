# This exercise consists of printing the digit on the tens of any given number 

integer = int(input("Please, enter a integer: "))

tens = (integer // 10) % 10

print("The tens digit is", tens)