'''
This exercise consists in creating a function that receives
a list as parameter and returns the biggest element
'''

def maior_elemento(lista):
    lista.sort()
    return lista[-1]
    
