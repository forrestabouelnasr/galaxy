import math
def projection(star, camera, eye=[0,0,1], orientation=[0,0,0]):
    Bx = (eye[2]/Dz(star, camera, orientation))*(Dx(star, camera, orientation)-eye[0])
    By = (eye[2]/Dz(star, camera, orientation))*(Dy(star, camera, orientation)-eye[1])
    return [Bx,By]
    
def Dx(a, c, theta=[0,0,0]):
    return (math.cos(theta[1])*((math.sin(theta[1])*(a[1]-c[1]))+(math.cos(theta[2])*(a[0]-c[0]))))-(math.sin(theta[1])*(a[2]-c[2]))

def Dy(a, c, theta=[0,0,0]):
    return (math.sin(theta[0])*((math.cos(theta[1])*(a[2]-c[2]))+(math.sin(theta[1])*((math.sin(theta[2])*(a[1]-c[1]))+((math.cos(theta[2])*(a[0]-c[0])))))))+(math.cos(theta[0])*((math.cos(theta[2])*(a[1]-c[1]))-(math.sin(theta[2])*(a[0]-c[0]))))

def Dz(a, c, theta=[0,0,0]):
    return (math.cos(theta[0])*((math.cos(theta[1])*(a[2]-c[2]))+(math.sin(theta[1])*((math.sin(theta[2])*(a[1]-c[1]))+((math.cos(theta[2])*(a[0]-c[0])))))))-(math.sin(theta[0])*((math.cos(theta[2])*(a[1]-c[1]))-(math.sin(theta[2])*(a[0]-c[0]))))



