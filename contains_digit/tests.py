import solution
import unittest

class ContainsDigitTest(unittest.TestCase):

	def test_contains_digit_1st(self):
		self.assertEqual("False", solution.contains_digit(123, 4) )

	def test_contains_digit_2nd(self):
		self.assertEqual("True", solution.contains_digit(42, 2) )

	def test_contains_digit_3rd(self):
		self.assertEqual("True", solution.contains_digit(1000, 0) )

	def test_contains_digit_4th(self):
		self.assertEqual("False", solution.contains_digit(12346789, 5) )

if __name__ == '__main__':
	unittest.main()
