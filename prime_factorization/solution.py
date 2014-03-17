def prime_factorization(number):
    number = int(number)
    prime_list = [ ]
    for divisor in range(2, number + 1):
        counter = 0
        while number % divisor == 0:
            counter += 1
            number //= divisor

            if (number % divisor != 0):
                doubles = (divisor, counter)
                prime_list.append(doubles)

    return prime_list

def main():
	print (prime_factorization(10))
	print (prime_factorization(14))
	print (prime_factorization(356))
	print (prime_factorization(89))
	print (prime_factorization(1000))
if __name__ == '__main__':
		main()