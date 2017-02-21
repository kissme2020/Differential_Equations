# spring-mass-dashpot.py

# The spring mass dahpot systme.
# mx'' + bx' + kx = 0 m,k > 0, b >= 0.
# Where m is mass , b is dashpot and k is spring constat.
# Plot each of graph one or two of constants varied  other.  

import numpy as np

def GetDiscriminant(a, b, c):
    """ assmus b and c  is a real number. 
    Return Discriminant of quadactic formula. """
    return b**2 -4*a*c

def getResponse(m, k, b):
    """Assume m and k are positive real number 
    and b is positive real number or zero. 
    Return real and imangary part of root. """
    
    

    

def GetRealSoluation(c1, c2, p, omage_d, t)
    """Assume c1, c2 and omage_d is real number. 
    c1 : initail position 
    c2 : initail velocity
    return a function amplitude * cos(omage * t - phi). """
    return np.cos(omage*t - phi)

def GetAmplitude(constant1, constant2, t):
    """Assume constant1, constant2 and t is real number. 
    Return constant1 * exp(constant2 * t), """
    return constant1 * np.exp(constant2 * t)

def GetDiscriminant(a, b, c):
    """ assmus b and c  is a real number. 
    Return Discriminant of quadactic formula. """
    return b**2 -4*a*c



# test code
import matplotlib.pyplot as plt

t_0 = 0; delta_t = 0.001; t_final = 12
omage = 1; phi = np.pi/4 
constant1 = np.sqrt(2); constant2 = -1/4
time = []; sinusoidal = []; upper = []; lower = [] 

t = t_0
while t < t_final:
    time.append(t)
    upper.append(GetAmplitude(constant1, constant2, t))
    lower.append(GetAmplitude(-constant1, constant2, t))
    sinusoidal.append(upper[-1] * GetSinusoidal(omage, phi, t))
    t += delta_t

plt.xlabel("Time")
plt.plot(time, sinusoidal, label="underdamped")
plt.plot(time, upper, label="upper envelope")
plt.plot(time, lower, label="lower envelope")
plt.xlim(min(time), max(time))
# plt.yscale('log')
plt.grid(True)
plt.legend()

plt.show()
