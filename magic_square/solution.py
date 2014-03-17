def magic_square(matrix):
    res = [sum(matrix[0]) for i in range(0, len(matrix) + len(matrix[0]) + 2)]

    sums = []
    sums += [sum(item) for item in matrix]
    sums += [sum(item) for item in zip(*matrix)]
    l = len(matrix[0])
    sums.append(sum([matrix[i][i] for i in range(l)]))
    sums.append(sum([matrix[l-1-i][i] for i in range(l-1,-1,-1)]))
    return res == sums

def main():
    print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
    print(magic_square([[4,9,2], [3,5,7], [8,1,6]]))
    print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

if __name__ == '__main__':
    main()
