
'''
The objective of this exercise was to create a function that 
receives as parameter an integral n and returns 'Fizz' if it's
divisible by 3, 'Buzz' if it's divisible by 5, or 'FizzBuzz' if
it's divisible by 3 AND 5 at the same time, else it returns n. 

Also, i did a test function to print the results and see if they
are right.
'''

def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 != 0):
        return 'Fizz'
    if (n % 5 == 0) and (n % 3 != 0):
        return 'Buzz'
    if (n % 5 == 0) and (n % 3 == 0):
        return 'FizzBuzz'
    else:
        return n

def test_fizzbuzz(a,b):
    while a <= b:
        print("For %i ="%(a),fizzbuzz(a))
        a += 1

test_fizzbuzz(1,20)