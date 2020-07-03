import numpy as np

def alfa(t, i):
    if i == 0:
        return ((t-1)*(t-2)*(t-3)) / (-6.0)
    if i == 1:
        return ((t)*(t-2)*(t-3)) / (2.0)
    if i == 2:
        return ((t)*(t-1)*(t-3)) / (-2.0)
    if i == 3:
        return ((t)*(t-1)*(t-2)) / (6.0)
    return 0


def lagrange_t(t, puntos: np.array):
    r = np.zeros(2)
    for i in range(4):
        r = r + puntos[i]*alfa(t, i)
    return r
