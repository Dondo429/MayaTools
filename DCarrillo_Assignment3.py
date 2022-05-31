########################################
#Donovan Carrillo############
########################################
###1 A good tool is a tool that is simply intuitive and works for the user without
#having to rack their brains to understand the tool
###2
#understanding the problem that the user has
#finding as many paths to dynamically get to user's wanted end result
#build tool
#see if tool solves all problems presented
#repeat
###3
#documentation is for the user, while comments are for programmers and editors to a tool
#documenting what the tool does describes its powers and abilities in a handout form
###4
#maya.cmds help page on autodesk.com
###5
#in the script editor top screen
#it lists what commands were preformed
###6
#os

###7
import maya.cmds as cmd
import math

#printing for whitespace
print('')
print('')


def listNodes():
    #i is an iterator
    i = 1
    #nodesList will store final nodes
    nodesList = []
    while i < 5:
        cmd.createNode('transform', n='TrNode'+str(i))
        i += 1
    #i wasn't sure how to select transformNodes without selecting all transforms
    #so i select the first four elements in the nodes
    #:)
    nodes = cmds.ls(type = 'transform')
    n = 0
    while n <= 3:
        nodesList.append(nodes[n])
        n += 1
    return nodesList
 
n = listNodes()   
print(n)

###8

def selectitems():
    ###use cmds.ls() in three modes
    ###selecting mesh, old node, and nurb
    cmd.polyCube(n = 'geometryCube')
    cmd.nurbsCube(n = 'nurbCube')
    
    modesList = []
    cmd.ls('transform')
    modesList.append(cmd.ls('transform'))
    modesList.append(cmd.ls(geometry = True))
    modesList.append(cmd.ls(type = 'nurbsCurve'))
    return modesList

m = selectitems()
print(m)


###9
def printFunctions(n, m):
    print(n)
    print('')
    print(m)
    
print('')
print('Should return same results as earlier')
print('')
printFunctions(n,m)  


###10  
###couldn't set keyframes before I had to turn in assignment
###function moves previously created object named geometryCube
###.1 on the x per unit time i and keyframes

def moveBallLol(n):
    cmds.select('geometryCube')
    i = 1
    while i < 25:
        cmd.xform(r = true , t=(.1,0,0)
        ###This line is giving me trouble :(
        
        cmd.setKeyframe(t = (str(i)+'sec'))
        i += 1
    
    
    
    
    
    