from fractions import gcd

def simplify_fraction(fraction):
	first = fraction[0]
	second = fraction[1]
	greatest = gcd(first,second)
	first = first / greatest
	second = second / greatest
	return (first,second)

def sort_fractions(fractions):
	dictionary = {}
	j = 0
	sorted(fractions)
	for i in fractions:
		x = fractions[j][0]
		y = fractions[j][1]
		dictionary[i] = float(x) / y
		j += 1
	return sorted(dictionary, key=dictionary.get)


def main():
		print( sort_fractions([(2, 3), (1, 2)]) )
		print( sort_fractions([(2, 3), (1, 2), (1, 3)]) )
		print ( sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]) )
if __name__ == '__main__':
		main()