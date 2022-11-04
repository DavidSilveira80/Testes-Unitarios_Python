from unittest import TestCase
from entre_letras import alfabeto, verifica_ordem_alfabetica, verifica_entre_letras, numero_letras_entre_letras


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
