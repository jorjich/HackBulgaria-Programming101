def list_to_number(digits):
	number = 0
	for i in digits:
		number += i
		number *= 10
	number //= 10
	return number
def main():
	print( list_to_number([1,2,3]) )
	print( list_to_number([9,9,9,9,9]) )
	print( list_to_number([1,2,3,0,2,3]) )
if __name__ == '__main__':
	main()