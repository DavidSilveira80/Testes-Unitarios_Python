import pytest

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
    result = 'fizzbuzz'
  
  elif pos % 5 == 0:
    result =  'buzz'
  
  elif pos % 3 == 0:
    result = 'fizz'
  
  return result
  
if __name__=='__main__':
  assert fizzbuzz(1) == '1'
  assert fizzbuzz(2) == '2'
  assert fizzbuzz(4) == '4'

  assert fizzbuzz(3) == 'fizz'
  assert fizzbuzz(6) == 'fizz'
  assert fizzbuzz(9) == 'fizz'
  
  assert fizzbuzz(5) == 'buzz'
  assert fizzbuzz(10) == 'buzz'
  assert fizzbuzz(20) == 'buzz'

assert fizzbuzz(15) == 'fizzbuzz'
assert fizzbuzz(30) == 'fizzbuzz'
assert fizzbuzz(45) == 'fizzbuzz'