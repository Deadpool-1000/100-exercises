from math import pi
# Question:  
# Please write a function that calculates liquid volume in a sphere using the following formula. 
# The radius r  is always 10, so consider making it a default parameter.

def volume_of_partially_filled_sphere(h, r=10):
    v = (4*pi*(r**3))/3 - (pi*(h**2)*(3*r - h)/3)
    return v

print(volume_of_partially_filled_sphere(2))
