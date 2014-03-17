import solution
import unittest

class PrimeFactorizationTest(unittest.TestCase):

	def test_prime_factorization_10(self):
		self.assertEqual([(2, 1), (5, 1)], solution.prime_factorization(10))

	def test_prime_factorization_14(self):
		self.assertEqual([(2, 1), (7, 1)], solution.prime_factorization(14))

	def test_prime_factorization_356(self):
		self.assertEqual([(2, 2), (89, 1)], solution.prime_factorization(356))

	def test_prime_factorization_89(self):
		self.assertEqual([(89, 1)], solution.prime_factorization(89))

	def test_prime_factorization_1000(self):
		self.assertEqual([(2, 3), (5, 3)], solution.prime_factorization(1000))

if ( __name__ == '__main__' ):
	unittest.main()