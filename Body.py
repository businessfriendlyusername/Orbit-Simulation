import math

class Body:
    def __init__(self, velocity, radius, mass, orbits=0, pos=0):
    	self.mass = mass
    	if orbits == 0:
	        # calculate the tangential velocity vector <x,y> based on the velocity (velocity) and the angle (pos)
	        self.velocity = [math.sin(math.radians(pos)) * velocity, math.cos(math.radians(pos)) * velocity]
	        # calculate position <x,y> based on the radius(radius) from the center of the system and the angle(pos)
	        self.pos = [math.cos(math.radians(pos)) * radius, math.sin(math.radians(pos)) * radius]
        else:
        	# calculate the tangential velocity vector <x,y> based on the velocity (velocity) and the angle (pos)
	        self.velocity = [(math.sin(math.radians(pos)) * velocity) + orbits.velocity[0], (math.cos(math.radians(pos)) * velocity) + orbits.velocity[1]]
	        # calculate position <x,y> based on the radius(radius) from the center of the system and the angle(pos)
	        self.pos = [(math.cos(math.radians(pos)) * radius) + orbits.pos[0], (math.sin(math.radians(pos)) * radius) + orbits.pos[1]]
