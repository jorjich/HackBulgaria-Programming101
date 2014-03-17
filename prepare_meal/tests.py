import solution
import unittest

class PrepareMealTest(unittest.TestCase):

	def test_prepare_meal_5(self):
		self.assertEqual('"eggs"', solution.prepare_meal(5))

	def test_prepare_meal_3(self):
		self.assertEqual('"spam"', solution.prepare_meal(3))

	def test_prepare_meal_27(self):
		self.assertEqual('"spam spam spam"', solution.prepare_meal(27))

	def test_prepare_meal_15(self):
		self.assertEqual('"spam and eggs"', solution.prepare_meal(15))

	def test_prepare_meal_45(self):
		self.assertEqual('"spam spam and eggs"', solution.prepare_meal(45))

	def test_prepare_meal_7(self):
		self.assertEqual('""', solution.prepare_meal(7))

if ( __name__ == '__main__'):
	unittest.main()