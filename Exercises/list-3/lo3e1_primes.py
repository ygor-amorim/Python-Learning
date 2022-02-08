'''
The objective of this exercise was to receive an integer on input
and then print if its a prime number or not
'''

n = int(input("Enter an integer: "))

prime = True
count = 2

while count <= (n-1):
    a = n % count
    count += 1
    if a != 0:
        prime
    else:
        prime = False

if prime:
    print("prime number")
else:
    print("nonprime number")



