def main():
    '''
    This exercise consists in: 
    1) Receiving an integer as input
    2) If the number is multiple of 3, print the word "Fizz"
    3) Else, print the given number
    
    Exemplo:
    
    Enter an integer number: 5
    5
    Enter an integer number: 6
    Fizz
    
    '''
    num = int(input("Enter a integer number: "))
    

    if num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
main()
