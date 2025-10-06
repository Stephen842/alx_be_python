import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        '''Set up the simple calculator instance before each test.'''
        self.calc = SimpleCalculator()

    def test_addition(self):
        '''Test the add method.'''
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        '''Test the subtract method.'''
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_multiplication(self):
        '''Test the multiply method.'''
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-10, -5), 50)

    def test_division(self):
        '''Test the divide method.'''
        self.assertEqual(self.calc.divide(50, 10), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(7, -1), -7)

        ### Test division by zero
        self.assertIsNone(self.calc.divide(20, 0))

if __name__ == "__main__":
    unittest.main()