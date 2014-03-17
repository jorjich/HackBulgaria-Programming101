import cat
import os
import unittest

class CatTest(unittest.TestCase):

    def test_with_empty_file(self):
        content = os.system("cat file.txt")
        self.assertEqual(content, cat.main())

if __name__ == '__main__':
    unittest.main()
