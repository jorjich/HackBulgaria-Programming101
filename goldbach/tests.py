import solution
import unittest

class GoldachTest(unittest.TestCase):

	def test_goldbach_4(self):
		self.assertEqual([(2,2)], solution.goldbach(4))


	def test_goldbach_6(self):
		self.assertEqual([(3,3)], solution.goldbach(6))

	
	def test_goldbach_8(self):
		self.assertEqual([(3,5)], solution.goldbach(8))

	
	def test_goldbach_10(self):
		self.assertEqual([(3,7), (5,5)], solution.goldbach(10))

	
	def test_goldbach_100(self):
		self.assertEqual([(3,97), (11,89), (17,83), (29,71), (41,59), (47,53)], solution.goldbach(100))

if __name__ == '__main__':
			unittest.main()		

	