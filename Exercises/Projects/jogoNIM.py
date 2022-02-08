'''
NIM Game
The objective of this exercise was described in the README.md file
in the same folder.'''

# Function that contains the guidelines which the computer plays.
def computador_escolhe_jogada(n,m):
    count = 1
    while count < m:
        peças_restantes = n - count

        if peças_restantes % (m+1) == 0:
            jogada = count
            n = peças_restantes
            return jogada
        else:
            count = count + 1

    if count == m:
        return m
# Function that receives the plays by the user.
def usuario_escolhe_jogada(n,m):
    jogada = int(input("Quantas peças você vai tirar? "))
    print()
    if 1 <= jogada <= m:
        return jogada
    else:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        return usuario_escolhe_jogada(m,n)
        
# Little auxiliary function that prints the results of each play by the user.
def jogada_usuario_print(jogada_usuario, n):

    if jogada_usuario == 1:
        print("Você retira uma peça")
    else:
        print("Você retira", jogada_usuario, "peças do tabuleiro")
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro")
    else:
        print("Agora restam", n,"peças no tabuleiro")

# Little auxiliary function that prints the results of each play by the computer.
def jogada_pc_print(jogada_pc, n):

    if jogada_pc == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", jogada_pc, "peças do tabuleiro")
    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro")
    else:
        print("Agora restam", n,"peças no tabuleiro")

# Function that contains the match, with previous functions being called.
# Note that there are only one possible result to any match: Computer wins.
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
   
    if n % (m+1) == 0:
        print("Voce começa!")
        print()
        jogada_usuario = usuario_escolhe_jogada(n,m)
        n = n - jogada_usuario
        jogada_usuario_print(jogada_usuario,n)
        
        while n > 0:
            jogada_pc = computador_escolhe_jogada(n,m)
            n = n - jogada_pc
            jogada_pc_print(jogada_pc,n)
            if n <= 0:
                break
            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n - jogada_usuario
            jogada_usuario_print(jogada_usuario,n)
            if n <= 0:
                break
        print("Fim do jogo! O computador ganhou!")
        
    else:
        print("Computador começa!")
        print()
        jogada_pc = computador_escolhe_jogada(n,m)
        n = n - jogada_pc
        jogada_pc_print(jogada_pc, n)

        while n > 0:
            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n - jogada_usuario
            jogada_usuario_print(jogada_usuario,n)
            print()
            if n <= 0:
                break
            jogada_pc = computador_escolhe_jogada(n,m)
            n = n - jogada_pc
            jogada_pc_print(jogada_pc,n)
            print()
            if n <= 0:
                break
        print()
        print("Fim do jogo! O computador ganhou!")

# Function that acts as a main function and also implements a "championship",
# option, with 3 matches. Note that this one also has only one possible result.
def campeonato():
        
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print()
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        escolha = int(input(""))

        if escolha == 1:
            print("Voce escolheu partida isolada!")
            partida()
        
        if escolha == 2:
            print("Voce escolheu um campeonato!")

            for num in (1,2,3):
                print("**** Rodada",num,"****")
                print()
                partida()
            print()    
            print("Placar: Você 0 X 3 Computador")


campeonato()

