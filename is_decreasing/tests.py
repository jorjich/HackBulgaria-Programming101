import solution
import unittest

class IsDecreasingTest(unittest.TestCase):

	def test_is_decreasing_1st(self):
		self.assertEqual(True, solution.is_decreasing([5,4,3,2,1]))

	def test_is_decreasing_2nd(self):
		self.assertEqual(False, solution.is_decreasing([1,2,3]))

	def test_is_decreasing_3rd(self):
		self.assertEqual(True, solution.is_decreasing([100,50,20]))

	def test_is_decreasing_4th(self):
		self.assertEqual(False, solution.is_decreasing([1,1,1,1]))

if (__name__ == '__main__'):
	unittest.main()