import solution
import unittest

class SumOfDivisorsTest(unittest.TestCase):
	def test_sum_of_divisors_8(self):
		self.assertEqual(15, solution.sum_of_divisors(8))

	def test_sum_of_divisors_7(self):
		self.assertEqual(8, solution.sum_of_divisors(7))

	def test_sum_of_divisors_1(self):
		self.assertEqual(1, solution.sum_of_divisors(1))

	def test_sum_of_divisors_2340(self):
		self.assertEqual(2340, solution.sum_of_divisors(1000))	

if __name__ == '__main__':
    unittest.main()
