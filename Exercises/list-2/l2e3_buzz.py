def main():
    '''
   This exercise consists in: 
    1) Receiving an integer as input
    2) If the number is multiple of 5, print the word "Buzz"
    3) Else, print the given number
    
    Exemplo:
    
    Enter an integer number: 5
    Buzz
    Enter an integer number: 6
    6
    
    '''
    num = int(input("Enter an integer number: "))

    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
main()
