#Donovan Carrillo Midterm
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

#functions
#create circle (use HW 5)
#class


###took this class from HW 5
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
        
        
def constrainObj(createdCircle, selectedObject):
    ###take selected Object
    
    ###constrain created circle from above to object with parent constraint
    cmds.parentConstraint("createdCircle", "selectedObject")


def animCurve():
    ###take selected object
    
    ###animate along curve for every object
    cmds.pathAnimation()
    
    ###xform object to not location for every interval of frames


def pointCurve(pnt = [], crv = None):
    point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(OpenMaya.MSelectionList().getDagPath(crv))
    paramUtill=OpenMaya.MScriptUtil()
    paramPtr=paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point)
    if isOnCurve == True:



        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    else :
        point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )



    param = paramUtill.getDouble(paramPtr)
    return param


def posOnCurve(curv = None, shape = None):
    cvPos = cmds.pointPosition(cv, w = True)
    nameLoc = (curv+ 'loc')
    an = cmds.spaceLocator(n = nameLoc)
    cmds.move(cvPois[0], cvPos[1]. cvPos[2], [an[0]])
    uPos = distance.returnClosestUPosition(an[0], shape)
    mc.move(uPos[0],uPos[1],[actualName[0]])
    return an[0] 


###ACTUAL PROGRAM
##select  curve then shape to run program
sel = cmds.ls(sl=1)
print(sel)
shape = sel[1]
curv = sel[0]
print(shape)
print(curv)

print(posOnCurve(curv, shape)
#print(pointCurve(cmds.xform(shape, q= True, ws = True, t = 1), curv))
print(OpenMaya.MFnNurbsCurve.cvPositions())


#knots = len(cmds.getAttr(curv+''))
#cmds.select(curv+".cv[0]")




