def slope_style_score(scores):
	maxy=max(scores)
	miny=min(scores)
	sum = 0
	for i in scores:
		sum += i
	sum = sum - (miny + maxy)
	total = sum/float(len(scores)-2)
	return round(total, 2)
def main():
	print( slope_style_score([94, 95, 95, 95, 90]) )
	print( slope_style_score([60, 70, 80, 90, 100]) )
	print( slope_style_score([96, 95.5, 93, 89, 92]) )
if __name__ == '__main__':
	main()