''' 
This exercise consists in receiving an integer n as input
and then printing the first n real odd numbers 
'''

def main(): 

    n = int(input("Digite o valor de n: "))
    cont = 0

    while  cont <  n:
             impar = 2 * cont + 1 
             print(impar)

             cont = cont  + 1

main()