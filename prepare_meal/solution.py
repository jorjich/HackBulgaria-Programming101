def prepare_meal(number):
	max = 0
	new_string = ""
	return_string = ""
	eggs = False
	if (number % 5 == 0):
		number = number // 5
		eggs = True
	for i in range(0, number//3+1):
		if(3**i == number):
			if (i > max):
				max = i
	new_string = ("spam ") * max
	if (max == 0):
		if(eggs):
			new_string = new_string + ("eggs")
		else:
			return "\"\""
	elif (eggs):
		new_string = new_string + ("and eggs")
	if(new_string[len(new_string)-1] == " "):
		return_string = "\"" + new_string[:len(new_string)-1] + "\""
	else:
		return_string = "\"" + new_string + "\""
	return return_string
def main():
		print( prepare_meal(5) )
		print( prepare_meal(3) )
		print ( prepare_meal(27) )
		print ( prepare_meal(15) )
		print ( prepare_meal(45) )
		print ( prepare_meal(7) )
if __name__ == '__main__':
		main()