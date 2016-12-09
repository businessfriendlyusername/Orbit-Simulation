# Orbit of the Moon and the Earth Simulation
# simulation.py
# Jared Vu and Stephen Blevins
#
# --------------------------------------------------------
from visual import *
from Body import *
from Integrator import *
from visual.graph import *
import math

scene = display(title='Orbit Sim', width = 1000, height=1000, center=(0,0,0))
G = 6.66308 * math.pow(10, -11)
bodies = []

#Time Variables that can be changed
time = 0
dt = 86400 / 100
years = 1
final_time = 86400 * 365 * years 
rate_ani = 10000

#Append Bodies to be used in Sim
bodies.append(Body(0, 0, 1.98855*math.pow(10,30))) # sun
bodies.append(Body(29800, 149600000000, 5.972*math.pow(10,24), bodies[0], 180)) # earth
bodies.append(Body(1000, 384400000, 7.347*math.pow(10,22), bodies[1])) # poon

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
Moon = sphere(pos=(bodies[2].pos[0],bodies[2].pos[1],0), radius=1*10**9, make_trail=True)
Moon.trail_object.color=color.white
Moon.trail_type=points
Moon.interval=10
Moon.retain=500

#------------------------------------------------------------------------------

ES_Distance = []
ME_Distance = []
while time < final_time:
    var = integrator.integrateRK4(var, dt)

    for i in range(0, len(bodies) * 4, 4):
        rate(rate_ani)
        bodies[int(i/4)].pos[0] = var[i]
        bodies[int(i/4)].pos[1] = var[i+1]
        #Moon Distance scaling-----------------------
        scale = 50
        scaleX = scale*(bodies[1].pos[0]-bodies[2].pos[0])
        scaleY = scale*(bodies[1].pos[1]-bodies[2].pos[1])
        #Drawing-------------------------------------
        Sun.pos = (bodies[0].pos[0],bodies[0].pos[1],0)
        Earth.pos = (bodies[1].pos[0],bodies[1].pos[1],0)
        Moon.pos = (bodies[2].pos[0]+scaleX,bodies[2].pos[1]+scaleY,0)
        #Record Distance-----------------------------
        ES_Distance.append(sqrt(((bodies[0].pos[0]-bodies[1].pos[0])**2+(bodies[0].pos[1]-bodies[1].pos[1])**2)))
        ME_Distance.append(sqrt(((bodies[1].pos[0]-bodies[2].pos[0])**2+(bodies[1].pos[1]-bodies[2].pos[1])**2)))
        #Update Velocity-----------------------------
        bodies[int(i/4)].velocity[0] = var[i+2]
        bodies[int(i/4)].velocity[1] = var[i+3]
        

    time += dt

#--------------------------------Graphing------------------------------------
gdisplay(title='Distance between Earth and Sun',xtitle='Time',ytitle='Distance(KM)',background=color.white, foreground=color.black)
f1 = gcurve(color=color.cyan)
gdisplay(title='Distance between Moon and Earth',xtitle='Time',ytitle='Distance(KM)',background=color.white, foreground=color.black)
f2 = gcurve(color=color.red)

for x in range(len(ES_Distance)):
    f1.plot(pos=(x,ES_Distance[x]))


for x in range(len(ME_Distance)):
    f2.plot(pos=(x,ME_Distance[x]))


