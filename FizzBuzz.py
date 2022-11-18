from unittest import TestCase

"""
Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""
"""
FizzBuzz parte B
Após resolver o problema do FizzBuzz acrescente a seguintes regra: 
- Números contendo o algarismo 3 devem aparecer como 'Fizz'. 
- Números contendo o algarismo 5 devem aparecer como 'Buzz'. 
- Números contendo ambos os algarismos devem aparecer como 'FizzBuzz', 
se o 3 vier antes do 5 ou 'BuzzFizz' caso contrário. 
Obs.: Vale lembrar que as 3 regras do primeiro problema continuam valendo.
"""
# Seguindo a aula Raio X do TDD
# versão simplificada


def algarismo_fizzbuzz(pos):
    if '3' in str(pos) and '5' not in str(pos):
        result = 'Fizz'

    elif '3' not in str(pos) and '5' not in str(pos):
        result = str(pos)

    elif '5' in str(pos) and '3' not in str(pos):
        result = 'Buzz'

    elif str(pos).index('3') < str(pos).index('5'):
        result = 'FizzBuzz'

    elif str(pos).index('3') > str(pos).index('5'):
        result = 'BuzzFizz'

    return result


def fizzbuzz(pos):
    result = str(pos)

    if pos % 5 != 0 and pos % 3 != 0:
        result = str(pos)

    elif pos % 3 == 0 and pos % 5 == 0:
        result = 'FizzBuzz'

    elif pos % 5 == 0:
        result = 'Buzz'

    elif pos % 3 == 0:
        result = 'Fizz'

    return result


print(fizzbuzz(35))
print(algarismo_fizzbuzz(35))
# Tentando configurar wakatime no github
# Para mensurar atividades
