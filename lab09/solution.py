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

