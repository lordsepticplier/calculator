import pytest
from calc.calc import plus,subtract,calculate

def test_plus () :
  assert plus(5 , 2) == 7
  assert plus(-1 , 2) == 1
  assert plus(-1 , -5) == -6

def test_subtract () :
  assert subtract(5 , 2) == 3
  assert subtract(1 ,4) == -3
  assert subtract(-2 , -2) == 0

def test_calculate () :
  assert calculate ('plus' , 5 , 2) == 7
  assert calculate ('subtract' , 6 , 3) == 3
