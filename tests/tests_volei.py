from unittest import TestCase
from volei import coleta_tentativas_pontos


class TestesVolei(TestCase):

    def test_coleta_tentativas_saque_bloqueio_ataque(self):
        self.assertEqual(coleta_tentativas_pontos([10, 20, 12], 's'), 10)
        self.assertEqual(coleta_tentativas_pontos([10, 20, 12], 'b'), 20)
        self.assertEqual(coleta_tentativas_pontos([10, 20, 12], 'a'), 12)

    def test_coleta_pontos_saque_bloqueio_ataque(self):
        self.assertEqual(coleta_tentativas_pontos([1, 10, 9], 's'), 1)
        self.assertEqual(coleta_tentativas_pontos([1, 10, 9], 'b'), 10)
        self.assertEqual(coleta_tentativas_pontos([1, 10, 9], 'a'), 9)
