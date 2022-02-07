def main():
    '''
    This exercise consists in: 
    1) Receiving an integer as input
    2) If the number is multiple of 3 AND 5 at the same time, print the word "FizzBuzz"
    3) Else, print the given number
    
    Exemplo:
    
    Enter an integer number: 8
    8
    Enter an integer number: 15
    FizzBuzz
    
    '''
    num = int(input("Digite um número: "))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
main()
