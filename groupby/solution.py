def groupby(func, seq):
	grouped_dict = {}
	for i in seq:
		grouped_dict[func(i)] = []
	for i in seq:
		for key in grouped_dict:
			if (key == func(i)):
				grouped_dict[key].append(i)
	return grouped_dict

def main():
	print ( groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]) )
	print ( groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]) )
	print ( groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]) )
if __name__ == '__main__':
	main()