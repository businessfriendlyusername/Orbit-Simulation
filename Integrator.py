# COMP155 Computer Simulation                       
#
# Integrator class
#   Implements various differential equation integration techniques.
#   Forward Euler
#   Runge-Kutta 2nd order
#   Runge-Kutta 3rd order
#
# constructor:
# Integrator(num_eqs, dt, diff_eqs)
#    num_eqs: number of diff eqs
#    dt: time delta for integration steps
#    diff_eqs: a function that implements the diff eqs
#       function must have signature diff_eqs(t, x) -> dx
#       where t is time, x is a vector of current values
#       and dx is the vector x'(t,x)
#
# methods:
#   integrateEuler(x, dt) -> x
#   integrateRK2(x, dt) -> x
#   integrateRK4(x, dt) -> x
#     Each of these methods implements an integration method using
#     the supplied diff eqs.
#     input x: vector x(t)
#     input dt: time step
#     returns: vector x(t+dt)

class Integrator:

    def __init__(self, num_eqs, dt, diff_eqs):
        self.num_eqs = num_eqs
        self.dt = dt
        self.diff_eqs = diff_eqs
        
    # add two vectors
    def addV(self, v1, v2):
        x = [0.0]*self.num_eqs
        for i in range(self.num_eqs):
            x[i] = v1[i] + v2[i]
        return x

    # multiply vector v by scalar s
    def mulSV(self, s, v):    
        x = [0.0]*self.num_eqs
        for i in range(self.num_eqs):
            x[i] = s * v[i]
        return x

    # Euler integration
    def integrateEuler(self, x, t):
        # x(t+dt) = x(t) + f'(t,x)*dt
        dt = self.dt
        x = self.addV(x, self.mulSV(dt, self.diff_eqs(t,x)))
        return x

    # 2nd order Runka-Kutta integration
    def integrateRK2(self, x, t):
        # k1 = dt*f'(tn,xn)
        # k2 = dt*f'(tn+dt/2,xn+k1/2)
        # x = xn + k2
        dt = self.dt
        k1 = self.mulSV(dt, self.diff_eqs(t, x))
        k2 = self.mulSV(dt, self.diff_eqs(t+dt/2.0, self.addV(x, self.mulSV(0.5, k1))))
        x = self.addV(x, k2)
        return x

    # 4th order Runka-Kutta integration
    def integrateRK4(self, x, t):
        # k1 = dt*f'(tn,xn)
        # k2 = dt*f'(tn+dt/2,xn+k1/2)
        # k3 = dt*f'(tn+dt/2,xn+k2/2)
        # k4 = dt*f'(tn+dt,xn+k3)
        # x = xn + k1/6 + k2/3 + k3/3 + k4/6
        dt = self.dt
        k1 = self.mulSV(dt, self.diff_eqs(t, x))
        k2 = self.mulSV(dt, self.diff_eqs(t+dt/2.0, self.addV(x, self.mulSV(0.5, k1))))
        k3 = self.mulSV(dt, self.diff_eqs(t+dt/2.0, self.addV(x, self.mulSV(0.5, k2))))
        k4 = self.mulSV(dt, self.diff_eqs(t+dt, self.addV(x, k3)))
        x = self.addV(x, self.mulSV(1.0/6.0, k1))
        x = self.addV(x, self.mulSV(1.0/3.0, k2))
        x = self.addV(x, self.mulSV(1.0/3.0, k3))
        x = self.addV(x, self.mulSV(1.0/6.0, k4))
        return x
