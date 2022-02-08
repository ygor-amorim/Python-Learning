'''
This exercise consists in receiving a series of numbers as input
and then printing the submitted numbers in the reverse order
'''

num = int(input("Enter a number: "))
inserted_numbers = []
while num != 0:
    inserted_numbers.append(num)
    num = int(input("Enter a number: "))

inserted_numbers.reverse()
for n in inserted_numbers:
    print(n)

