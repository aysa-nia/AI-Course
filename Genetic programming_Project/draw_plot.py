import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from scipy.interpolate import make_interp_spline



def draw_2plot(x1 , y1 , x2 , y2):
    plt.plot(x1, y1, label = "line 1")
    plt.plot(x2, y2, label = "line 2")
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()



def draw_curved_plot(p1 , p2):
    x = np.array(p1)
    y = np.array(p2)
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = X_Y_Spline(X_)
    plt.plot(X_, Y_)
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.show()

