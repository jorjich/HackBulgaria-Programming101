def count_consonants(str):
	str = str.lower()
	count_all = len(str)
	for i in str:
		if(i=="a" or i=="o" or i=="e" or i=="i" or i=="u" or i=="y" or i==" " or i=="!" or i==","):
			count_all -= 1
	return count_all
def main():
	print( count_consonants("Python") )
	print( count_consonants("Theistareykjarbunga") )
	print( count_consonants("grrrrgh!") )
	print( count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
	print( count_consonants("A nice day to code!") )
if __name__ == '__main__':
	main()