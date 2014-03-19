import solution
import unittest
import sys
from subprocess import check_output


class ConcatFilesTest(unittest.TestCase):

    def test_wc_chars(self):
        sys.argv = [sys.argv[0]]
        sys.argv.append('chars')
        sys.argv.append('story.txt')
        wc_c = int(check_output(["wc", "-m", 'story.txt']).split()[0])
        self.assertEqual(wc_c, solution.main())

    def test_wc_words(self):
        sys.argv = [sys.argv[0]]
        sys.argv.append('words')
        sys.argv.append('story.txt')
        wc_w = int(check_output(["wc", "-w", 'story.txt']).split()[0])
        self.assertEqual(wc_w, solution.main())

    def test_wc_lines(self):
        sys.argv = [sys.argv[0]]
        sys.argv.append('lines')
        sys.argv.append('story.txt')
        wc_l = int(check_output(["wc", "-l", 'story.txt']).split()[0])
        self.assertEqual(wc_l, solution.main())

    def test_no_files(self):
        sys.argv = [sys.argv[0]]
        self.assertEqual("No given arguments!", solution.main())


if __name__ == '__main__':
   unittest.main()
