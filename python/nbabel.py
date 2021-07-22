# Mentor: Matti Picus
# Reference: http://initialconditions.org/codes/12

"""
Improvements that can be made:

    1. Many of the places the author has used v**2 for squaring, instead we can use any NumPy functions like np.square(), np.pow(), np.multiply()
    2. Some places np.sum is used but in some places sum() is used, it should be generalized
    3. Oops! I was wrong - Author should use if-else condition while passing sys.argv[1]  
    4. Conversion of python2 to python3
    5. Why to load data in main function? Class should be created for loading data! It should be generalized. 
"""

from __future__ import with_statement             # used to add functionality to current module of python
import sys
import numpy as np
from itertools import combinations

# defining single particles
class particle(object):
    """
    A particle has mass, position, velocity and acceleration.
    """
    def __init__(self, mass, x, y, z, vx, vy, vz):
        self.mass = mass
        self.position = np.array([x, y, z])
        self.velocity = np.array([vx, vy, vz])
        self.acceleration = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])          # Force due to: 1. Gravitation 2. Mutual Attraction

    # https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
    # kinetic_energy = 0.5 * self.mass * np.sum(v**2 for v in self.velocity)
    # def getx(self):
    #     return self._kinetic_energy
    # kinetic_energy = property(getx)
    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * np.sum(v**2 for v in self.velocity)

# For cluster of particles
class Cluster(list):
    """
    A cluster is just a list of particles with methods to accelerate and advance them.
    """
    # Total kinetic energy
    @property
    def kinetic_energy(self):
        return sum(particle.kinetic_energy for particle in self)

    # Total energy
    @property
    def energy(self):
        return self.kinetic_energy + self.potential_energy

    # Confusion -- Solved
    # 1. Acceleration due to gravity
    # 2. Position of particle 
    # 3. Acceleration due to mutual attraction
    # 4. Velocity 
    def step(self, dt):
        self.__accelerate()
        self.__advance_positions(dt)
        self.__accelerate()
        self.__advance_velocities(dt)

    def __accelerate(self):
        # Confusion -- Solved
        # particle's individual acceleration
        for particle in self:
            particle.acceleration[1] = particle.acceleration[0]
            particle.acceleration[0] = 0.0
            self.potential_energy = 0.0

        # Acceleration due to mutual atraction
        for p1, p2 in combinations(self, 2):
            vector = np.subtract(p1.position, p2.position)
            distance = np.sqrt(np.sum(vector**2))
            p1.acceleration[0] = p1.acceleration[0] - (p2.mass/distance**3) * vector
            p2.acceleration[0] = p2.acceleration[0] + (p1.mass/distance**3) * vector
            self.potential_energy -= (p1.mass * p2.mass)/distance

    # r(i+1)th position, r(i)th position is given
    def __advance_positions(self, dt):
        for p in self:
            p.position = p.position + p.velocity * dt + 0.5 * dt**2 * p.acceleration[0]

    # v(i+1)th velocity, v(i)th velocity is given
    def __advance_velocities(self, dt):
        for p in self:
            p.velocity = p.velocity + 0.5 * (p.acceleration[0] + p.acceleration[1]) + dt

if __name__ == "__main__":
    tend, dt = 10.0, 0.001   # end time, timestep

    # Extracted using: tar -xvf filename
    # Giving path
    file = "/mnt/c/khush/Downloads/input16.txt"

    # calling object
    cluster = Cluster()

    # https://docs.python.org/3/library/sys.html
    # https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script#:~:text=For%20every%20invocation%20of%20Python,represent%20the%20command%20line%20arguments.
    # https://www.tenforums.com/tutorials/127857-access-wsl-linux-files-windows-10-a.html
    with open("input16.txt") as input_file:
        for line in input_file:
            try:
                # After spliting & leaving index 0: 0.0625, 0.214835865608654947,  -0.120469325327368135,  -0.2661811268232539, 0.757849421156586822,  0.157644506165220161,  -0.0715602005208729741
                # Converting to float & appending particle's info, i.e. initializing with their energy and other details 
                cluster.append(
                        particle(*[float(x) for x in line.split()[1:]])
                )
            except:
                pass

    old_energy = -0.25
    # https://stackoverflow.com/questions/17192158/nameerror-global-name-xrange-is-not-defined-in-python-3 
    # XD, Replaced xrange to range coz python 3 don't support xrange (it was depretiated)
    for step in range(1, int(tend/dt+1)):
        cluster.step(dt)
        if not step % 10:
            print("t = %.2f, E = % .10f, dE/E = % .10f" % ( 
                    dt * step, cluster.energy, (cluster.energy-old_energy)
                                                /old_energy
            ))
            old_energy = cluster.energy

    print("Final dE/E = %.6e" % ((cluster.energy+0.25)/-0.25))

