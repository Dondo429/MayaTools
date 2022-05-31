import pymel.core as pmc

from guiMaker import guiMaker


####
#Donovan Carrillo
#Weekend HW 7


###Not sure how to run makeCyl using Button

def makeCyl(cylWindow, *args, **kwargs):
    data = cylWindow.CurrentValues()
    pmc.cylinder(hr = data["Height"], n = data["Name Of Cylinder"], r = data["Radius"])
    

def cylWindow():
    cylWindow = guiMaker("mainWindow", "Cylinder Maker")
    cylWindow.createLayout("tab","Epic")
    cylWindow.createControl("textField","Name Of Cylinder", controlLabel = "Name", p = "Default",bgc = (.2,.2,.2))
    cylWindow.createControl("intField","Radius",controlLabel="Radius", p = "Default",bgc = (.3,.32,.32))
    cylWindow.createControl("floatField", "Height", controlLabel = "Height", p = "Default",bgc = (.21,.21,.21))
    cylWindow.createControl("radioButtons", controlName= "Caps", controlLabel = "Caps", p = "Default", radioList={"True":"Caps: Yes","False":"Caps: No"})
    cylWindow.createControl("button", "Create", controlLabel = "Create",p = "Default", c = makeCyl(cylWindow), bgc = (.2,.2,.2))
    
    makeCyl(cylWindow)
    
    
    
    
cylWindow()
