import solution
import unittest

class IsIntPalindromeTest(unittest.TestCase):

	def test_is_int_palindrome_1(self):
		self.assertEqual("True", solution.is_int_palindrome(1))

	def test_is_int_palindrome_42(self):
		self.assertEqual("False", solution.is_int_palindrome(42))

	def test_is_int_palindrome_100001(self):
		self.assertEqual("True", solution.is_int_palindrome(100001))

	def test_is_int_palindrome_999(self):
		self.assertEqual("True", solution.is_int_palindrome(999))

	def test_is_int_palindrome_123(self):
		self.assertEqual("False", solution.is_int_palindrome(123))

if __name__ == '__main__':
    unittest.main()
