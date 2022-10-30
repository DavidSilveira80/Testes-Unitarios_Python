from unittest import TestCase
"""
Contando as letras dos números

Se os números de 1 a 5 fossem escritos em palavras:
um, dois, três, quatro, cinco, então t
teríamos utilizado 2 + 4 + 4 + 6 + 5 = 21 letras no total.

Se todos os números de 1 até 1000 fossem escritos em palavras,
quantas letras nós teríamos utilizado?
"""


numeros = range(1, 1001)


def converte_para_string(algarismo):
    return str(algarismo)


def tamanho_algarismo(algarismo):
    algarismo = converte_para_string(algarismo)
    return len(algarismo)


def um_nove_palavra(unidade):
    algarismo = converte_para_string(unidade)
    unnove = {'1': 'Um', '2': 'Dois', '3': 'Três', '4': 'Quatro', '5': 'Cinco', '6': 'Seis', '7': 'Sete', '8': 'Oito',
              '9': 'Nove'}
    if algarismo in unnove:
        return unnove[algarismo]


def dez_dezenove_palavra(dezDezenove):
    algarismo = converte_para_string(dezDezenove)
    dezdezenove = {'10': 'Dez', '11': 'Onze', '12': 'Doze', '13': 'Treze', '14': 'Quatorze', '15': 'Quinze',
                   '16': 'Dezesseis', '17': 'Dezessete', '18': 'Dezoito', '19': 'Dezenove'}
    if algarismo in dezdezenove:
        return dezdezenove[algarismo]


def vinte_noventa_palavra(vinteNoventa):
    algarismo = converte_para_string(vinteNoventa)
    vintenoventa = {'2': 'Vinte', '3': 'Trinta', '4': 'Quarenta', '5': 'Cinquenta', '6': 'Sessenta', '7': 'Setenta',
                    '8': 'Oitenta', '9': 'Noventa'}
    if algarismo[0] in vintenoventa:
        return vintenoventa[algarismo[0]]


def cem_novecentos_palavra(centena):
    algarismo = converte_para_string(centena)
    cemnovecentos = {'1': 'Cem', '2': 'Duzentos', '3': 'Trezentos', '4': 'Quatrocentos', '5': 'Quinhentos',
                     '6': 'Seiscentos', '7': 'Setecentos', '8': 'Oitocentos', '9': 'Novecentos', '*': 'Cento'}
    if algarismo[0] in cemnovecentos:
        return cemnovecentos[algarismo[0]]


def mil_palavra(milhar):
    return 'Mil'


for num in numeros:
    numero = converte_para_string(num)

    if tamanho_algarismo(numero) == 1:
        print(numero, um_nove_palavra(numero))

    elif tamanho_algarismo(numero) == 2:

        if 9 <= num <= 19:
            print(numero, dez_dezenove_palavra(numero))
        else:
            print(numero, vinte_noventa_palavra(numero[0]),
                  um_nove_palavra(numero[1]))

    elif tamanho_algarismo(numero) == 3:
        if numero[1:] == '00':
            print(numero, cem_novecentos_palavra(numero[0]))
        elif 101 <= int(numero) <= 199:
            if 1 <= int(numero[1:]) <= 9:
                print(numero, cem_novecentos_palavra("*"), um_nove_palavra(numero[2]))
            elif 10 <= int(numero[1:]) <= 19:
                print(numero, cem_novecentos_palavra('*'), dez_dezenove_palavra(numero[1:]))
            elif numero[2] == '0':
                print(numero, cem_novecentos_palavra('*'), vinte_noventa_palavra(numero[1]))
            else:
                print(numero, cem_novecentos_palavra('*'), vinte_noventa_palavra(numero[1]),
                      um_nove_palavra(numero[2]))
        else:
            if 1 <= int(numero[1:]) <= 9:
                print(numero, cem_novecentos_palavra(numero[0]), um_nove_palavra(numero[2]))
            elif 10 <= int(numero[1:]) <= 19:
                print(numero, cem_novecentos_palavra(numero[0]), dez_dezenove_palavra(numero[1:]))
            elif numero[2] == '0':
                print(numero, cem_novecentos_palavra(numero[0]), vinte_noventa_palavra(numero[1]))
            else:
                print(numero, cem_novecentos_palavra(numero[0]), vinte_noventa_palavra(numero[1]),
                      um_nove_palavra(numero[2]))
    elif tamanho_algarismo(numero) == 4:
        print(numero, mil_palavra(numero))


class TestContagemLetras(TestCase):
    def test_range_numeros(self):
        assert len(numeros) == 1000

    def test_converte_para_String(self):
        self.assertEqual(converte_para_string(1), '1')
        self.assertEqual(converte_para_string(20), '20')
        self.assertEqual(converte_para_string(100), '100')
        self.assertEqual(converte_para_string(1000), '1000')

    def test_tamanho_algarismo_unidade(self):
        self.assertEqual(tamanho_algarismo('1'), 1)
        self.assertEqual(tamanho_algarismo('23'), 2)
        self.assertEqual(tamanho_algarismo('100'), 3)
        self.assertEqual(tamanho_algarismo('1000'), 4)

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
