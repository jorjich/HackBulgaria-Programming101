import unittest

import solution

import sys

class SumNumbersTest(unittest.TestCase):
    def test_equal_55(self):
        sys.argv.append('chisla.txt')
        self.assertEqual(55, solution.main())

    def test_not_equal_120(self):
        self.assertNotEqual(120, solution.main())

    def test_not_equal_0(self):
        self.assertNotEqual(0, solution.main())

    def test_too_many_args(self):
        sys.argv.append('chisla.txt')
        sys.argv.append('chisla.txt')
        self.assertEqual("Too many arguments", solution.main())

    def test_not_enough_args(self):
        sys.argv = [sys.argv[0]]
        self.assertEqual("No given arguments!", solution.main())


if __name__ == '__main__':
   unittest.main()

