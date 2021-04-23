import numpy as np

from Blok4.AnalyticalComputing.v1ac.ac_exceptions import DimensionError

x= np.array([[12,7,3],
    [4 ,5,6],
    [7 ,8,9]])

y =np.array( [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]])

def inner_product(u: np.ndarray, v: np.ndarray) -> np.ndarray:  # TODO
    if len(u) != len(v):
        raise DimensionError

    else:
        for x in range(len(u)):
            return sum([u[x] * v[x]])

def matrix_product(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    if M.shape[-1] == len(v):

        for i in M:
            return np.array([inner_product(i, v)])

    else:

        raise DimensionError("Matrix en vector zijn niet hetzelfde formaat.")


print(matrix_product(x,y))