# Orbit of the Moon and the Earth Simulation
# Jared Vu and Stephen Blevins
# Description: Our term project will be to design a simulation of the moon orbiting the Earth while the Earth orbits the sun.
# We were interested in finding out whether the Moon would leave the Earth's orbit and if so, when it would happen.
# 
#----------------------------------------------------------------

from visual import *

# Initialization of the Sun, Earth, and Moon.

def init():
    # Initialize Masses(kg)
    S_Mass = 1.98855*10**(float(30))
    E_Mass = 5.972*10**(float(24))
    M_Mass = 7.347*10**(float(22))
    # Initialize shapes
    # Distance between Sun and Earth = 149.6 million km
    # Distance between Moon and Earth = 384,400 km
    # Radius of Sun = 695,700km
    # Radius of Earth = 6371 km
    # Radius of Moon = 1737 km
    Sun = sphere(pos=(0,0,0), radius=10, color=color.yellow)
    Earth = sphere(pos=(92.96,0,0), radius=1, material=materials.BlueMarble)
    #Moon = sphere(pos=(

init()

