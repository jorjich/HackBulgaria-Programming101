import solution
import unittest

class WhatIsMySignTest(unittest.TestCase):

	def test_what_is_my_sign_1st(self):
		self.assertEqual("Leo", solution.what_is_my_sign(5, 8) )

	def test_what_is_my_sign_2nd(self):
		self.assertEqual("Aquarius", solution.what_is_my_sign(29, 1) )

	def test_what_is_my_sign_3rd(self):
		self.assertEqual("Cancer", solution.what_is_my_sign(30, 6) )

	def test_what_is_my_sign_4th(self):
		self.assertEqual("Gemini", solution.what_is_my_sign(31, 5) )

	def test_what_is_my_sign_5th(self):
		self.assertEqual("Aquarius", solution.what_is_my_sign(2, 2) )

	def test_what_is_my_sign_6th(self):
		self.assertEqual("Taurus", solution.what_is_my_sign(8, 5) )

	def test_what_is_my_sign_7th(self):
		self.assertEqual("Capricorn", solution.what_is_my_sign(9, 1) )

if ( __name__ == '__main__'):
	unittest.main()
