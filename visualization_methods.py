import database_methods
import numpy as np
from images2gif import writeGif
from PIL import Image
import os
import time as timeModule
        
def visualize():
    print "starting visualization"
    radius=10
    image_filenames=[]
    image_list=[]
    plotsize=800
    data = np.zeros( (plotsize,plotsize,3), dtype=np.uint8)
    
    #first, gather all times from the db
    times = [x[0] for x in database_methods.database_read('''select distinct time from objects''')]
    
    counter = 0
    #at each time...
    for time in times:
        data = np.zeros( (plotsize,plotsize,3), dtype=np.uint8)
        #gather all details for each star
        stars = database_methods.database_read('''select object_id, x_position, y_position, z_position, mass
                                            from objects
                                            where time = ?''', [time])
        for star in stars:
            position = [star[1], star[2], star[3]]
            mass = star[4]
            #[center, r] = transform
            #for each star, draw a circle
            plotCenter = [star[1], star[2]]
            r = (star[4] ** (1.0/3.0))
            data = draw_circle([plotCenter[0]*plotsize,plotCenter[1]*plotsize],r*radius,data)
        
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




def draw_circle(center,r,data):
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
                        data[x,y]=[255,255,255]
                y+=1
        x+=1
    return data




