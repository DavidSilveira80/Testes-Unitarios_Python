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


class TestFizzBuzz(TestCase):
    def test_retorna_numero(self):
        self.assertEqual(fizzbuzz(1), '1')
        self.assertEqual(fizzbuzz(2), '2')
        self.assertEqual(fizzbuzz(53), '53')

    def test_multiplos_3(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(9), 'Fizz')

    def test_multiplos_5(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz(20), 'Buzz')
        self.assertEqual(fizzbuzz(35), 'Buzz')

    def test_multiplos_3_5(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(fizzbuzz(45), 'FizzBuzz')

    def test_com_algarismo_3(self):
        self.assertEqual(algarismo_fizzbuzz(43), 'Fizz')
        self.assertEqual(algarismo_fizzbuzz(3), 'Fizz')
        self.assertEqual(algarismo_fizzbuzz(13), 'Fizz')
        self.assertEqual(algarismo_fizzbuzz(123), 'Fizz')

    def test_com_algarismo_5(self):
        self.assertEqual(algarismo_fizzbuzz(5), 'Buzz')
        self.assertEqual(algarismo_fizzbuzz(145), 'Buzz')
        self.assertEqual(algarismo_fizzbuzz(25), 'Buzz')

    def test_algarismo_3_5(self):
        self.assertEqual(algarismo_fizzbuzz(345), 'FizzBuzz')
        self.assertEqual(algarismo_fizzbuzz(543), 'BuzzFizz')
        self.assertEqual(algarismo_fizzbuzz(353), 'FizzBuzz')
        self.assertEqual(algarismo_fizzbuzz(535), 'BuzzFizz')

    def test_sem_algarismo_3_5(self):
        self.assertEqual(algarismo_fizzbuzz(142), '142')
        self.assertEqual(algarismo_fizzbuzz(1), '1')
