# EP - Design de software
# Aluno: Stephan Christian Bottcher
# Data: 17/10/2020

#importando a funcao random para a distribuicao das cartas

import random

# inserindo baralho completo de 52 cartas
cartas = [1,2,3,4,5,6,7,8,9,10,0,0,0]
cartas = cartas*4

# as duas cartas distribuidas ao jogador(a e b)
random(cartas) = a
random(cartas) = b

# as duas cartas distribuidas ao banco(c e d)
random(cartas) = c
random(cartas) = d

# as cartas adicionais possivelmente distribuidas ao jogador e banco, respectivamente(e e f)
random(cartas) = e
random(cartas) = f


# Estabelecendo regras para a contagem das cartas e a definicao do vencedor:


#  caso as somas 8 e 9 tenham sido atingidas pelo jogador ou pelo banco
if a+b == 8 or a+b == 9 or c+d == 8 or c+d == 9:
    while a+b>c+d:
        vencedor=jogador
    while c+d>a+b:
        vencedor=banco
    while a+b==c+d:
        vencedor=empate  

# caso a somatoria das cartas do jogador tenha sido menor ou igual a 5 ou, igual a 6 ou 7, respectivamente

if a+b <= 5:
    a+b+e = Soma_do_jogador

if a+b ==6 or a+b ==7:
    a+b = Soma_do_jogador

# caso a somatoria das cartas do banco tenha sido menor ou igual a 5 ou, igual a 6 ou 7, respectivamente

if c+d <= 5:
    c+d+f = Soma_do_banco

if c+d == 6 or c+d == 7:
    c+d = Soma_do_banco

# estabelecendo regras de contagem para considerar somente as unidades caso a somatoria das cartas exceda 9

# no caso das cartas do jogador
if a+b > 9:
    a+b-10 = Soma_do_jogador
if a+b+e > 9:
    a+b-10 = Soma_do_jogador

# no caso das cartas do banco
if c+d > 9:
    c+d-10 = Soma_do_banco
if c+d+f > 9:
    c+d-10 = Soma_do_banco

# definindo quem foi vencedor
if Soma_do_banco>Soma_do_jogador:
    vencedor=banco
if Soma_do_jogador>Soma_do_banco:
    vencedor=jogador
if Soma_do_banco==Soma_do_jogador:
    vencedor=empate



ficha0 = 300


print ('Jogo de Bacara')

objeto_da_aposta = input('Em quem deseja apostar (banco, jogador ou empate)? ')
if objeto_da_aposta = banco:
    while vencedor=banco:
        print(Voce ganhou)
    else print(Voce perdeu)
if objeto_da_aposta = jogador:
    while vencedor=jogador:
        print(Voce ganhou)
    else print(Voce perdeu)
if objeto_da_aposta = empate:
    while vencedor = empate:
        print(Voce ganhou)
    else print(Voce perdeu)






    

    


    