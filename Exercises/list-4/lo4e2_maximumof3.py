'''
In this exercise the objective was to create a function that receives
3 integers as parameters (a, b and c) and returns the biggest of the 3.

'''
def maximo(a,b,c):
    if (a > b) and (a > c):
        return a
    if (b > a) and (b > c):
        return b
    else:
        return c

print(maximo(30,14,10))
print(maximo(23,27,5))
print(maximo(5,14,66))
print(maximo(0,-1,1))