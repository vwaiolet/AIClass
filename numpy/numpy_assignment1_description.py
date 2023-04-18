
#아래와 같이 출력하는 Numpy code를 완성하시오
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# Python program to print nXn
# checkerboard pattern using numpy

import numpy as np

# function to print Checkerboard pattern
def printcheckboard(n):
	
	print("Checkerboard pattern:")

	# create a n * n matrix
	arr = np.zeros((n, n))

	# fill with 1 the alternate rows and columns
	arr[1::2, 0::2] = 1
	arr[0::2, 1::2] = 1

	# print the pattern
	print(arr)

# driver code
n = 8
printcheckboard(n)
