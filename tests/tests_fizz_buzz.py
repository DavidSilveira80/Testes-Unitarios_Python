from unittest import TestCase
from FizzBuzz import algarismo_fizzbuzz, fizzbuzz


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
