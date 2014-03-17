import solution
import unittest

class SortFractionsTest(unittest.TestCase):

	def test_sort_fractions_1st(self):
		self.assertEqual([(1,2), (2, 3)], solution.sort_fractions([(2,3),(1,2)]))

	def test_sort_fractions_2nd(self):
		self.assertEqual([(1,3), (1,2), (2,3)], solution.sort_fractions([(2,3),(1,2),(1,3)]))

	def test_sort_fractions_3rd(self):
		self.assertEqual([(22,78), (15, 32),(5,6),(7,8),(9,6),(22,7)], solution.sort_fractions([(5,6),(22,78),(22,7),(7,8),(9,6),(15,32)]))
		
if __name__ == '__main__':
	unittest.main()