import numpy as np

#Create array of linery spaced elements between 0 and 9

arr= np.linspace(0, 9, 10, dtype=int)
print('Original Array')
print(arr)

#Replace all numbers with -1 without modifying the original

arr_copy = arr.copy()
arr_copy[arr_copy % 2 == 1] = -1
print("\nModified array (odds replaced with -1):")
print(arr_copy)


#Convert original array into 2d with two rows
arr_2d = arr.reshape(2, -1)
print("\n2D array with 2 rows:")
print(arr_2d)

#  find sum of all elements
total_sum = arr.sum()


print("\nSum of all elements in original array:", total_sum)