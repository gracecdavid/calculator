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

    def test_addition_with_zero(self):
        calculator = Calculator()
        result = calculator.add(0, 3)
        self.assertEqual(result, 3)

    def test_subtraction_with_zero(self):
        calculator = Calculator()
        result = calculator.sub(5, 0)
        self.assertEqual(result, 5)

    def test_addition_with_large_numbers(self):
        calculator = Calculator()
        result = calculator.add(1000000, 2000000)
        self.assertEqual(result, 3000000)

    def test_subtraction_with_large_numbers(self):
        calculator = Calculator()
        result = calculator.sub(2000000, 1000000)
        self.assertEqual(result, 1000000)

    # Additional test cases to improve coverage
    def test_addition_with_floats(self):
        calculator = Calculator()
        result = calculator.add(2.5, 3.5)
        self.assertEqual(result, 6)

    def test_subtraction_with_floats(self):
        calculator = Calculator()
        result = calculator.sub(5.5, 3.5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

