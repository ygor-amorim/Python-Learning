# This exercise consists in printing the credit card bill from
# a fictitious person based on user

def main():
    nome = input("Digite o nome do cliente: ")
    dia = input("Digite o dia de vencimento: ")
    mes = input("Digite o mês de vencimento: ")
    valor = input("Digite o valor da fatura: ")

    print("Olá,",nome)
    print("A sua fatura com vencimento em", dia, "de", mes, "no valor de R$" ,valor, "está fechada.")

#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . .

main()
