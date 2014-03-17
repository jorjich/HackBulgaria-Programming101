def nth_fib_lists(listA, listB, n):
	first = listA
	second = listB
	current = []
	if( n == 1):
		return first
	elif( n == 2 ):
		return second
	elif( n > 2 ):
		for i in range(3, n+1):
			current = first + second
			first = second
			second = current
		return current
	else:
		return "ERROR"

def main():
	print ( nth_fib_lists([1], [2], 1) )
	print ( nth_fib_lists([1], [2], 2) )
	print ( nth_fib_lists([1, 2], [1, 3], 3) )
	print ( nth_fib_lists([], [1, 2, 3], 4) )
	print ( nth_fib_lists([], [], 100) )
if __name__ == '__main__':
		main()