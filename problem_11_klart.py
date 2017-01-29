
from numpy import *

ar = zeros([20,20], dtype = long)

ar[0][:] = [8, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 8]
ar[1][:] = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00]
ar[2][:] = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65]
ar[3][:] = [52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91]
ar[4][:] = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
ar[5][:] = [24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
ar[6][:] = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
ar[7][:] = [67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
ar[8][:] = [24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
ar[9][:] = [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95]
ar[10][:] = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 9, 53, 56, 92]
ar[11][:] = [16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57]
ar[12][:] = [86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
ar[13][:] = [19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40]
ar[14][:] = [04, 52, 8, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
ar[15][:] = [88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
ar[16][:] = [04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
ar[17][:] = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16]
ar[18][:] = [20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54]
ar[19][:] = [01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48]


def calc_rows(A, i, j):
	list = []
	for row in range(i, i+4):
		product = 1
		for element in A[row, j:j+4]:
			product *= element
		list.append(product)
	list.sort()
	return list[-1]

def calc_columns(A, i, j):
	list = []
	for column in range(j, j+4):
		product = 1
		for element in A[i:i+4, column]:
			product *= element
		list.append(product)
	list.sort()
	return list[-1]

def calc_diagonals(A, i, j):
	list = []
	product = 1
	for k in range(0,4):
		product *= A[i+k, j+k]
	list.append(product)
	product = 1
	for k in range(0,4):
		product *= A[i+3-k, j+k]
	list.append(product)
	list.sort()
	return list[-1]


def calc_box(A, i, j):
	column_value = calc_columns(A, i, j)
	row_value = calc_rows(A, i, j)
	diagonal_value = calc_diagonals(A, i, j)
	list = [column_value, row_value, diagonal_value]
	list.sort()
	return list[-1]

if __name__ == '__main__':
	
	greatest_value = 0
	for i in range(0, 17):
		for j in range(0, 17):
			value = calc_box(ar, i, j)
			if value > greatest_value:
				greatest_value = value
	
	print greatest_value
