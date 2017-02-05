# recitation1.py
## recitation1 plot graph.
import math
import matplotlib.pyplot as plt
import numpy as np

# Formulare for ODE. : (x_0 - a/k)*e^(k*t) + a/k
def Afunction(x_0, a, k, t):
    """ Assumes x_0 and a, k are real number.
    x_0 : initial population. 
    a : rate of hunting
    k : rate of natural growth. 
    t : time 
    Return function result. """
    return (x_0 - a/k)*np.exp(k*t) + a/k
    

time = np.arange(0.0, 10, 0.1)  # Change in time. 
a = 20
k = 0.2 
#Constant Solution
constant = a/k 
x_0 = 0; x = x_0; delta_x = 50 ;x_final = constant+(2*delta_x)
result = {}
# loop change initial condition 
while x <= x_final:
    if x == 100:
        key = "Constant Solution"
    else:
        key = "x_0 = {}".format(str(x))
    y = []
    for t in time:
        y.append(Afunction(x, a, k, t))
    result.update({key: y})
    x += delta_x

for k in result.keys():
    plt.plot(time, result[k], label=k)
plt.legend()
plt.title("Growth of Oryxes by initial")
plt.xlabel("Time in years")
plt.ylabel("Number of Oryxes")
plt.xlim(time[0], time[-1])
plt.grid(True)
plt.show()






