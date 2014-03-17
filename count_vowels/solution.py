def count_vowels(str):
	str = str.lower()
	count = 0
	for i in str:
		if(i=="a" or i=="o" or i=="e" or i=="i" or i=="u" or i=="y"):
			count += 1
	return count
def main():
	print( count_vowels("Python") )
	print( count_vowels("Theistareykjarbunga") )
	print( count_vowels("grrrrgh!") )
	print( count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
	print( count_vowels("A nice day to code!") )
if __name__ == '__main__':
	main()