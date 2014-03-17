def contains_digits(number, digits):
	is_it = False
	if(len(digits) == 0):
		is_it = True
	for i in digits:
		while(number>10):
			if(number % 10 == i):
				is_it = True
			number //= 10
		if(number == i):
			is_it = True
		else:
			is_it = False
	if (is_it):
		return "True"
	else:
		return "False"
def main():
	print( contains_digits(402123, [0, 3, 4]) )
	print( contains_digits(666, [6,4]) )
	print( contains_digits(123456789, [1,2,3,0]) )
	print( contains_digits(456, []) ) 
if __name__ == '__main__':
	main()