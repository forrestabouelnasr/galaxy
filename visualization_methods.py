import database_methods
import numpy as np
from images2gif import writeGif
from PIL import Image
import os
import time as timeModule
import Projection
import random
import math

def visualize():
    print "starting visualization"
    radius=10
    image_filenames=[]
    image_list=[]
    plotsize=800
    data = np.zeros( (plotsize,plotsize,3), dtype=np.uint8)
    stationaryStars = []
    while len(stationaryStars) < 200:
        a = random.uniform(-1.0,1.0)
        b = random.uniform(-1.0,1.0)
        while a**2 + b **2 >= 1:
            a = random.uniform(-1.0,1.0)
            b = random.uniform(-1.0,1.0)
        x = 2 * a * (1 - a**2 - b**2) ** 0.5
        y = 2 * b * (1 - a**2 - b**2) ** 0.5
        z = 1 - 2*(a**2 + b**2)
        stationaryStars.append([0, 1000*x, 1000*y, 1000*z, 0.01])
    a=1000
    b = 0.000000001
    stationaryStars.append([0,b,b,b,6])
    stationaryStars.append([0,1,b,b,2])
    stationaryStars.append([0,2,b,b,2])
    stationaryStars.append([0,3,b,b,2])
    stationaryStars.append([0,4,b,b,2])
    stationaryStars.append([0,5,b,b,2])
    stationaryStars.append([0,-4,b,b,2])
    stationaryStars.append([0,-3,b,b,2])
    stationaryStars.append([0,-2,b,b,2])
    stationaryStars.append([0,-1,b,b,2])
    stationaryStars.append([0,-5,b,b,2])
    cameraDistance = 20.0
    #increasing camera[0] rotates the camera to the left
    #increasing camera[1] rotates the camera to the down
    orientation = [0,-3.14159/4,0]
    camera = [0, cameraDistance, 0]
    
    #first, gather all times from the db
    times = [x[0] for x in database_methods.database_read('''select distinct time from objects''')]
    
    counter = 0
    #at each time...
    for time in times:

        #orientationVector=[
        #    math.cos(orientation[0])*math.cos(orientation[1]),
        #    math.sin(orientation[0])*math.cos(orientation[1]),
        #    math.sin(orientation[1])
        #]
        #camera = [
        #    -orientationVector[0]*cameraDistance,
        #    -orientationVector[1]*cameraDistance,
        #    -orientationVector[2]*cameraDistance
        #]
        
        data = np.zeros( (plotsize,plotsize,3), dtype=np.uint8)
        #gather all details for each star
        stars = database_methods.database_read('''select object_id, x_position, y_position, z_position, mass
                                            from objects
                                            where time = ?''', [time])

        for star in stars:
            position = [star[1], star[2], star[3]]
            mass = star[4]
            #for each star, draw a circle
            #plotCenter = [star[1], star[2]]
            plotCenter = Projection.projection(position, [0,0.5,-0.5], [0,0,1],[3.14159/2,0,0])
            r = (star[4] ** (1.0/3.0))
            data = draw_circle([plotCenter[0]*plotsize,plotCenter[1]*plotsize],r*radius,data)
        for star in stationaryStars:
            position = [star[1], star[2], star[3]]
            #print position
            mass = star[4]
            #for each star, draw a circle
            #plotCenter = [star[1], star[2]]
            plotCenter = Projection.projection(position, camera, [0,0,1],orientation)
            #print plotCenter
            r = (star[4] ** (1.0/3.0))
            data = draw_circle([plotCenter[0]*plotsize,plotCenter[1]*plotsize],r*radius,data,[255,100,100])
        
        
        orientation[0] += 0.01

    
        
        #construct an image
        img = Image.fromarray(data, 'RGB')
        filename = 'image'+'0'*(8-len(str(counter)))+str(counter)+'.png' 
        image_filenames.append(filename)
        img.save(filename)
        counter+=1
    
    #concat images into a movie file
    #os.remove('out.mp4')
    os.system("./ffmpeg -framerate 20 -pattern_type glob -i '*.png' -c:v libx264 -pix_fmt yuv420p out" + str(int(timeModule.time())) + ".mp4")
    #remove images
    for fn in image_filenames:
        os.remove(fn)
        pass
    return




def draw_circle(center,r,data, color=[255,255,255]):
    #r is in pixels/index units
    #if the centerpoint of a given pixel is fewer than "r" pixels from the
    #centerpoint of the circle, color that pixel
    l,w,d=np.shape(data)
    r2=r*r
    x_max=1+int(center[0]+r)
    y_max=1+int(center[1]+r)
    x=int(center[0]-r)
    while x < x_max:
        if x >= 0 and x < l:
            y=int(center[1]-r)
            while y < y_max:
                if y >= 0 and y < w:
                    if float(x-center[0])**2 + float(y-center[1])**2 < r2:
                        data[x,y]=color
                y+=1
        x+=1
    return data




