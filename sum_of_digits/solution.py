def sum_of_digits(n):
	n = abs(n)
	sum = 0
	while(n>9):
		sum += ( n%10 )
		n //= 10
	sum += n
	return sum

def main():
	print( sum_of_digits(1325132435356))
	print( sum_of_digits(123) )
	print( sum_of_digits(6) )
	print( sum_of_digits(1) )
if __name__ == '__main__':
	main()