def is_increasing(seq):
	is_true = False
	length = len(seq)
	if(length==1):
		return True
	for i in range(0, length-1):
		if(seq[i] < seq[i+1]):
			is_true = True
		else:
			is_true = False
	return is_true
def main():
	print( is_increasing([1,2,3,4,5]) )
	print( is_increasing([1]) )
	print( is_increasing([5,6,-10]) )
	print( is_increasing([1,1,1,1]) )
if __name__ == '__main__':
	main()