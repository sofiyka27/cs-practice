import numpy as np

hours = np.arange(0,22,3)
line = np.linspace(0,1,5)
zeros = np.full((1,6),0)
unknown_table = np.full((2,3),-1)
identity = np.ones((3,3))

print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

#2
print(hours[2])
print(hours[-1])
print(hours[2:5])
print(hours[::2])
print(hours[::-1])

#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1,2])
print(temperatures[0,:])
print(temperatures[:,-1])
print(temperatures[:2,1:])
print(temperatures[:2,1:3])

#4
matrix = np.arange(1, 26).reshape(5, 5)
matrix1 = matrix[:3,:]
print(matrix1)
print(matrix1.shape)
matrix2 = matrix[3:,:]
print(matrix2)
print(matrix2.shape)
matrix3 = matrix[:,:2]
print(matrix3)
print(matrix3.shape)
matrix4 = matrix[1:4,2:]
print(matrix4)
print(matrix4.shape)
matrix5 = matrix[3:,3:]
print(matrix5)
print(matrix5.shape)

#5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print(changed_hours)
print(hours)
# copy() нужен, чтобы мы не потеряли данные о переменной hours
# если сделать changed_hours = hours то мы сотрем исходную hours

#6
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print(numbers.shape)
print(table.shape)
print(transposed.shape)
