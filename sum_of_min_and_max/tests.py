import solution
import unittest

class SumMinMaxTest(unittest.TestCase):
	def test_sum_min_max_1st(self):
		self.assertEqual(10, solution.sum_of_min_and_max([1,2,3,4,5,6,8,9]))

	def test_sum_min_max_2nd(self):
		self.assertEqual(90, solution.sum_of_min_and_max([-10,5,10,100]))

	def test_sum_min_max_3rd(self):
		self.assertEqual(2, solution.sum_of_min_and_max([1]))

if __name__ == '__main__':
    unittest.main()
