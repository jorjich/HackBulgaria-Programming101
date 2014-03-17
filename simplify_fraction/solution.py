from fractions import gcd

def simplify_fraction(fraction):
	first = fraction[0]
	second = fraction[1]
	greatest = gcd(first,second)
	first = first // greatest
	second = second // greatest
	return (first,second)
def main():
		print( simplify_fraction((3,9)) )
		print( simplify_fraction((1,7)) )
		print ( simplify_fraction((4,10)) )
		print ( simplify_fraction((63,462)) )
if __name__ == '__main__':
		main()