# plot_underdamped.py 

# plot underdamped response 

import numpy as np

def GetSinusoidal(omage, phi, t):
    """ Assume that amplitude and omage is real number. 
    return a function amplitude * cos(omage * t - phi). """
    return np.cos(omage*t - phi)

def GetAmplitude(constant1, constant2, t):
    """Assume constant1, constant2 and t is real number. 
    Return constant1 * exp(constant2 * t), """
    return constant1 * np.exp(constant2 * t)    

# test code
import matplotlib.pyplot as plt

t_0 = 0; delta_t = 0.001; t_final = 12
omage = 1; phi = np.pi/4 
constant1 = np.sqrt(2); constant2 = -1/4
time = []; sinusoidal = []; upper = []; lower = []
halfperiod = []; yline = [] 

t = t_0
while t < t_final:
    time.append(t)
    upper.append(GetAmplitude(constant1, constant2, t))
    lower.append(GetAmplitude(-constant1, constant2, t))
    sinusoidal.append(upper[-1] * GetSinusoidal(omage, phi, t))
    #half period of time 
    if (t >= (3*np.pi) / 4) and  ( t <=  ((3*np.pi) / 4 + np.pi) ):
        halfperiod.append(t)    
    t += delta_t
# horizontal line for half period    
for val in halfperiod:
    yline.append(0)
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time, sinusoidal, label="underdamped")
ax.plot(time, upper, label="upper envelope")
ax.plot(time, lower, label="lower envelope")
ax.plot(halfperiod, yline)
ax.annotate('Half of Period',
            xy=(sum(halfperiod) / len(halfperiod), 0),
            xytext=(3, 0.64),
            arrowprops=dict(facecolor='black', shrink=0.05),)
ax.annotate(r'$e^{-pt}$',
            xy=(sum(time) / len(time),
                sum(upper) / len(upper)),
            xytext=(6.6, 1),
            arrowprops=dict(facecolor='black', shrink=0.05),)

ax.set_xlim(min(time), max(time))
ax.set_xlabel("Time")
ax.grid(True)
# ax.legend()

plt.show()
