import math

class Body:
    def __init__(self, velocity, radius, mass, pos=0):
        # calculate the tangential velocity vector <x,y> based on the velocity (velocity) and the angle (pos)
        self.velocity = [math.sin(math.radians(pos)) * velocity, math.cos(math.radians(pos)) * velocity]
        # calculate position <x,y> based on the radius(radius) from the center of the system and the angle(pos)
        self.pos = [math.cos(math.radians(pos)) * radius, math.sin(math.radians(pos)) * radius]
        self.mass = mass
        self.radius = radius
