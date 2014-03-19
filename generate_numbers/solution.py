import sys
from random import randint

def generate_numbers(*args):
	if( len(sys.argv) == 3):
		filename = sys.argv[1]
		n = int(sys.argv[2])
		file = open(filename, "w")
		for i in range(0,n):
			rand_number = randint(1,1000)
			file.write(" ".join(str(rand_number)))
		file.close()
	elif( len(sys.argv) > 3):
		print ("Too much arguments")
	else:
		print ("No arguments given")

def main():
	generate_numbers(sys.argv)

if __name__ == '__main__':
		main()
