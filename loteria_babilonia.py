# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input('Entre com um número entre 1 e 15: '))

        except ValueError as err:
            print('Valor inválido!')
            continue

        if 1 <= numero_usuario <=15:
               return numero_usuario
        print('Valor inválido! Por favor, entre com um número entre 1 e 15. ')


def check_numbers(num_sorteio, num_usuario):
    if num_usuario == num_sorteio:
        print('Paranbéns! Você descobriu o número sorteado.')
        True

    elif num_usuario > num_sorteio:
        print('Número mais alto que o sorteado, tente um número mais baixo. ')
        False

    else:
        print('Número mais baixo que o sorteado, tente um número mais alto. ')
        False

numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()

    if check_numbers(num_sorteio=numero_sorteio, num_usuario=numero_usuario):
        break

else:
    print('Suas tentativas acabaram!')