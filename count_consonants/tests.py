import solution
import unittest

class CountConsonantsTest(unittest.TestCase):

	def test_count_consonants_1st(self):
		self.assertEqual(4, solution.count_consonants("Python"))

	def test_count_consonants_2nd(self):
		self.assertEqual(11, solution.count_consonants("Theistareykjarbunga"))

	def test_count_consonants_3rd(self):
		self.assertEqual(7, solution.count_consonants("grrrrgh!"))

	def test_count_consonants_4th(self):
		self.assertEqual(44, solution.count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

	def test_count_consonants_5th(self):
		self.assertEqual(6, solution.count_consonants("A nice day to code!"))

if ( __name__ == '__main__'):
	unittest.main()