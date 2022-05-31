#Donovan Carrillo
#Assignment 2
#Date Modified 9/22/2021 7:16pm
#Creates a Rudimentary Car in maya 
#file based off of file presented in class

import maya.cmds as cmd

###Body(name, size) creates a basic car shape 
def Body(name,size):
    body = cmd.polyCube(name=name,depth = size[2],width=size[0],height=size[1],subdivisionsDepth = 6)[0]
    return body
    
###Wheels(bodyObj, wheelSize,carSize) creates wheels at the corners of the car created in Body(name,size)    
def Wheels(bodyObj,wheelSize,carSize):
    ###create two arrays for tires and tire names
    tires = []
    tireList = ["frontRight","frontLeft","rearRight","rearLeft"]
    
    #find x coordinates, both can be used for left and right wheels
    ###use var cmds from script in class
    rightSideX = cmd.getAttr(bodyObj+".bbnx") # carSize[0]/2
    leftSideX = cmd.getAttr(bodyObj+".bbxx")# -carSize[0]/2
    #find z coordinates, can be used on both front and back
    ###Dont need y, y is up###
    ##gets attribute of x and z coordinates / 3 so the wheels aren't on the corners but inside the car chassis a little bit
    frontZ = cmd.getAttr(bodyObj+".bbxz") - cmd.getAttr(bodyObj+".bbxz")/3 # carSize[2]/2  - carSize[2]/6
    rearZ = cmd.getAttr(bodyObj+".bbnz") - cmd.getAttr(bodyObj+".bbnz")/3 # - carSize[2]/2  + carSize[2]/6
    axisY = cmd.getAttr(bodyObj+".bbny")
    #print the position of tire selected spots
    print(rightSideX,leftSideX,frontZ,rearZ,axisY)
    tirePos = [(rightSideX,axisY,frontZ),(leftSideX,axisY,frontZ),(rightSideX,axisY,rearZ),(leftSideX,axisY,rearZ)]
    n = 0
    
    #create tires out of Cylinder basic mesh
    #take radius/height from wheelSize obj
    for tire in tireList:
        currentWheel = cmd.polyCylinder(name =(bodyObj+"_"+ tire),axis = (1,0,0),radius = wheelSize[0],height=wheelSize[1])[0]
        cmd.xform(currentWheel,t=tirePos[n])
        #take created list and add it to currentWheel List
        tires.append(currentWheel)
        n = n + 1
    return tires     

###take all objects ceated as values
###parent each to the next and group them in the outliner
def carOrg(name,bodyGeo,wheelGeo):
    mainGroup = cmd.group(name=name+"_grp",em=1)
    geoGroup =cmd.group(name=name+"_Geo_grp",em=1)
    rigGroup = cmd.group(name=name+"_Rig_grp",em=1)
    ctrlGroup =cmd.group(name=name+"_Ctrl_grp",em=1)
    cmd.parent([geoGroup,rigGroup,ctrlGroup],mainGroup)
    cmd.parent(bodyGeo,geoGroup)
    cmd.parent(wheelGeo,bodyGeo)
    return [mainGroup,geoGroup,rigGroup,ctrlGroup]
    

def rigCar(carName,carBody,wheels,carGroups):
    pass

        

###main function
def carAssembly():
    dimensions = (4,3,6)
    tireSize = (.5,1)
    ###Stinky Car didn't work due to space in name
    ###no white spaces
    carName = "StinkyCar"
    count = 0
    newCarName = carName
    while cmd.objExists(newCarName+"_grp"):
        newCarName = carName+str(count)
        count +=1 
    carBody = Body(newCarName,dimensions)
    wheels = Wheels(newCarName,tireSize,dimensions)
    carGroups = carOrg(newCarName,carBody,wheels)
    print(carGroups) 

    

if __name__ == "__main__":
    carAssembly()
        