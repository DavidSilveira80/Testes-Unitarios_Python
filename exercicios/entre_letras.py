from unittest import TestCase

"""
Entre letras
Contribuição de: Denis Costa

Faça um programa que receba duas letras, e diga quantas letras há entre elas.
As letras passadas devem estar em ordem alfabética.
Se não estiverem o programa deve avisar o usuário.
Exemplo: 'a', 'b' = 0 'a', 'c' = 1 'a', 'z' = 24 'w', 'e' = Não está na ordem alfabética
"""

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def verifica_ordem_alfabetica(letra1: str, letra2: str) -> bool:
    if letra1 <= letra2:
        ordem_alfabetica = True
    else:
        ordem_alfabetica = False
    return ordem_alfabetica


def verifica_entre_letras(inicio: str, fim: str) -> int:
    numero_de_letras = 0
    for letra in alfabeto[alfabeto.index(inicio):alfabeto.index(fim) + 1]:

        if inicio < letra < fim:
            numero_de_letras += 1

    return numero_de_letras


# Programa Principal
def numero_letras_entre_letras(letra_inicio: str, letra_final: str) -> str:
    if verifica_ordem_alfabetica(letra_inicio, letra_final):
        n_letras = verifica_entre_letras(letra_inicio, letra_final)
        resposta = f'Há {n_letras} letras entre {letra_inicio} e {letra_final}'
    else:
        resposta = 'Não está na ordem alfabética'
    return resposta
