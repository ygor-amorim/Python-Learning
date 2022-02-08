'''
This one was a bit tricky, the objective was to print if the
input integer has any equal digits adjacent to each other.

Example:
Enter an integer: 123
no
Enter an integer: 1223
yes
'''

def adjacents():

    num_str = input("Enter an integer: ")
    integer = int(num_str)
    count = len(num_str)
    non_adjacent = True
    original_value = integer
    integer_clone = integer 

    while count > 1:
        integer = (integer // (10 ** (count-1))) % 10
        integer_clone = (integer_clone // (10 ** (count-2))) % 10
        anterior = integer
        proximo = integer_clone
        integer = original_value
        integer_clone = original_value
        count -= 1
        if proximo == anterior:
            non_adjacent = False
        else:
            non_adjacent

    if non_adjacent:
        print("no") 
    else:
        print("yes") 


adjacents()

    


