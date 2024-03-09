import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.sub(5, 3)
        self.assertEqual(result, 2)

    def test_addition_with_negative_numbers(self):
        calculator = Calculator()
        result = calculator.add(-2, 3)
        self.assertEqual(result, 1)

    def test_subtraction_with_negative_numbers(self):
        calculator = Calculator()
        result = calculator.sub(5, -3)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()

