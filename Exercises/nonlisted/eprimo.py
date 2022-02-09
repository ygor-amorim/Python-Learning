'''
Exercise that contains a prime number detector. It also contains
a related function that counts submitted prime numbers.
'''

def éPrimo(k):
    count = 2

    while count <= (k-1):
        a = k % count
        count += 1
        if a == 0:
            return False
    
    return True

##################################
#prime number counter#
def sequencia():
    
    num = int(input("Digite o primeiro numero: "))
    cont = 0
    while num != 0:
        if éPrimo(num):
            cont += 1
        num = int(input("Insira o próximo número: "))             
    print(cont)
    
##################################

n = int(input("Digite um numero para saber se é primo: "))
while n != 0:
    if éPrimo(n):
        print("É primo")
        print()
    else:
        print("Não é primo")
        print()
    n = int(input("Digite um numero para saber se é primo: "))
