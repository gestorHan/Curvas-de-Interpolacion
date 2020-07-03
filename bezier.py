import numpy as np
def b_3(t,i):
    if i == 0:
        return (1-t)**3
    if i == 1:
        return 3*t*((1-t)**2)
    if i == 2:
        return 3*(t**2)*(1-t)
    if i == 3:
        return t**3
    return 0
    
def bezier_t (t,puntos:np.array):
    m = np.zeros(2)
    for i in range (4):
        m = m +  puntos[i]*b_3(t, i) 
    return m