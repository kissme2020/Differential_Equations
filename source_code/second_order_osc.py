# second_ordr_osc.py

#Graph second order ODE oscillation

import numpy as np
import matplotlib.pyplot as plt

def ODE(inputFrequency, natrualFrequenay, t):
    """ Assumes inputFrequency and natrualFrequenay
    is a positive real number and t is time.    
    Return amplitue as its time."""
    if inputFrequency != natrualFrequenay:
        # (D^2 + natrualFrequenay^2) = cos(inputFrequency * t)
        return np.cos(inputFrequency * t)/(natrualFrequenay**2 - inputFrequency**2) 
    else:
        return (t * np.sin(natrualFrequenay)) /(2 * natrualFrequenay) 

def GetDampLine(natrualFrequenay, t):
    """ Assumes a natrualFrequenay is positive real number
    and t is time. 
    Return Damped line when pure oscillation. """
    return (t/2*natrualFrequenay)

#test code
#Get value of Resonance
omega0 = 3.0  # Natural Frequency
# Input Frequency
omega1 = 1; stop_omega1 = omega0; delta_omega1 = 0.5
# Time 
time = np.arange(0, 6*np.pi, 0.01)
# Save result
ODEResult = dict()
#Loop for change input frequency
while omega1 <= omega0:
    # print(omega1)
    # Get date from time.
    result = [] 
    for t in time:
        result.append(ODE(omega1, omega0, t))
    ODEResult.update({"Input Frequency {:2.1f}".format(omega1) : result})     
    # # Get Demped line when input Frequency == natural frequency
    # if omega1 == omega0:
    #     result = []
    #     for t in time:
    #         result.append(GetDampLine(omega0, t))
    #     ODEResult.update({"Damped Line" : result})     
    print(omega1)    
    omega1 = omega1 + delta_omega1
    omega1 = round(omega1, 2)
# Plot
# Extract Keys
for key in ODEResult.keys():
    plt.plot(time, ODEResult[key])
plt.show()

# There is homogeneous equations, so, It can not be show correct graph 
