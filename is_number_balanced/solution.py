def is_number_balanced(n):
	m = str(n)
	first_part = 0
	second_part = 0
	sum_first_part = 0
	sum_second_part = 0
	if(len(m)<2):
		return True
	else:
		parts = len(m) // 2
		if(len(m) % 2 == 0):
			first_part = int(m[:parts])
			second_part = int(m[parts:])
			sum_first_part = sum_of_digits(first_part)
			sum_second_part = sum_of_digits(second_part)
			if(sum_first_part == sum_second_part):
				return True
			else:
				return False
		else:
			first_part = int(m[:parts])
			second_part = int(m[parts+1:])
			sum_first_part = sum_of_digits(first_part)
			sum_second_part = sum_of_digits(second_part)
			if (sum_first_part == sum_second_part):
				return True
			else:
				return False

def sum_of_digits(n):
	n = abs(n)
	sum = 0
	while(n>9):
		sum += ( n%10 )
		n //= 10
	sum += n
	return sum

def main():
	print( is_number_balanced(9) )
	print( is_number_balanced(11) )
	print( is_number_balanced(13) )
	print( is_number_balanced(121) )
	print( is_number_balanced(4518) )
	print( is_number_balanced(28471) )
	print( is_number_balanced(1238033) )
if __name__ == '__main__':
	main()