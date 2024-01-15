import unittest
from mon_code import addition, soustraction, multiplication, division

class TestMonCode(unittest.TestCase):

        def test_addition(self):
            self.assertEqual(addition(2, 3), 5)
            self.assertEqual(addition(-1, 1), 0)
            self.assertEqual(addition(0, 0), 0)

        def test_soustraction(self):
            self.assertEqual(soustraction(5, 2), 3)
            self.assertEqual(soustraction(1, 1), 0)
            self.assertEqual(soustraction(0, 0), 0)
        
        def test_multiplication(self):
            self.assertEqual(multiplication(2, 3), 6)
            self.assertEqual(multiplication(-1, 1), -1)
            self.assertEqual(multiplication(0, 5), 0)
        
        def test_division(self):
            self.assertEqual(division(6, 2), 3)
            self.assertEqual(division(5, 2), 2.5)
            self.assertRaises(ValueError, division, 1, 0)


# test_main.py
import pytest
from main import MathOperations

# Instanciez la classe MathOperations
math_operations = MathOperations()

# Tests pour l'addition
def test_addition():
    assert math_operations.addition(2, 3) == 5
    assert math_operations.addition(-2, 3) == 1
    assert math_operations.addition(0, 0) == 0
    assert math_operations.addition(2.5, 3.5) == 6.0

# Tests pour la soustraction
def test_subtraction():
    assert math_operations.subtraction(5, 3) == 2
    assert math_operations.subtraction(-2, 3) == -5
    assert math_operations.subtraction(0, 0) == 0
    assert math_operations.subtraction(2.5, 1.5) == 1.0

# Tests pour la multiplication
def test_multiplication():
    assert math_operations.multiplication(2, 3) == 6
    assert math_operations.multiplication(-2, 3) == -6
    assert math_operations.multiplication(0, 0) == 0
    assert math_operations.multiplication(2.5, 2) == 5.0

# Tests pour la division
def test_division():
    assert math_operations.division(6, 3) == 2
    assert math_operations.division(-6, 3) == -2
    assert math_operations.division(0, 5) == 0
    assert math_operations.division(2.5, 2) == 1.25

# Tests pour la division par zéro
def test_division_by_zero():
    with pytest.raises(ValueError):
        math_operations.division(5, 0)

