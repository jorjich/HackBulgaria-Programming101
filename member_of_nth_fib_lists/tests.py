import solution
import unittest

class MemberOfNthFibListsTest(unittest.TestCase):

	def test_member_of_nth_fib_lists_1st(self):
		self.assertEqual(False, solution.member_of_nth_fib_lists([1,2],[3,4],[5,6]))

	def test_member_of_nth_fib_lists_2nd(self):
		self.assertEqual(True, solution.member_of_nth_fib_lists([1,2],[3,4],[1,2,3,4,3,4,1,2,3,4]))

	def test_member_of_nth_fib_lists_3rd(self):
		self.assertEqual(True, solution.member_of_nth_fib_lists([7,11],[2],[7,11,2,2,7,11,2]))

	def test_member_of_nth_fib_lists_4th(self):
		self.assertEqual(False, solution.member_of_nth_fib_lists([7,11],[2],[11,7,2,2,7]))

if __name__ == '__main__':
	unittest.main()