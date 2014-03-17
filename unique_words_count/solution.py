def unique_words_count(arr):
	unique_list = []
	for i in arr:
		if not(i in unique_list):
			unique_list.append(i)
	return len(unique_list)

def main():
		print( unique_words_count(["apple", "banana", "apple", "pie"]) )
		print( unique_words_count(["python", "python", "python", "ruby"]) )
		print ( unique_words_count(["HELLO!"] * 10) )
if __name__ == '__main__':
		main()