import simulation_methods
import visualization_methods
import random
# https://en.wikipedia.org/wiki/Verlet_integration#Velocity_Verlet


dt = 0.0005
currentTime=0
endTime = 0.4
N =20 # N is the number of stars

# give stars initial positions and velocities
positions = []
velocities = []
masses =[]
for i in xrange(0,N):
    positions.append([random.random(), random.random(), 0.0])
    velocities.append([random.random(), random.random(), 0.0])
    masses.append(random.random() / 10.0 )

#initialialize the DB
simulation_methods.initializeDatabase()

# calculate initial force/acceleration on each star
accelerations = simulation_methods.updateAccelerations(positions, masses)
#positions = methods1.updatePositions(positions, velocities, accelerations, dt)
#print positions

# start calculation loop:
print "Starting simulation"
while currentTime < endTime:
    currentTime += dt
    #calculate the new position based on the current x,v,a
    positions = simulation_methods.updatePositions(positions, velocities, accelerations, dt)
    #calculate the new acceleration based on the new position
    oldAccelerations = list(accelerations)
    accelerations = simulation_methods.updateAccelerations(positions, masses)
    #calculate the new velocity based on the current v , current a, and new a
    velocities = simulation_methods.updateVelocities(velocities, accelerations, oldAccelerations, dt)
    #write positions to file / db
    simulation_methods.writeStatus(positions, masses, currentTime)

print "simulation complete"
    
visualization_methods.visualize()
    
    
