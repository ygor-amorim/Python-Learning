'''
The objective of this exercise was to design a function that 
returns the sum of all hypotenuses between 0 and n. 
'''
import math

def its_hypotenuse(n):
    i = 1
    j = 1

    while i < n:
        while j < n:
            if math.pow(n,2) == (math.pow(i,2) + math.pow(j,2)):
                return True
            else:
                j = j + 1
        i = i + 1
        j = 1

    return False


def sum_hypotenuses(n):
    count = 1
    soma = 0
    while count <= n:
        if its_hypotenuse(count):
            soma = soma + count
            count = count + 1
        else:
            count = count + 1
    return soma







                



    
