import solution
import unittest

class ListToNumbersTest(unittest.TestCase):

	def test_list_to_numbers_123(self):
		self.assertEqual(123, solution.list_to_number([1,2,3]))

	def test_list_to_numbers_99999(self):
		self.assertEqual(99999, solution.list_to_number([9,9,9,9,9]))

	def test_list_to_numbers_123023(self):
		self.assertEqual(123023, solution.list_to_number([1,2,3,0,2,3]))

if ( __name__ == '__main__'):
	unittest.main()