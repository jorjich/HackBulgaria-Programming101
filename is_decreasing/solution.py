def is_decreasing(seq):
	is_true = False
	length = len(seq)
	if(length==1):
		return "True"
	for i in range(0, length-1):
		if(seq[i] > seq[i+1]):
			is_true = True
		else:
			is_true = False
	return is_true
def main():
	print( is_decreasing([5,4,3,2,1]) )
	print( is_decreasing([1,2,3]) )
	print( is_decreasing([100, 50, 20]) )
	print( is_decreasing([1,1,1,1]) )
if __name__ == '__main__':
	main()