def main():
    '''
    Objetivo deste exercício:
    1) Utilizar conhecimentos básicos de input e if para:
       a) Criar um programa que recebe a entrada de 3 variaveis,
       sendo essas os coeficientes a, b e c, de uma equacão do segundo grau
       b) Utilizar esses coeficientes para obter a(s) raiz(es) de qualquer
       equação do segundo grau
       c) Delimitar os 3 casos de resultados de saída, sendo esses
       com delta < 0, delta == 0 ou delta > 0
       
    '''
    print("Olá, este programa calcula as raízes de uma equação de segundo grau (ax²+bx+c = 0), dadas as raízes a, b e c")

    a = int(input("Insira o valor de a: "))
    b = int(input("Insira o valor de b: "))
    c = int(input("Insira o valor de c: "))

    delta = (b ** 2) - (4  * a * c)
    bhaskara1 = ( - b + (delta**(1/2))) / (2 * a)
    bhaskara2 = ( - b - (delta**(1/2))) / (2 * a)

    if delta < 0:
        print("Essa equação não possui raiz real")

    if delta == 0:
        print("Como Δ = 0, a única raiz da equação é: ", bhaskara1)

    if delta > 0:
        print("Como Δ > 0, as duas raizes reais da equação são: x1=", bhaskara1, "e x2=", bhaskara2)


#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

