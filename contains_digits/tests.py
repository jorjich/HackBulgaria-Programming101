import solution
import unittest

class ContainsDigitsTest(unittest.TestCase):

	def test_contains_digits_1st(self):
		self.assertEqual("True", solution.contains_digits(402123, [0,3,4]))

	def test_contains_digits_2nd(self):
		self.assertEqual("True", solution.contains_digits(402123, [0,3,4]))

	def test_contains_digits_3rd(self):
		self.assertEqual("True", solution.contains_digits(402123, [0,3,4]))

	def test_contains_digits_4th(self):
		self.assertEqual("True", solution.contains_digits(402123, [0,3,4]))

if __name__ == '__main__':
	unittest.main()