###Created By: Donovan Carrillo
###Created Nov 30 2021
###LAST UPDATE: Dec 14 2021 2:23pm

#Theatrical Spotlight
####
#This is the main script meant to be paired with cameraAngleCalc.py found in https://drive.google.com/drive/folders/12A-Pb0FVh_bWtu6GaflLxFZRMULDlDZA?usp=sharing
#This tool when installed following Documentation steps found in Google Drive folder will
#set selected spotlight(s) to track a mesh and change the cone angle of spotlight based on distance of object from spotlight

import pymel.core as pmc
from guiMaker import guiMaker
import os
###
#THIS LINE WILL ADD THE PLUG IN TO YOUR MAYA 
               ###THIS STRING SHOULD BE THE FILE PATH WHERE YOU SAVED cameraAngelCalc
                                   ###Change this string before compile###
pmc.loadPlugin("C:\\Users\\donov\\Documents\\maya\\scripts\\cameraAngleCalc.py")


#########################################################################################
##FUNCTION DEFINING
#########################################################################################
#buffer angle and weight of the aim constraint
buffer = 0
weight = 1.0

def connectNodes(SLList):
    for light in SLList:
        #nodeName sets the name of the cameraAngleCalc node
        #and sets it equal to cameraAngleCalc + spotlight's name
        #get shape node
        shapeNode = pmc.listRelatives(light, shapes=True)
        print(shapeNode)
        nodeName = "cameraAngleCalc" + light
        print("created node: " + nodeName)
        pmc.createNode('cameraAngleCalc', n = nodeName)
        #Shape's bounding box
        pmc.connectAttr(shape+'.boundingBoxMax', nodeName + '.bbMax')
        pmc.connectAttr(shape+'.boundingBoxMin', nodeName + '.bbMin')
        #Light Buffer Angle
        pmc.setAttr(nodeName+'.lightBuffer', buffer)
        #Light and Shape translates
        pmc.connectAttr(light+'.t', nodeName+'.lightTranslate')
        pmc.connectAttr(shape+'.t', nodeName+'.objectTranslate')
        #connect cone angle to spotlight
        pmc.connectAttr(nodeName+'.coneAngle', shapeNode[0]+'.coneAngle')
        
    
    
def runGUI(gui, *args, **kwargs):
    data = gui.CurrentValues()
    #pmc.cylinder(hr = data["Height"], n = data["Name Of Cylinder"], r = data["Radius"])
    buffer = data['Radius Buffer']
    weight = data['Target Weight']
    

def myWindow():
    myWindow = guiMaker("mainWindow", "Theatrical Spotlight")
    myWindow.createLayout("tab","Epic")

    myWindow.createControl("intField","Radius Buffer",controlLabel="Radius Buffer", p = "Default",bgc = (.2,.2,.2))
    myWindow.createControl("floatField", "Target Weight", controlLabel = "Weight", p = "Default",bgc = (.21,.21,.21))
    myWindow.createControl("button", "Create", controlLabel = "Create",p = "Default", c = runGUI(myWindow), bgc = (.2,.2,.2))
    
    runGUI(myWindow)
#############################################################################################################

####
#Main Script
#This script will control the Cone Angle of a Spotlight and creates an Aim Constraint aiming at a selected shape


#run GUI for users
myWindow()

print("buffer: "+str(buffer))
print("weight: "+str(weight))


#####These lists will sort through all selected objects and organize them
selectedList = pmc.ls(sl=True)
SLList = []
shape = ''
rejectList = []

######################
###sorting throuigh selectedList using the children to discover objectType
#######
for i in selectedList:
    print(i)
    #Shapes
    if cmds.objectType(pmc.listRelatives(i, c=True)) == 'mesh':
        shape = i
    #Spotlights
    elif cmds.objectType(pmc.listRelatives(i, c=True)) == 'spotLight':
        print('this a spotlight lol')
        SLList.append(i)
    #any other light shape or object
    else:
        rejectList.append(i)
     
#####Prints Organized Lists   
print('Selected Shape')
print(shape)
print('Selected Spotlights')
print(SLList)
print('Other Selected Objects')
print(rejectList)

####Deselect objects in rejectList
for i in rejectList:
    pmc.select(i,d = True)

######################################
"""
Here we have two lists and a Shape, Spotlights, and extra selected objects
We have sorted into these lists and deselcted all extra objects
We will now focus an aim constraint on the object and assign weight from the ui earlier
"""
###Get an array of arrays of bounding boxes of all the shapes
for light in SLList:
    print("aiming "+light+" at "+ shape)
    pmc.aimConstraint(shape, light, w = weight, aim = [0, 0 , -1])


###Plug in nodes
connectNodes(SLList)
    

