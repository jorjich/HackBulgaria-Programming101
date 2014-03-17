def nth_fib_lists(list1, list2, n):
	first = list1
	second = list2
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

def member_of_nth_fib_lists(listA, listB, needle):
	haystack = nth_fib_lists(listA,listB, 10)
	exit_status = False
	exit_status = sublistExists(haystack, needle)
	return exit_status

def sublistExists(list, sublist):
    for i in range(len(list)-len(sublist)+1):
        if sublist == list[i:i+len(sublist)]:
            return True
    return False 

def main():
	print ( member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]) )
	print ( member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]) )
	print ( member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]) )
	print ( member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]) )
if __name__ == '__main__':
		main()