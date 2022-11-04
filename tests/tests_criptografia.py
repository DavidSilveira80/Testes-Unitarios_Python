from unittest import TestCase

from criptografia import cripto_minusculas_maiusculas, cripto_char


class TestCriptografia(TestCase):
    def test_cripto_char_direita_A_D(self):
        self.assertEqual(cripto_char('A', 'r', 3), 'D')

    def test_cripto_char_esquerda_A_arroba(self):
        self.assertEqual(cripto_char('A', 'l', 1), '@')

    def test_cripto_primeira_passada_minusculas_maiusculas_3_direita(self):
        self.assertEqual(cripto_minusculas_maiusculas('Texto #3', 'r', 3), 'Wh{wr #3')
        self.assertEqual(cripto_minusculas_maiusculas('David', 'r', 3), 'Gdylg')
