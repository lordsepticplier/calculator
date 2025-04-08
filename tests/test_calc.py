import pytest
from calc . calc import add , subtract , multiply , calculate

def test_add () :
assert add (5 , 2) == 7
assert add ( -1 , 2) == 1
assert add ( -1 , -5) == -6

def test_subtract () :
assert subtract (5 , 2) == 3
assert subtract (1 ,4) == -3
assert subtract ( -2 , -2) == 0

def test_multiply () :
assert multiply (2 , 2) == 4
assert multiply ( -1 , 3) == -3
assert multiply ( -1 , -1) == 1

def test_calculate () :
assert calculate ( ’ add ’ , 5 , 2) == 7
assert calculate ( ’ subtract ’ , 6 , 3) == 3
assert calculate ( ’ multiply ’ , 4 , 2) == 8
