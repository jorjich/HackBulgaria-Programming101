import solution
import unittest
import sys


class ConcatFilesTest(unittest.TestCase):

    def test_concat_files(self):
        sys.argv.append('solution.py')
        sys.argv.append('chisla.txt')
        self.file = open('solution.py', 'r')
        self.content = self.file.read()
        self.file.close()
        self.file = open('chisla.txt', 'r')
        self.content = self.file.read()
        self.file.close()
        self.assertEqual(self.content, solution.main())

    def test_no_files(self):
        sys.argv = [sys.argv[0]]
        self.assertEqual("No given arguments!", solution.main())


if __name__ == '__main__':
   unittest.main()
