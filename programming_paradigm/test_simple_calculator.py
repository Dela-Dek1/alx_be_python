import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Positive test cases
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10.5, 2.3), 12.8)

        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(10, 0), 10)
    
    def test_subtraction(self):
        # Positive test cases
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(12.5, 3.1), 9.4)

        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(10, 0), 10)

    def test_multiplication(self):
        # Positive test cases
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(10.5, 2), 21.0)

        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_division(self):
        # Positive test cases
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 5), 2.0)

        # Test with zero as divisor
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)  # Correct way to test for ZeroDivisionError

        # Test division by non-zero float
        self.assertEqual(self.calc.divide(10.0, 2.0), 5.0)

