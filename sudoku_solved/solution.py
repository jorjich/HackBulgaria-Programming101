def sudoku_solved(sudoku):
	sum_rows = 0
	sum_columns = 0
	for i in range(0,9):
		for j in range(0,9):
			sum_rows += sudoku[i][j]
			sum_columns += sudoku[j][i]
		if(sum_rows != 45 or sum_columns !=45):
			return False
		else:
			sum_rows = 0
			sum_columns = 0
	sum_subsquares = 0
	# it will be much better with a for cycle but have no time
	# 1st square on 1st row
	sum_subsquares = sudoku[0][0] + sudoku[0][1] + sudoku[0][2] + sudoku[1][0] + sudoku[1][1] + sudoku[1][2] + sudoku[2][0] + sudoku[2][1] + sudoku[2][2]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	#2nd square on 1st row
	sum_subsquares = sudoku[0][3] + sudoku[0][4] + sudoku[0][5] + sudoku[1][3] + sudoku[1][4] + sudoku[1][5] + sudoku[2][3] + sudoku[2][4] + sudoku[2][5]
	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	# 3rd square on 1st row 
	sum_subsquares = sudoku[0][6] + sudoku[0][7] + sudoku[0][8] + sudoku[1][6] + sudoku[1][7] + sudoku[1][8] + sudoku[2][6] + sudoku[2][7] + sudoku[2][8]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	#1st square on 2nd row
	sum_subsquares = sudoku[3][0] + sudoku[3][1] + sudoku[3][2] + sudoku[4][0] + sudoku[4][1] + sudoku[4][2] + sudoku[5][0] + sudoku[5][1] + sudoku[5][2]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	# 2nd square on 2nd row
	sum_subsquares = sudoku[3][3] + sudoku[3][4] + sudoku[3][5] + sudoku[4][3] + sudoku[4][4] + sudoku[4][5] + sudoku[5][3] + sudoku[5][4] + sudoku[5][5]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	# 3rd square on 2nd row
	sum_subsquares = sudoku[3][6] + sudoku[3][7] + sudoku[3][8] + sudoku[4][6] + sudoku[4][7] + sudoku[4][8] + sudoku[5][6] + sudoku[5][7] + sudoku[5][8]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	#1st square on 3rd row
	sum_subsquares = sudoku[6][0] + sudoku[6][1] + sudoku[6][2] + sudoku[7][0] + sudoku[7][1] + sudoku[7][2] + sudoku[8][0] + sudoku[8][1] + sudoku[8][2]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	#2nd square on 3rd row
	sum_subsquares = sudoku[6][3] + sudoku[6][4] + sudoku[6][5] + sudoku[7][3] + sudoku[7][4] + sudoku[7][5] + sudoku[8][3] + sudoku[8][4] + sudoku[8][5]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0

	# 3rd square on 3rd row
	sum_subsquares = sudoku[6][6] + sudoku[6][7] + sudoku[6][8] + sudoku[7][6] + sudoku[7][7] + sudoku[7][8] + sudoku[8][6] + sudoku[8][7] + sudoku[8][8]

	if (sum_subsquares != 45):
		return False
	else:
		sum_subsquares = 0
	return True
def main():
	print (sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
	print (sudoku_solved([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9]
]))
if __name__ == '__main__':
	main()