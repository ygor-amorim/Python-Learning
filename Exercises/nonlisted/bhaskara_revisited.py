'''
Bhaskara exercise refactored, I tinkered some things while I was
studying a little bit more about functions and then again when the
subject was lists. 

'''
# Function that returns the 2 possible values for baskhara
def bhaskara(a,b,c):
    delta = (b ** 2) - (4  * a * c)
    bhask1 = ( - b + (delta**(1/2))) / (2 * a)
    bhask2 = ( - b - (delta**(1/2))) / (2 * a)
    if delta >= 0:
        return [bhask1, bhask2]

def main():
    a = int(input("Insira o valor de a: "))
    b = int(input("Insira o valor de b: "))
    c = int(input("Insira o valor de c: "))
    delta = (b ** 2) - (4  * a * c)

    if delta < 0:
        print("Essa equação não possui raiz real")

    if delta == 0:
        print("Como Δ = 0, a única raiz da equação é: ", bhaskara(a,b,c))

    if delta > 0:
        if bhaskara(a,b,c)[0] < bhaskara(a,b,c)[1]:
            print("Como Δ > 0, as duas raizes reais da equação são: x1=", bhaskara(a,b,c)[0], "e x2=", bhaskara(a,b,c)[1])
        else:
            print("Como Δ > 0, as duas raizes reais da equação são: x1=", bhaskara(a,b,c)[1], "e x2=", bhaskara(a,b,c)[0])
    
        
    

