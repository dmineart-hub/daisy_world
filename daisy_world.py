# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:55:29 2023

@author: dmineart
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:21:33 2023

@author: bwj
"""

#File for working on our Daisy World Model. We can try to use a github repository to all 
#work on this together! We'll use the equations from Watson and Lovelock 1983. 

import numpy as np
from scipy.integrate import odeint
import math

#test edit 
#second edit

stef_boltz = 5.670374419e-8 # Stefan-Boltzman constant W⋅m−2⋅K−4
d = 1.49e11 #distance of the Earth from the Sun, in m
Lo = 3.846e26 #luminosity of the Sun, W
Ab = 0.3 #Albedo
emiss=0.996
k_to_c = 273
s = 917 #solar flux W/m^2 set by Watson and Lovelock

#%%
"""
daw / dt = aw (xB-Y)
dab / dt = ab (xB-Y)

ab and aw = areas covered by black and white daisys
x = area of fertile ground not covered by either species
B = growth rate per unit of time
Y - death rate per unit of time

x = p - ab -aw
The area of fertile ground which is uncolonized by daisys, 
where P is the proportion of the planet's surface area which is fertile ground.

The growth rate of the daisies is assumed to be a parabolic function of local temperature, T1

B1 = 1 - 0.003265 (22.5 - T1)^2
which is zero 

stef_boltz(Te + 273)^4 = SL (1-A)

"""

m = emiss*(s*Lo)*(1-Ab) # we still need S, but I have  no clue where to find S. It's apparently the constant having units of flux?
h = m / stef_boltz
o = math.sqrt(math.sqrt(h))

Te = -273 + o
print(Te) #the effective T at which the planet radiates

#%%
"""
F=ste_boltz(Te+273)^4

F is the total radiation lost to space

"""
F = (stef_boltz)*(Te+273)**4
print(F)

#%%
"""
q = SL/stef_boltz -> (T1 +273)^4 = SL/stef_boltz (1-A1)

q = 0 , the local temp all become equal to themean temp
This situation corresponds to perfect "conduction" of energy from higher to lower temps.

q1 = q/4 (273+22.5)^3

q is expressed as the degree to which solar energy, after having been abosrbd by the planet, is 
redistributed amongst the three types of surface 

"""
q = (s*Lo)/(stef_boltz)
print(q)

q1 = (q/4) * (273 +22.5)**3
print(q1)

q0= 0 

#%%


