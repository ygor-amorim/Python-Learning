'''
This exercise consists in creating a function that receives a 
list with integers/floats as parameter and returns the sum of
all elements in the list
'''

def soma_elementos(lista):
    soma = 0     
    for num in range(len(lista)):
           soma += lista[num]
    return soma