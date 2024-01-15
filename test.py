import pytest
import unittest
from main import MathOperations


class TestMonCode(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(MathOperations.addition(2, 3), 5)
        self.assertEqual(MathOperations.addition(-1, 1), 0)
        self.assertEqual(MathOperations.addition(0, 0), 0)
        self.assertEqual(MathOperations.addition(2.5, 3.5), 6.0)

    def test_soustraction(self):
        self.assertEqual(MathOperations.soustraction(5, 2), 3)
        self.assertEqual(MathOperations.soustraction(-2, 3), -5)
        self.assertEqual(MathOperations.soustraction(0, 0), 0)
        self.assertEqual(MathOperations.soustraction(2.5, 1.5), 1.0)

    def test_multiplication(self):
        self.assertEqual(MathOperations.multiplication(2, 3), 6)
        self.assertEqual(MathOperations.multiplication(-2, 3), -6)
        self.assertEqual(MathOperations.multiplication(0, 0), 0)
        self.assertEqual(MathOperations.multiplication(2.5, 2), 5.0)

    def test_division(self):
        self.assertEqual(MathOperations.division(6, 2), 3)
        self.assertEqual(MathOperations.division(-6, 3), -2)
        self.assertEqual(MathOperations.division(5, 2), 2.5)

        with self.assertRaises(ValueError):
            MathOperations.division(1, 0)


    def test_division_negative(self):
        self.assertEqual(MathOperations.division(-6, 3), -2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            MathOperations.division(1, 0)

   
    def test_modulo_negative(self):
        self.assertEqual(MathOperations.modulo(-5, 2), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            MathOperations.modulo(2.5, 0)

@pytest.mark.parametrize("a, b, r", [(10, 8, 18), (-5, -10, -15), (2.5, 3.5, 6.0)])
def test_add_two_numbers(a, b, r):
        print(f"La somme de a={a}, b={b}, est égale à={r}")
        assert MathOperations.addition(a, b) == r


@pytest.mark.parametrize("base, exponent, result", [
        (2, 3, 8),
        (3, 2, 9),
        (5, 0, 1),
        (-2, 2, 4),
        (2, -2, 0.25),
        (0, 5, 0),
        (0, 0, 1),
        (2, -3, 0.125),  
    ])


def test_power(base, exponent, result):
        print(f"Testing power with base={base}, exponent={exponent}, expected result={result}")
        assert MathOperations.power(base, exponent) == result


@pytest.mark.parametrize("a, b, r", [(10, 3, 1), (-5, 2, 1), (2.5, 0.5, 0.0)])
def test_modulo(a, b, r):
    print(f"Testing modulo with a={a}, b={b}, expected result={r}")
    assert MathOperations.modulo(a, b) == r

