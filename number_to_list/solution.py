def number_to_list(n):
	new_list = []
	while (n>10):
		new_list.append(n%10)
		n //= 10
	new_list.append(n)
	new_list.reverse()
	return new_list
def main():
	print( number_to_list(123) )
	print( number_to_list(99999) )
	print( number_to_list(123023) )
if __name__ == '__main__':
	main()