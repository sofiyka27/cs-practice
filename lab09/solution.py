import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    arr = np.asarray(values)
    
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist()
    }

def change_vector(values):
    arr = np.asarray(values).copy()
    arr[2:5] = 99
    arr[::2] = -1
    
    return arr.tolist()

def cap_above(values, limit):
    arr = np.asarray(values)
    mask = arr > limit
    arr[mask] = limit
    
    return arr.tolist()

def celsius_to_fahrenheit(values):
    arr = np.asarray(values)
    fahrenheit = arr * 9 / 5 + 32
    
    return fahrenheit.tolist()