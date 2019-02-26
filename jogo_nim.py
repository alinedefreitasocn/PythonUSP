# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:18:01 2019

@author: aline

Você deverá escrever um programa na linguagem Python, versão 3, que permita a
uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá
seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível
retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso
considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o
jogador a iniciar a partida com a frase "Você começa"
Caso contrário, o computador toma a inciativa de começar o jogo.
Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em
deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.
Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador
se utilize da estratégia vencedora.
"""


def main():
    print(u'Bem-vindo ao jogo do NIM! Escolha:')
    print(u'1 - para jogar uma partida isolada')
    print(u'2 - para jogar um campeonato')
    a = input('')
    if a == 2:
        print(' ')
        print(u'Voce escolheu um campeonato!')
        print(' ')
        campeonato()
    elif a == 1:
        print(' ')
        print(u'Voce escolheu jogar uma partida isolada!')
        print(' ')
        partida()
    else:
        print(u'Valor inválido! Tente novamente...')
        main()


def campeonato():
    for i in [1, 2, 3]:
        print(' ')
        print('**** Rodada ' + str(i) + ' ****')
        print(' ')
        partida()


def partida():
        n = input('Quantas peças? ')
        m = input('Limite de peças por jogada? ')
        if n % (m + 1) == 0:
            print(' ')
            print(u'Você começa!')
            print('')
            usuario_escolhe_jogada(m, n)
        else:
            print('')
            print(u'Computador começa!')
            print('')
            computador_escolhe_jogada(m, n)


def computador_escolhe_jogada(m, n):
    if n % m == 0:
        j = m - 1
    else:
        j = m
    return j



def usuario_escolhe_jogada(m, n):
    j = input('Quantas peças você vai tirar? ')
    while j > m:
        print('Oops! Jogada inválida! Tente de novo.')
        j = input('Quantas peças você vai tirar? ')
    return j

main()