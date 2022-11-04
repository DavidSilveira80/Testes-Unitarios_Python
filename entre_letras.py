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


class TestEntreLetras(TestCase):
    def test_quantidade_letras_alfabeto(self):
        self.assertEqual(len(alfabeto), 26)

    def test_letra_E_no_alfabeto(self):
        self.assertEqual('E' in alfabeto, True)

    def test_ordem_alfabetica(self):
        self.assertEqual(verifica_ordem_alfabetica('A', 'B'), True)
        self.assertEqual(verifica_ordem_alfabetica('C', 'B'), False)
        self.assertEqual(verifica_ordem_alfabetica('A', 'A'), True)
        self.assertEqual(verifica_ordem_alfabetica('Z', 'A'), False)

    def test_numero_letras_entre_A_C(self):
        self.assertEqual(verifica_entre_letras('A', 'C'), 1)

    def test_numero_letras_entre_A_B(self):
        self.assertEqual(verifica_entre_letras('A', 'B'), 0)

    def test_numero_letras_entre_D_H(self):
        self.assertEqual(verifica_entre_letras('D', 'H'), 3)

    def test_numero_letras_entre_B_L(self):
        self.assertEqual(verifica_entre_letras('B', 'L'), 9)

    def test_numero_letras_entre_A_A(self):
        self.assertEqual(verifica_entre_letras('A', 'A'), 0)

    def test_principal_H_D(self):
        self.assertEqual(numero_letras_entre_letras('H', 'D'), 'Não está na ordem alfabética')

    def test_principal_D_H(self):
        self.assertEqual(numero_letras_entre_letras('D', 'H'), 'Há 3 letras entre D e H')

    def test_principal_A_Z(self):
        self.assertEqual(numero_letras_entre_letras('A', 'Z'), 'Há 24 letras entre A e Z')

    def test_principal_A_B(self):
        self.assertEqual(numero_letras_entre_letras('A', 'B'), 'Há 0 letras entre A e B')

    def test_principal_A_A(self):
        self.assertEqual(numero_letras_entre_letras('A', 'A'), 'Há 0 letras entre A e A')
