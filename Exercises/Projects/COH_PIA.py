'''
COH_PIA
The objective of this exercise was described in the README.md file
in the same folder.
'''
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def lista_frases(texto):
    '''A funcao recebe um texto e devolve uma lista das frases dentro do texto'''
    lista_frases = []
    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)
    return lista_frases

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def lista_palavras(texto):
    '''A funcao recebe um texto e devolve uma lista das palavras dentro do texto'''
    lista_palavras = []
    frases = lista_frases(texto)
    for frase in frases:
        lista_palavras += separa_palavras(frase)
    return lista_palavras

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def MediaPalavras(texto):
    '''Essa funcao recebe um texto e divide a soma dos
    tamanhos destas palavras pelo número total de palavras.
    '''
    total_palavras = len(lista_palavras(texto))

    soma_tamanhos = 0
    for palavra in lista_palavras(texto):
        soma_tamanhos += len(palavra)

    tamanho_medio = soma_tamanhos / total_palavras
    
    return tamanho_medio


def TypeToken(texto):
    '''Essa funcao recebe um texto e divide o numero
    de palavras diferentes pelo número total de palavras.
    '''
    total_palavras = len(lista_palavras(texto))
    typeToken = n_palavras_diferentes(lista_palavras(texto)) / total_palavras

    return typeToken


def HapaxLegomana(texto):
    '''Essa funcao recebe uma lista de palavras e divide o numero
    de palavras que aparecem uma única vez pelo número total de palavras
    '''
    total_palavras = len(lista_palavras(texto))
    hapaxLegomana = n_palavras_unicas(lista_palavras(texto)) / total_palavras

    return hapaxLegomana

def MediaSentencas(texto):
    '''Essa funcao recebe um texto e calcula a
    soma dos caracteres em todas as sentenças dividida pelo numero
    de sentenças
    '''
    
    lista_sentencas = separa_sentencas(texto)
    numero_sentencas = len(lista_sentencas)
    soma_caracteres = 0
    for palavra in lista_sentencas:
        soma_caracteres += len(palavra)
    
    mediaSentencas = soma_caracteres / numero_sentencas
    return mediaSentencas

def ComplexidadeSentenca(texto):
    '''Essa funcao recebe um texto e divide o numero total de frases pelo
    numero de sentencas.
    '''
    lista_sentencas = separa_sentencas(texto)
    numero_sentencas = len(lista_sentencas)
    frases_total = 0
    cont = 0
    while cont < numero_sentencas:
        frases_total += len(separa_frases(lista_sentencas[cont]))
        cont += 1

    complexidade = frases_total / numero_sentencas

    return complexidade

def tamanho_medio_frase(texto):
    '''Essa funcao recebe um texto e divide a soma do numero de caracteres
    pelo número de frases total.
    '''
    lista_sentencas = separa_sentencas(texto)
    frases_total = 0
    cont = 0
    caracteres = 0

    while cont < len(lista_sentencas):
        lista_frases = []
        for sentenca in lista_sentencas:
            lista_frases += separa_frases(sentenca)
        frases_total += len(separa_frases(lista_sentencas[cont]))
        cont += 1

    for frase in lista_frases:
        caracteres += len(frase)

    tam_medio_frase = caracteres / frases_total
    return tam_medio_frase


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    diferenca = abs((as_a[0] - as_b[0]) - (as_a[1] - as_b[1]) -  (as_a[2] - as_b[2]) - (as_a[3] - as_b[3]) - (as_a[4] - as_b[4]))

    grau_similaridade = diferenca / 6

    return grau_similaridade

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    return assinatura.__add__([
        MediaPalavras(texto),
        TypeToken(texto),
        HapaxLegomana(texto),
        MediaSentencas(texto),
        ComplexidadeSentenca(texto),
        tamanho_medio_frase(texto)
        ])


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas_texto = []

    for texto in textos:
        assinaturas_texto.append(calcula_assinatura(texto))

    menor_comparacao = 100000000000000000000
    cont = 0
    for assinatura in assinaturas_texto:
        comparacao_n = compara_assinatura(assinatura,ass_cp)
        if comparacao_n < menor_comparacao:
            menor_comparacao = comparacao_n
            cont += 1

    return cont

def imprime_assinatura():
    assinatura = calcula_assinatura(input("Insira o texto modelo que deseja saber a assinatura: "))
    print(assinatura)

def COH_PIA():
    imprime_assinatura()
    assinatura_modelo = le_assinatura()
    textos = le_textos()

    print("O autor do texto", avalia_textos(textos, assinatura_modelo), "está infectado com COH-PIAH")




COH_PIA()