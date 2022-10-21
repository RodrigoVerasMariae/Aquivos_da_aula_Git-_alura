from random import randint
from time import sleep

maquina = randint(0,2)

print('*'*10)
print('BORA JOGAR!')
print('*'*10)

time = sleep(1)

print('''
[1] Pedra
[2] Papel
[3] Tesoura
''')

time = sleep(1)

print('>'*17)
print('ESCOLHA SUA JOGADA')
print('>'*17)

jogador = int(input('Escolha sua jogada: '))

print('Pedra...')
tempo = sleep(1)
print('Papel...')
tempo = sleep(1)
print('Tesoura!')

tempo = sleep(1)

if maquina == 0:
    if jogador == 1:
        print('A maquina escolheu pedra e voce pedra também, empate!')
    if jogador == 2:
        print('A maquina escolheu pedra e voce papel, voce ganhou!')
    if jogador == 3:
        print('A maquina escolheuu pedra e voce tesoura, a maquina ganhou!')

elif maquina == 1:
    if jogador == 1:
        print('A maquina escolheu papel e voce pedra, a maquina ganhou!')
    if jogador == 2:
        print('A maquina escolheu papel e voce papel, deu empate!')
    if jogador == 3:
        print('A maquina escolheu papel e voce tesoura, voce ganhou!')

elif maquina == 2:
    if jogador == 1:
        print('A maquina escolheu tesoura e voce pedra, voce ganhou!')
    if jogador == 2:
        print('A maquina escolheu tesoura e voce papel, a maquina ganhou!')
    if jogador == 3:
        print('A maquina escolheu tesoura e voce tesoura, empate!')
