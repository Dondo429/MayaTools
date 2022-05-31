###Donovan Carrillo
###Date Modified: 9/14/2021
###Creates three shapes, add shapes to a list, move objects up 5 units, loop all back to 0

##CHANGES

##BUGS


###MAIN###
import maya.cmds as cmd
cube = 'Epic_Cube'
pyr = 'Pog_Pyramid'
tor = 'Tubular_Torus'

#cube
cmd.polyCube(n = cube, ax = [1, 1, 1])


#pyramid
cmd.polyPyramid(n = pyr, ax =[1,0,2],sh = 2, nsi=5, w=3)


#donut
cmd.polyTorus(n = tor)

cmd.select(ado=True)

###use LS to add to list
shapesList = cmd.ls(geometry = True)
###print list created using LS commands
print(shapesList)

###xform the list 
for x in shapesList:
    print('xform move up shape: ' + x)
    cmd.xform(r=True, t=(0,5,0))
 

###setAttr to move objects back to origin 
for x in shapesList:
    print('setAttr shape to origin: '+ x)
    shape = cmd.listRelatives(x, p = 1)[0]
    cmd.setAttr(shape+".translateY", 0)
    
###
#The easiest way to move things was xform in my opinion
#another way to move things is using cmd.move()

