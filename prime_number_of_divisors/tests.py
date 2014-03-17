import solution
import unittest

class PrimeNumberOfDivisorsTest(unittest.TestCase):

	def test_prime_number_of_divisors_7(self):
		self.assertEqual("True", solution.prime_number_of_divisors(7))

	def test_prime_number_of_divisors_8(self):
		self.assertEqual("False", solution.prime_number_of_divisors(8))

	def test_prime_number_of_divisors_9(self):
		self.assertEqual("True", solution.prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()
