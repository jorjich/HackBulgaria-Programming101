def sum_of_min_and_max(arr):
	min = arr[0]
	max = arr[0]
	for i in arr:
		if( i < min):
			min = i
		if( i> max):
			max = i
	return min + max
def main():
	print( sum_of_min_and_max([1,2,3,4,5,6,8,9]) )
	print( sum_of_min_and_max([-10,5,10,100]) )
	print( sum_of_min_and_max([1]) )
if __name__ == '__main__':
	main()