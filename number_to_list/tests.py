import solution
import unittest

class NumberToListTest(unittest.TestCase):

	def test_number_to_list_123(self):
		self.assertEqual([1,2,3], solution.number_to_list(123))

	def test_number_to_list_99999(self):
		self.assertEqual([9,9,9,9,9], solution.number_to_list(99999))
		
	def test_number_to_list_123023(self):
		self.assertEqual([1,2,3,0,2,3], solution.number_to_list(123023))
		
if ( __name__ == '__main__' ):
	unittest.main()