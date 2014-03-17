def is_prime(m):
	count = 0
	m = abs(m)
	if(m == 1):
		return 0
	if (m == 2):
		return 1
	for i in range(2, m):
		if( m % i == 0):
			return 0
	return 1

def goldbach(n):
	number = 0
	first_prime_list = []
	second_prime_list = []
	m = n//2
	for i in range(1,m+1):
		if(is_prime(i) == 1):
			number = n - i
			if(is_prime(number) == 1):
				first_prime_list.append(i)
				second_prime_list.append(number)
	zipped = zip(first_prime_list, second_prime_list)
	return list(zipped)

def main():
	print ( goldbach(4) )
	print ( goldbach(6) )
	print ( goldbach(8) )
	print ( goldbach(10) )
	print ( goldbach(100) )
if __name__ == '__main__':
		main()
