class SortedDisplayDict(dict):
   def __str__(self):
       return "{" + ", ".join("%r: %r" % (key, self[key]) for key in sorted(self)) + "}"


def calculate_coins(suma):
	total = 0
	count = 0
	int_suma = int(suma)
	if(int_suma == suma):
		pass
	else:
		suma *= 100
	list_with_coins = [100,50,20,10,5,2,1]
	new_dict = {}
	for i in list_with_coins:
		while True:
			if( (total+i) <= suma):
				total += i
				count += 1
			else:
				break
		new_dict[i] = count
		count = 0		
	return SortedDisplayDict(new_dict)
def main():
	print (calculate_coins(0.53))
	print (calculate_coins(8.94))
if __name__ == '__main__':
	main()