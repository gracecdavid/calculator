import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    # This is to test the addition
    def test_addition(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    # This is to test subtraction 
    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.sub(5, 3)
        self.assertEqual(result, 2)
    def test_positive_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)  # Test with positive integers
        self.assertEqual(calculator.add(5, 7), 12)  # Test with positive integers

if __name__ == '__main__':
    unittest.main()
        