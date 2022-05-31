### Donovan Carrillo

import maya.cmds as cmds

class circleControl:
    name = "circle"
    radius = 1
    #confused on what kind of object position should be
    
    def __init__():
        self.name = "circle"
        self.radius = 1
        cmds.circle(n = "circle", r = 1, c=[0,0,0])
    
    #create circle constructor
    def __init__(self, name, radius, px, py, pz):
        name = self.name
        radius = self.radius
        cmds.circle(n = name, r = radius, c=[px,py,pz])
    
    #moves circle
    ###NOT RELATIVE TO WORLD###
    def moveCircle(self, px, py, pz):
        cmds.xform(self.name, ws=False, t=[px,py,pz])
    
    #Scales circle
    #then freezes scale transformations
    def changeRadius(self, r):
        cmds.scale(r, r, r)
        cmds.makeIdentity(apply = True, s = 1)
        
        
c = circleControl("circle", 2, 0, 0, 0)
c.moveCircle(1, 1, 1)
c.changeRadius(2)        