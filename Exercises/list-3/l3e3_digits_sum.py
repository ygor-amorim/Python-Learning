'''
This exercise consists in receiving an integer n and 
then printing the sum of the digits in this number

Example:
Enter an integer: 12
3
Enter an integer: 123
6
Enter an integer: 1
1
'''

n_str = input("Enter an integer: ")
n = int(n_str)
count = int(len(n_str))
total_sum = 0

while count > 0:
    digito = n // 10 ** (count - 1) % 10
    total_sum = total_sum + digito
    count -= 1

print(total_sum)

