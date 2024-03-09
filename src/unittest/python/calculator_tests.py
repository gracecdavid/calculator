# calculator_tests.py
import unittest
from calculator import Calculator
class CalculatorTest(unittest.TestCase):
    def test_addition(self):
        calculator = Calculator()
        result = calculator.add(2,3)
        self.assertEqual(result, 5)    
if __name__ == '__main__':
    unittest.main()
