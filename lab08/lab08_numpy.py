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
