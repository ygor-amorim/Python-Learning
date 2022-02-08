'''
This exercise consisted in creating a function that returns
the biggest n prime number, while using an auxiliary function
that determines if a number is prime or not.
'''

def itsPrime(k):
    count = 2

    while count <= (k-1):
        a = k % count
        count += 1
        while a == 0:
            return False
    
    return True

def maior_primo(n):
    while not itsPrime(n):
        n -= 1
    if itsPrime(n):
        return n
