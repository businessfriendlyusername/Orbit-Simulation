# Orbit of the Moon and the Earth Simulation
# simulation.py
# Jared Vu and Stephen Blevins
#
# --------------------------------------------------------
from visual import *
from Body import *
from Integrator import *
import math

scene = display(title='Orbit Sim', width = 1000, height=1000, center=(0,0,0))
G = 6.66308 * math.pow(10, -11)
bodies = []

#Time Variables that can be changed
time = 0
dt = 86400 / 100
years = 5000
final_time = 86400 * 365 * years
rate_ani = 10000

#Append Bodies to be used in Sim
bodies.append(Body(0, 0, 1.98855*math.pow(10,30))) # sun
bodies.append(Body(29800, 149600000000, 5.972*math.pow(10,24))) # earth

var = [0.0] * len(bodies) * 4
num_eqs = len(bodies) * 4
for i in range(num_eqs):
    var.append(0)


def diff_eqs(t, A):
    dA = [0.0] * num_eqs
    for i in range(0, num_eqs, 4):
        totalx = 0  # sum of force in x direction
        totaly = 0  # sum of force in y direction
        dA[i] = bodies[int(i/4)].velocity[0]  # x component position differential
        dA[i + 1] = bodies[int(i/4)].velocity[1]  # y component position differential
        for j in range(0, num_eqs, 4):
            if j == i:
                continue  # object doesn't apply force to itself
            r = math.sqrt(math.pow(bodies[int(i/4)].pos[0] - bodies[int(j/4)].pos[0], 2) + math.pow(
                bodies[int(i/4)].pos[1] - bodies[int(j/4)].pos[1], 2))  # distance between bodies
            force = (G * bodies[int(i/4)].mass * bodies[int(j/4)].mass) / pow(r, 2)  # force of gravity between two bodies
            xvec = bodies[int(j/4)].pos[0] - bodies[int(i/4)].pos[0]  # x component of vector pointing from body 1 to body 2
            yvec = bodies[int(j/4)].pos[1] - bodies[int(i/4)].pos[1]  # y component of vector pointing from body 1 to body 2
            xvec = xvec / r  # convert to unit vector
            yvec = yvec / r  # convert to unit vector
            totalx = totalx + (xvec * force)  # force in x direction
            totaly = totaly + (yvec * force)  # force in y direction
        dA[i + 2] = totalx/bodies[int(i/4)].mass
        dA[i + 3] = totaly/bodies[int(i/4)].mass
    return dA

integrator = Integrator(num_eqs, dt, diff_eqs)

for i in range(0, len(bodies) * 4, 4):                                                   
    var[i] = bodies[int(i / 4)].pos[0]         
    var[i + 1] = bodies[int(i / 4)].pos[1]     
    var[i + 2] = bodies[int(i / 4)].velocity[0]
    var[i + 3] = bodies[int(i / 4)].velocity[1]
    

#----------------------------------Graphics-----------------------------------
    #initialize default shapes
    # radius of sun = 6.95 * 10**8
    # radius of Earth = 6.37* 10**6
Sun = sphere(pos=(bodies[0].pos[0],bodies[0].pos[1],0), radius=3*10**10, color = color.orange)
Earth = sphere(pos=(bodies[1].pos[0],bodies[1].pos[1],0), radius=6.37*10**9, material=materials.BlueMarble, make_trail=True)
Earth.trail_object.color=color.green
Earth.trail_type = points
Earth.interval = 10
Earth.retain=1000
text(text='',align='left',pos=(-8*10**10,-8*10**10,0),color=color.green,height=1*10**10)

#------------------------------------------------------------------------------
#for i in range(len(bodies)):
#    planets.append([])
Distance = []
while time < final_time:
    var = integrator.integrateRK4(var, dt)

    for i in range(0, len(bodies) * 4, 4):
        rate(rate_ani)
        bodies[int(i/4)].pos[0] = var[i]
        bodies[int(i/4)].pos[1] = var[i+1]
        Sun.pos = (bodies[0].pos[0],bodies[0].pos[1],0)
        Earth.pos = (bodies[1].pos[0],bodies[1].pos[1],0)
        Distance.append("distance = " + str(sqrt(((bodies[0].pos[0]-bodies[1].pos[0])**2+(bodies[0].pos[1]-bodies[1].pos[1])**2))))
        bodies[int(i/4)].velocity[0] = var[i+2]
        bodies[int(i/4)].velocity[1] = var[i+3]
        #print("body " + str(int(i/4)) + " position: (" + str(bodies[int(i/4)].pos[0]) + "," + str(bodies[int(i/4)].pos[1]) + ")")
        #print("body " + str(int(i/4)) + " velocity: (" + str(bodies[int(i/4)].velocity[0]) + "," + str(bodies[int(i/4)].velocity[1]) + ")")
    #print("\n")

    time += dt


