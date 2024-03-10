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

if __name__ == '__main__':
    unittest.main()
        