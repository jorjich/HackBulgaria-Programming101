def count_words(arr):
	new_dict = {}
	count = 0
	for i in arr:
		for j in arr:
			if (i==j):
				count += 1
		if not(i in new_dict):
			new_dict[i] = count
		count = 0
	return new_dict

def main():
	print ( count_words(["apple", "banana", "apple", "pie"]) )
	print ( count_words(["python", "python", "python", "ruby"]) )
if __name__ == '__main__':
	main()