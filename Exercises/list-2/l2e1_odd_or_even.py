def main():
    '''The objective of this exercise is:
    1) Receiving an integer number on input
    2) Printing if the number is ODD or EVEN
    
    Example:
    
    Hello! Welcome to the ODD or EVEN number detector!
    Please, enter an integer number.
    Number: 6
    EVEN
    
    Número: 7
    ODD'''

    print("Hello! Welcome to the ODD or EVEN number detector!")
    print("Please, enter an integer number.")
    
    
    num = int(input("Number: "))
    

    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

            
#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
main()
