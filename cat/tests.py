import cat
import unittest
import sys

class CatTest(unittest.TestCase):

    def setUp(self):
        sys.argv.append('file.txt')
        self.filename = sys.argv[1]
        self.my_file = open(self.filename, 'r')
        self.content = self.my_file.read()

    def test_cat(self):
        self.assertEqual(self.content, cat.main())

    def tearDown(self):
        self.my_file.close()


if __name__ == '__main__':
    unittest.main()
