"""
Objetivo: Criar um script que gerá um valor aleatoriamente,
guarda este valor, e pergunta repetidamente para o usuário chutar o valor
gerado até que ele acerte.
"""
import math
import random
from time import sleep

pc = random.randint(1, 6)
print('-=-'*20)
print('Vou pensar em um número entre 1 e 6. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PENSANDO...')
sleep(2)

if jogador == pc:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('Ganhei! eu pensei no numero {} e não no número {}'.format(pc, jogador))
