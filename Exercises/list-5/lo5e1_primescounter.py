'''
The objective of this exercise was to write a function that 
counts how many prime numbers are between 0 and n. [0,n] 
It also uses the previously created auxiliary function to
determine if a number is prime or not.
'''

def itsPrimo(k):
    count = 2

    while count <= (k-1):
        a = k % count
        count += 1
        while a == 0:
            return False
    
    return True


def n_primes(n):
    count = 2
    primes = 0
    while n > 1:
        if itsPrimo(count):
            count = count + 1
            primes = primes + 1
        else:
            count = count + 1
        n = n - 1
    return primes
