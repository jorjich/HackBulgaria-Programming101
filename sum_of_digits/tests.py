import solution
import unittest

class SumOfDigitsTest(unittest.TestCase):
	def test_sum_of_digits_0(self):
		self.assertEqual(0, solution.sum_of_digits(0))

	def test_sum_of_digits_1(self):
		self.assertEqual(1, solution.sum_of_digits(1))

	def test_sum_of_digits_123(self):
		self.assertEqual(6, solution.sum_of_digits(123))

	def test_sum_of_digits_1234(self):
		self.assertEqual(10, solution.sum_of_digits(1234))

	def test_sum_of_digits_negative_564(self):
		self.assertEqual(15, solution.sum_of_digits(-564))

if __name__ == '__main__':
    unittest.main()
