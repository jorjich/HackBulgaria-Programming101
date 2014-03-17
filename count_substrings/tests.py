import solution
import unittest

class CountSubstringsTest(unittest.TestCase):

	def test_count_substrings_1st(self):
		self.assertEqual(2, solution.count_substrings("This is a test string", "is"))

	def test_count_substrings_2nd(self):
		self.assertEqual(2, solution.count_substrings("babababa", "baba"))

	def test_count_substrings_3rd(self):
		self.assertEqual(4, solution.count_substrings("Python is an awesome language to program in!", "o"))

	def test_count_substrings_4th(self):
		self.assertEqual(0, solution.count_substrings("We have nothing in common!", "really?"))

	def test_count_substrings_5th(self):
		self.assertEqual(2, solution.count_substrings("This is this and that is this", "this"))

if ( __name__ == '__main__' ):
	unittest.main()
