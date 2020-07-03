import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.ticker as ticker
import numpy as np

from lagrange import lagrange_t
from bezier import bezier_t
from splines import b_spline_t

def calcular (t_desde , t_hasta , funcion , puntos , segmentos =150):
    t  = np.linspace(t_desde , t_hasta, num =segmentos)
    p = np.array(list(map (lambda t_i:funcion(t_i, puntos),t)))
    return p.T , t

def graficar_color (p_t, t , puntos , nombre):
    p_t = np.array([p_t[0],p_t[1]]).T.reshape(-1, 1, 2)
    
    fig, axs = plt.subplots(figsize=(8,8))
    plt.axis('equal')
    axs.xaxis.set_major_locator(ticker.MultipleLocator(1))
    axs.yaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.grid()
    plt.plot (puntos[: ,0 ] , puntos[: , 1],"--",linewidth =0.5  )
    plt.scatter(puntos[: ,0 ] , puntos[: , 1], c ="#1DDCA5" )
    
    lc = LineCollection(np.concatenate([p_t[:-1], p_t[1:]], axis=1),
                        cmap='plasma',
                        norm=plt.Normalize(t.min(), t.max()))
    lc.set_array(t)
    lc.set_linewidth(2)
    line = axs.add_collection(lc)
    cb = fig.colorbar(line, ax=axs )
    cb.ax.set_xlabel('t')

    margen = 0.2
    axs.set_xlim(puntos[:,0].min()-margen,puntos[:,0].max()+margen)
    axs.set_ylim(puntos[:,1].min()-margen,puntos[:,1].max()+margen)
    fig.suptitle(nombre, fontsize=16)
    plt.show()

if __name__ == "__main__":
    #Puntos item a y b
    puntos = np.array([[-3 , 0] , [-1 , 4] , [2,3]  , [4,1]])
    p_t,t  = calcular(0 , 3 , lagrange_t , puntos)
    graficar_color(p_t,t, puntos , "Interpolacion de lagrange")

    p_t,t = calcular(0,1 , bezier_t , puntos )
    graficar_color(p_t,t , puntos , "Curva de bezier")

    puntos = np.array([[-1, 0] , [1 , 4] , [3,-2]  , [4,3] , [6,1]])
    
    p_t,t = calcular(3,5 , b_spline_t , puntos)
    graficar_color(p_t ,t , puntos, "Curva b-spline")