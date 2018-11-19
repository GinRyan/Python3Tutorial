import numpy as np

arr1 = np.array([[1, 3, 5, 6, 4], [2, 3, 6, 1, 5]])
arr2 =  np.array([[4, 2, 0, -1, 1], [3, 2, -1, 4, 0]])
dest = arr1 + arr2
dest2 = arr1 * 2
dest3 = arr1 / 2
dest4 = arr1 * arr2
print(arr1)
print(arr2)
print(dest)
print(dest2)
print(dest3)
print(dest4)
print(arr1.dtype)
print(arr1.shape)
print(arr1.flatten())

print(dest4 > 2)