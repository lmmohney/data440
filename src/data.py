import numpy as np


def make_data(n: int) -> np.array:
    '''
    return an array of n random numbers
    '''
    return np.random.random(size=n)