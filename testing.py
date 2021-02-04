import calc_app
import unittest

class Test_Add(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(calc_app.add_numbers(1,1),2)

    def test_add2(self):
        self.assertEqual(calc_app.add_numbers(-1,-1),-2)

    def test_add3(self):
        self.assertEqual(calc_app.add_numbers(-2,1),-1)

class Test_Subtract(unittest.TestCase):
    def test_subtract1(self):
        self.assertEqual(calc_app.subtract_numbers(10,10),0)

    def test_subtract2(self):
        self.assertLess(calc_app.subtract_numbers(0,10),0)

    def test_subtract3(self):
        self.assertGreater(calc_app.subtract_numbers(11,10),0)


class Test_Multiply(unittest.TestCase):
    def test_multiply1(self):
        self.assertEqual(calc_app.multiply_numbers(3,15),45)

    def test_multiply2(self):
        self.assertLess(calc_app.multiply_numbers(-1,10),0)

    def test_multiply3(self):
        self.assertEqual(calc_app.multiply_numbers(10,10),100)

class Test_Divide(unittest.TestCase):
    def test_divide1(self):
        self.assertLess(calc_app.divide_numbers(100,-1),0)

    def test_divide2(self):
        self.assertEqual(calc_app.divide_numbers(4,4),1)

    def test_divide3(self):
        self.assertEqual(calc_app.divide_numbers(13,0),0) #This is my error handling test case prints 'cannot divide by zero'


if __name__ == "__main__":
    unittest.main()

