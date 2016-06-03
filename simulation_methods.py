def updateAccelerations(positions, masses):
    N = len(positions)
    G = 0.1
    forces = [[0.0, 0.0, 0.0] for _ in xrange(N)]
    for i in xrange(0,N-1):
        firstObjectPosition = positions[i]
        for j in xrange(i+1,N):
            secondObjectPosition = positions[j]
            positionVector = [
                secondObjectPosition[0] - firstObjectPosition[0],
                secondObjectPosition[1] - firstObjectPosition[1],
                secondObjectPosition[2] - firstObjectPosition[2]
            ]
            distanceSquared = (
                positionVector[0]**2 +
                positionVector[1]**2 +
                positionVector[2]**2 )
            distanceSquared = max(distanceSquared, 0.0003)
            distance = distanceSquared ** 0.5
            forceMagnitude = masses[i] * masses[j] * G / distanceSquared
            forces[i][0] += forceMagnitude * positionVector[0] / distanceSquared
            forces[i][1] += forceMagnitude * positionVector[1] / distanceSquared
            forces[i][2] += forceMagnitude * positionVector[2] / distanceSquared
            forces[j][0] -= forceMagnitude * positionVector[0] / distanceSquared
            forces[j][1] -= forceMagnitude * positionVector[1] / distanceSquared
            forces[j][2] -= forceMagnitude * positionVector[2] / distanceSquared
    
    accelerations = [[0.0, 0.0, 0.0] for _ in xrange(N)]
    for i in xrange(0,N):
        accelerations[i][0] = forces[i][0] / masses[i]
        accelerations[i][1] = forces[i][1] / masses[i]
        accelerations[i][2] = forces[i][2] / masses[i]
    return accelerations

def updatePositions(positions, velocities, accelerations, dt):
    N = len(positions)
    for i in xrange(0,N):
        positions[i][0] += velocities[i][0] * dt + 0.5*accelerations[i][0]*dt*dt
        positions[i][1] += velocities[i][1] * dt + 0.5*accelerations[i][1]*dt*dt
        positions[i][2] += velocities[i][2] * dt + 0.5*accelerations[i][2]*dt*dt
    return positions

def updateVelocities(velocities, accelerations, oldAccelerations, dt):
    N = len (velocities)
    for i in xrange(0,N):
        velocities[i][0] += 0.5 * (accelerations[i][0] + oldAccelerations[i][0]) * dt
        velocities[i][1] += 0.5 * (accelerations[i][1] + oldAccelerations[i][1]) * dt
        velocities[i][2] += 0.5 * (accelerations[i][2] + oldAccelerations[i][2]) * dt
    return velocities

def calculateForces_prototype(positions, masses):
    #first, split the volume into 64 cells; classify each star into a cell
    #second, calculate aggregate properties for each cell, i.e. center-of-mass, total mass
    #third, for each star, calculate forces with
    #   (a) all stars in the same cell
    #   (b) all the stars in neighboring cells ?
    #   (c) the aggregates of the non-neighboring cells
    cellBoundaries = calculateCellBoundaries(positions)
    
    
    
    
def calculateCellBoundaries(positions):
    pass





