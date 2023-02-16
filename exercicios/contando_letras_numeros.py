from unittest import TestCase
"""
Contando as letras dos números

Se os números de 1 a 5 fossem escritos em palavras:
um, dois, três, quatro, cinco, então t
teríamos utilizado 2 + 4 + 4 + 6 + 5 = 21 letras no total.

Se todos os números de 1 até 1000 fossem escritos em palavras, incluindo a letra 'e' (ex: Cento e Cinquenta),
quantas letras nós teríamos utilizado?
"""
numeros = range(1, 1001)


def converte_para_string(algarismo: int) -> str:
    return str(algarismo)


def tamanho_algarismo(algarismo: int) -> int:
    algarismo = converte_para_string(algarismo)
    return len(algarismo)


def um_nove_palavra(unidade: str) -> str:
    algarismo = converte_para_string(unidade)
    unnove = {'1': 'Um', '2': 'Dois', '3': 'Três', '4': 'Quatro',
              '5': 'Cinco', '6': 'Seis', '7': 'Sete', '8': 'Oito',  '9': 'Nove'}

    if algarismo in unnove:
        return unnove[algarismo]


def dez_dezenove_palavra(dezDezenove: str) -> str:
    algarismo = converte_para_string(dezDezenove)
    dezdezenove = {'10': 'Dez', '11': 'Onze', '12': 'Doze', '13': 'Treze',
                   '14': 'Quatorze', '15': 'Quinze', '16': 'Dezesseis',
                   '17': 'Dezessete', '18': 'Dezoito', '19': 'Dezenove'}

    if algarismo in dezdezenove:
        return dezdezenove[algarismo]


def vinte_noventa_palavra(vinteNoventa: str) -> str:
    algarismo = converte_para_string(vinteNoventa)
    vintenoventa = {'2': 'Vinte', '3': 'Trinta', '4': 'Quarenta', '5': 'Cinquenta',
                    '6': 'Sessenta', '7': 'Setenta', '8': 'Oitenta', '9': 'Noventa'}

    if algarismo[0] in vintenoventa:
        return vintenoventa[algarismo[0]]


def cem_novecentos_palavra(centena: str) -> str:
    algarismo = converte_para_string(centena)
    cemnovecentos = {'1': 'Cem', '2': 'Duzentos', '3': 'Trezentos', '4': 'Quatrocentos',
                     '5': 'Quinhentos', '6': 'Seiscentos', '7': 'Setecentos',
                     '8': 'Oitocentos', '9': 'Novecentos', '*': 'Cento'}

    if algarismo[0] in cemnovecentos:
        return cemnovecentos[algarismo[0]]


def mil_palavra(milhar: str) -> str:
    return 'Mil'


def gera_palavras(num: int) -> list:
    numero = converte_para_string(num)

    if tamanho_algarismo(numero) == 1:
        unidade = [um_nove_palavra(numero)]
        resp = unidade

    elif tamanho_algarismo(numero) == 2:
        if 9 <= num <= 19:
            resp = [dez_dezenove_palavra(numero)]
        else:
            previa = [vinte_noventa_palavra(numero[0]), um_nove_palavra(numero[1])]
            if None in previa:
                previa.remove(None)
                resp = previa
            else:
                resp = previa
    elif tamanho_algarismo(numero) == 3:
        if numero[1:] == '00':
            resp = [cem_novecentos_palavra(numero[0])]

        elif 101 <= int(numero) <= 199:
            if 1 <= int(numero[1:]) <= 9:
                resp = [cem_novecentos_palavra("*"), um_nove_palavra(numero[2])]

            elif 10 <= int(numero[1:]) <= 19:
                resp = [cem_novecentos_palavra('*'), dez_dezenove_palavra(numero[1:])]

            elif numero[2] == '0':
                resp = [cem_novecentos_palavra('*'), vinte_noventa_palavra(numero[1])]

            else:
                resp = [cem_novecentos_palavra('*'), vinte_noventa_palavra(numero[1]),
                        um_nove_palavra(numero[2])]

        else:
            if 1 <= int(numero[1:]) <= 9:
                resp = [cem_novecentos_palavra(numero[0]), um_nove_palavra(numero[2])]

            elif 10 <= int(numero[1:]) <= 19:
                resp = [cem_novecentos_palavra(numero[0]), dez_dezenove_palavra(numero[1:])]

            elif numero[2] == '0':
                resp = [cem_novecentos_palavra(numero[0]), vinte_noventa_palavra(numero[1])]

            else:
                resp = [cem_novecentos_palavra(numero[0]), vinte_noventa_palavra(numero[1]),
                        um_nove_palavra(numero[2])]
    elif tamanho_algarismo(numero) == 4:
        resp = [mil_palavra(numero)]
    return resp


def concatena_palavras(palavra: list) -> str:
    resp = 'e'.join(palavra)
    return resp


def conta_letras_palavras(palavras: str) -> int:
    return len(palavras)


def contagem_total(numeros: range) -> str:
    total_letras_palavras = 0
    for num in numeros:
        total_letras_palavras += conta_letras_palavras(concatena_palavras(gera_palavras(num)))
        #print(num, concatena_palavras(gera_palavras(num)),
              #conta_letras_palavras(concatena_palavras(gera_palavras(num))), total_letras_palavras)

    return f'Total: {total_letras_palavras}'


print(contagem_total(numeros))
