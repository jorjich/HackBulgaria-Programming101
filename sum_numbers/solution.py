import sys
from random import randint

def sum_numbers(filename):
	sum = 0
	if len(sys.argv) == 2:
		with open(sys.argv[1], "r") as file:
			content = file.read()
			x = content.strip("\n").split(" ")
			for i in x:
				sum += int(i)
		return sum
	elif len(sys.argv) > 2:
		return "Too many arguments"

	else:
		return "No given arguments!"
	return




def main():
	return sum_numbers(sys.argv)


if __name__ == '__main__':
	main()
