import solution
import unittest

class ReduceFilePathTest(unittest.TestCase):

	def test_reduce_file_path_1st(self):
		self.assertEqual("/", solution.reduce_file_path("/"))

	def test_reduce_file_path_2nd(self):
		self.assertEqual("/", solution.reduce_file_path("/srv/../"))

	def test_reduce_file_path_3rd(self):
		self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf/"))

	def test_reduce_file_path_4th(self):
		self.assertEqual("/srv/www/htdocs/wtf", solution.reduce_file_path("/srv/www/htdocs/wtf"))

	def test_reduce_file_path_5th(self):
		self.assertEqual("/srv", solution.reduce_file_path("/srv/./././././"))

	def test_reduce_file_path_6th(self):
		self.assertEqual("/etc/wtf", solution.reduce_file_path("/etc//wtf/"))

	def test_reduce_file_path_7th(self):
		self.assertEqual("/", solution.reduce_file_path("/etc/../etc/../etc/../"))

	def test_reduce_file_path_8th(self):
		self.assertEqual("/", solution.reduce_file_path("//////////////"))

	def test_reduce_file_path_9th(self):
		self.assertEqual("/", solution.reduce_file_path("/../"))


if __name__ == '__main__':
	unittest.main()