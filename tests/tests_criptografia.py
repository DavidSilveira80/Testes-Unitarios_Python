from unittest import TestCase

from criptografia import criptografa_minusculas_maiusculas, criptografa_char, inverte_texto, divide_string, \
    particiona_texto, tres_requisitos


class TestCriptografia(TestCase):
    def test_cripto_char_direita_A_D(self):
        self.assertEqual(criptografa_char('A', 'r', 3), 'D')

    def test_cripto_char_esquerda_A_arroba(self):
        self.assertEqual(criptografa_char('A', 'l', 1), '@')

    def test_cripto_minusculas_maiusculas_3_direita(self):
        self.assertEqual(criptografa_minusculas_maiusculas('Texto #3', 'r', 3), 'Wh{wr #3')
        self.assertEqual(criptografa_minusculas_maiusculas('David', 'r', 3), 'Gdylg')

    def test_cripto_segunda_passada_inverte_texto(self):
        self.assertEqual(inverte_texto('Wh{wr #3'), '3# rw{hW')
        self.assertEqual(inverte_texto('Gdylg'), 'glydG')
        self.assertEqual(inverte_texto('David'), 'divaD')

    def test_metade_da_string(self):
        self.assertEqual(divide_string('glydG'), 2)
        self.assertEqual(divide_string('3# rw{hW'), 4)

    def test_primeira_metdade_string(self):
        self.assertEqual(particiona_texto('glydG', 1), 'gl')
        self.assertEqual(particiona_texto('David', 1), 'Da')
        self.assertEqual(particiona_texto('Wh{wr #3', 1), 'Wh{w')

    def test_segunda_metade_string(self):
        self.assertEqual(particiona_texto('David', 2), 'vid')
        self.assertEqual(particiona_texto('glydG', 2), 'ydG')

    def test_programa_principal(self):
        self.assertEqual(tres_requisitos('Texto #3'), '3# rvzgV')
        self.assertEqual(tres_requisitos('abcABC1'), '1FECedc')
        self.assertEqual(tres_requisitos('vxpdylY .ph'), 'ks. \\n{frzx')
        self.assertEqual(tres_requisitos('vv.xwfxo.fd'), 'gi.r{hyz-xx')
