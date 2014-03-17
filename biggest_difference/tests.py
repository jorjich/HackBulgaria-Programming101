import solution
import unittest

class BiggestDifferenceTest(unittest.TestCase):

	def test_biggest_difference_1st(self):
		self.assertEqual(-1, solution.biggest_difference([1,2]))

	def test_biggest_difference_2nd(self):
		self.assertEqual(-4, solution.biggest_difference([1,2,3,4,5]))

	def test_biggest_difference_3rd(self):
		self.assertEqual(-9, solution.biggest_difference([-10,-9,-1]))

	def test_biggest_difference_4th(self):
		self.assertEqual(-99, solution.biggest_difference(range(100)))

if ( __name__ == '__main__'):
	unittest.main()