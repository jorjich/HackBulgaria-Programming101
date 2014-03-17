def prime_number_of_divisors(n):
	number = 0
	for i in range(1, n):
		if ( n % i == 0):
			number += 1
	number += 1
	return is_prime(number)
def is_prime(n):
	count = 0
	n = abs(n)
	if(n == 1):
		return "False"
	if (n == 2):
		return "True"
	for i in range(2, n):
		if( n % i == 0):
			return "False"
	return "True"
def main():
	print( prime_number_of_divisors(7) )
	print( prime_number_of_divisors(8) )
	print( prime_number_of_divisors(9) )
if __name__ == '__main__':
	main()