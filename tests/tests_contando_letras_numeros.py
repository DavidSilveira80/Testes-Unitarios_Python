from unittest import TestCase
import contando_letras_numeros

numeros = contando_letras_numeros.numeros
converte_para_string = contando_letras_numeros.converte_para_string
tamanho_algarismo = contando_letras_numeros.tamanho_algarismo
um_nove_palavra = contando_letras_numeros.um_nove_palavra
dez_dezenove_palavra = contando_letras_numeros.dez_dezenove_palavra
vinte_noventa_palavra = contando_letras_numeros.vinte_noventa_palavra
cem_novecentos_palavra = contando_letras_numeros.cem_novecentos_palavra
mil_palavra = contando_letras_numeros.mil_palavra
gera_palavras = contando_letras_numeros.gera_palavras
concatena_palavras = contando_letras_numeros.concatena_palavras
conta_letras_palavras = contando_letras_numeros.conta_letras_palavras
contagem_total = contando_letras_numeros.contagem_total


class TestContagemLetras(TestCase):
    def test_range_numeros(self):
        assert len(numeros) == 1000

    def test_converte_para_String(self):
        self.assertEqual(converte_para_string(1), '1')
        self.assertEqual(converte_para_string(20), '20')
        self.assertEqual(converte_para_string(100), '100')
        self.assertEqual(converte_para_string(1000), '1000')

    def test_tamanho_algarismo_unidade(self):
        self.assertEqual(tamanho_algarismo(1), 1)
        self.assertEqual(tamanho_algarismo(23), 2)
        self.assertEqual(tamanho_algarismo(100), 3)
        self.assertEqual(tamanho_algarismo(1000), 4)

    def test_unidade_1_9_palavra(self):
        self.assertEqual(um_nove_palavra('1'), 'Um')
        self.assertEqual(um_nove_palavra('2'), 'Dois')
        self.assertEqual(um_nove_palavra('3'), 'Três')
        self.assertEqual(um_nove_palavra('9'), 'Nove')

    def test_dezena_10_19_palavra(self):
        self.assertEqual(dez_dezenove_palavra('10'), 'Dez')
        self.assertEqual(dez_dezenove_palavra('11'), 'Onze')
        self.assertEqual(dez_dezenove_palavra('19'), 'Dezenove')

    def test_dezenas_20_90_palavra(self):
        self.assertEqual(vinte_noventa_palavra('20'), 'Vinte')
        self.assertEqual(vinte_noventa_palavra('50'), 'Cinquenta')
        self.assertEqual(vinte_noventa_palavra('90'), 'Noventa')

    def test_centenas_100_900_palavra(self):
        self.assertEqual(cem_novecentos_palavra('100'), 'Cem')
        self.assertEqual(cem_novecentos_palavra('300'), 'Trezentos')
        self.assertEqual(cem_novecentos_palavra('900'), 'Novecentos')
        self.assertEqual(cem_novecentos_palavra('*'), 'Cento')

    def test_1000_palavra(self):
        self.assertEqual(mil_palavra('1000'), 'Mil')

    def test_gera_palavra(self):
        self.assertEqual(gera_palavras(1), ['Um'])
        self.assertEqual(gera_palavras(10), ['Dez'])
        self.assertEqual(gera_palavras(19), ['Dezenove'])
        self.assertEqual(gera_palavras(20), ['Vinte'])
        self.assertEqual(gera_palavras(23), ['Vinte', 'Três'])
        self.assertEqual(gera_palavras(100), ['Cem'])
        self.assertEqual(gera_palavras(918), ['Novecentos', 'Dezoito'])
        self.assertEqual(gera_palavras(119), ['Cento', 'Dezenove'])
        self.assertEqual(gera_palavras(550), ['Quinhentos', 'Cinquenta'])
        self.assertEqual(gera_palavras(1000), ['Mil'])
        self.assertEqual(gera_palavras(555), ['Quinhentos', 'Cinquenta', 'Cinco'])

    def test_concatena_palavras(self):
        self.assertEqual(concatena_palavras(['Um']), 'Um')
        self.assertEqual(concatena_palavras(['Dezenove']), 'Dezenove')
        self.assertEqual(concatena_palavras(['Trinta']), 'Trinta')
        self.assertEqual(concatena_palavras(['Trinta', 'Cinco']), 'TrintaeCinco')
        self.assertEqual(concatena_palavras(['Cem']), 'Cem')
        self.assertEqual(concatena_palavras(['Cento']), 'Cento')
        self.assertEqual(concatena_palavras(['Cento', 'Um']), 'CentoeUm')
        self.assertEqual(concatena_palavras(['Cento', 'Cinquenta']), 'CentoeCinquenta')
        self.assertEqual((concatena_palavras(['Cento', 'Cinquenta', 'Um'])), 'CentoeCinquentaeUm')

    def test_conta_letras_palavras(self):
        self.assertEqual(conta_letras_palavras('Um'), 2)
        self.assertEqual(conta_letras_palavras('Dois'), 4)
        self.assertEqual(conta_letras_palavras('Dez'), 3)
        self.assertEqual(conta_letras_palavras('Dezenove'), 8)
        self.assertEqual(conta_letras_palavras('VinteeUm'), 8)
        self.assertEqual(conta_letras_palavras('CentoeQuarentaeUm'), 17)

    def test_contagem_total_letras(self):
        self.assertEqual(contagem_total(range(1, 4)), 'Total: 10')  # Range abrange os números 1, 2, 3
        self.assertEqual(contagem_total(range(1, 5)), 'Total: 16')  # Range abrange os números 1, 2, 3, 4
