import solution
import unittest

class IsIncreasingTest(unittest.TestCase):

	def test_is_increasing_1st(self):
		self.assertEqual(True, solution.is_increasing([1,2,3,4,5]))

	def test_is_increasing_2nd(self):
		self.assertEqual(True, solution.is_increasing([1]))

	def test_is_increasing_3rd(self):
		self.assertEqual(False, solution.is_increasing([5,6,-10]))

	def test_is_increasing_4th(self):
		self.assertEqual(False, solution.is_increasing([1,1,1,1]))

if (__name__ == '__main__'):
	unittest.main()