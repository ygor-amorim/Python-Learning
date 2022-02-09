'''
The objective of this exercise was to create a function that
returns the binomial coefficient of a subset of k elements from
a fixed set of n elements.

For that, I created a small function that returns the factorial of
n. Then, I applied the formula for the binomial coefficient.

I took the liberty of creating a function that prints the n line
from the Pascal's Triangle, after that, I did a simple function that
prints the Pascal Triangle from 0 to n.
'''

def factorial(n):
    fat = 1
    cont = 2

    while cont <= n:
        fat *= cont
        cont += 1  

    return fat

def coef_binomial(n,k):
    return factorial(n) / (factorial(k) * (factorial(n-k)))

def linha_pascal(n):
    k = 0
    while k <= n:
        print (coef_binomial(n,k), end=" ")
        k += 1

def triangulo_pascal(n):
    for num in range(n+1):
        linha_pascal(num)
        print()

triangulo_pascal(9)

