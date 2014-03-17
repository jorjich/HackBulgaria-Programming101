import solution
import unittest

class CountWordsTest(unittest.TestCase):

	def test_count_words_1st(self):
		self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, solution.count_words(["apple", "banana", "apple", "pie"]))

	def test_count_words_2nd(self):
		self.assertEqual({'ruby': 1, 'python': 3}, solution.count_words(["python", "python", "python", "ruby"]))

if ( __name__ == '__main__' ):
	unittest.main()