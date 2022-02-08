'''
This exercise consists in:
1) Receiving an integer n as input
2) Calculating and then printing the factorial of n
'''

n = int(input("Enter the value of n: "))
fat = 1
count = 2

while count <= n:
    fat *= count
    count += 1

print("%i! = %i"%(n,fat))
