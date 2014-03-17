import solution
import unittest

class IsAnBnTest(unittest.TestCase):

	def test_is_an_bn(self):
		self.assertEqual("True", solution.is_an_bn(""))

	def test_is_an_bn_rado(self):
		self.assertEqual("False", solution.is_an_bn("rado"))

	def test_is_an_bn_aaabb(self):
		self.assertEqual("False", solution.is_an_bn("aaabb"))

	def test_is_an_bn_aaabbb(self):
		self.assertEqual("True", solution.is_an_bn("aaabbb"))

	def test_is_an_bn_aabbaabb(self):
		self.assertEqual("False", solution.is_an_bn("aabbaabb"))

	def test_is_an_bn_bbbaaa(self):
		self.assertEqual("False", solution.is_an_bn("bbbaaa"))

	def test_is_an_bn_aaaaabbbbb(self):
		self.assertEqual("True", solution.is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
	unittest.main()