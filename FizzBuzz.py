from unittest import TestCase

"""
Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""
# Seguindo a aula Raio X do TDD
# versão simplificada


def fizzbuzz(pos):
    result = str(pos)
  
    if pos % 3 == 0 and pos % 5 == 0:
        result = 'FizzBuzz'
  
    elif pos % 5 == 0:
        result = 'Buzz'
  
    elif pos % 3 == 0:
        result = 'Fizz'
  
    return result
  

class TestFizzBuzz(TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz(1), '1')

    def test_2(self):
        self.assertEqual(fizzbuzz(2), '2')

    def test_4(self):
        self.assertEqual(fizzbuzz(4), '4')

    def test_multiplos_3(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(9), 'Fizz')

    def test_multiplos_5(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz(20), 'Buzz')

    def test_multiplos_3_5(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(fizzbuzz(45), 'FizzBuzz')
