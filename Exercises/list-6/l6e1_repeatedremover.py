'''
In this exercise the objective was to design a function that 
receives a list as a parameter and, if the list has any repeated
elements, returns a new list containing only unique elements.
'''
def repeated_remover(lista):
    count = 0
    new_list = []
    lista.sort()
    while count < len(lista):
        if (lista[count]) not in (new_list):
            new_list.append(lista[count])
        count = count + 1
    return new_list
