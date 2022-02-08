'''
This exercise consists in:
1) Receiving an integer n as input
2) Calculating and printing the factorial of n
'''

n = int(input("Insira um numero inteiro n para calcular n!: " )) 
produto = 1
cont = n - 1
n_exp = n

if n > 0:

    while cont >= 1:
        fat = n * cont
        cont -= 1 
        produto = (produto * fat)

    produto_final = produto // (n_exp ** (n_exp - 2))

    print(produto_final)

else:
    print(int(1))

   
    


