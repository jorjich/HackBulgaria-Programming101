def is_int_palindrome(n):
	n = abs(n)
	original_number = n
	new_number = 0
	while(n>9):
		new_number += (n % 10)
		new_number *= 10
		n //= 10
	new_number += n
	if (new_number == original_number):
		return "True"
	else:
		return "False"
def main():
	print( is_int_palindrome(1) )
	print( is_int_palindrome(42) )
	print( is_int_palindrome(100001) )
	print( is_int_palindrome(999) )
	print( is_int_palindrome(123) )
if __name__ == '__main__':
	main()