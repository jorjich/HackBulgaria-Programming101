import solution
import unittest

class IsNumberBalancedTest(unittest.TestCase):

	def test_is_number_balanced_9(self):
		self.assertEqual(True, solution.is_number_balanced(9))
	
	def test_is_number_balanced_11(self):
		self.assertEqual(True, solution.is_number_balanced(11))

	def test_is_number_balanced_13(self):
		self.assertEqual(False, solution.is_number_balanced(13))

	def test_is_number_balanced_121(self):
		self.assertEqual(True, solution.is_number_balanced(121))

	def test_is_number_balanced_4518(self):
		self.assertEqual(True, solution.is_number_balanced(4518))

	def test_is_number_balanced_28471(self):
		self.assertEqual(False, solution.is_number_balanced(28471))

	def test_is_number_balanced_1238033(self):
		self.assertEqual(True, solution.is_number_balanced(1238033))

if (__name__ == '__main__'):
	unittest.main()