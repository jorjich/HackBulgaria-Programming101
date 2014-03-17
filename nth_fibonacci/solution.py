def nth_fibonacci(n):
	first = 1
	second = 1
	current = 1
	if(n == 1):
		return first
	elif(n == 2):
		return second
	elif( n > 2):
		for i in range(3, n+1):
			current = first + second
			first = second
			second = current
		return current
	else:
		return "ERROR"
def main():
	print ( nth_fibonacci(1) )
	print ( nth_fibonacci(2) )
	print ( nth_fibonacci(3) )
	print ( nth_fibonacci(10) )
if __name__ == '__main__':
	main()