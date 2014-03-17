import solution
import unittest

class CalculateCoinsTest(unittest.TestCase):

	def test_calculate_couns_0_53(self):
		self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}, solution.calculate_coins(0.53))

	def test_calculate_couns_8_94(self):
		self.assertEqual({1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}, solution.calculate_coins(8.94))

if ( __name__ == '__main__'):
	unittest.main()