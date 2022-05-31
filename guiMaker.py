import pymel.core as pmc
from functools import partial

class guiMaker:
    def __init__(self,windowName,windowTitle):
        self._windowName = windowName
        self._windowTitle = windowTitle
        self._windowLayouts = []
        self._controls = []
        self._controlValues = {}
        self._funtion = ""
        self.createWindow()
        
    def helpMe(self,*args,**kwargs):
        pmc.launch(web="https://help.autodesk.com/view/MAYAUL/2022/ENU/?guid=__CommandsPython_index_html")
            
         
################################### Create Window ###########################         
    def createWindow(self):
        if pmc.window(self._windowName,exists=True):
            pmc.deleteUI(self._windowName)
        self._windowUI = pmc.window(self._windowName,title=self._windowTitle,mb=True,rtf=True)
        self._windowUI.show() 
################################# Create Layout for window #####################
    
    def createLayout(self,layoutType,layoutName,layoutLable = "myLayout", *args,**kwargs):
        validLayouts = ["frame","tab","rowColumn"]
        if layoutName in self._windowLayouts:
            print("Layout with that name already exsists")
            return
        if layoutType not in validLayouts:
            print("Huh? I dont know how to make that. Valid choices are \"form\",\"tab\",\"rowColumn\"")
            return
        
        #Frame Layout
        if layoutType == "frame":
            enableBackground = True
            if "bgc" not in kwargs:
                enableBackground = False
                kwargs["bgc"] = [0.35,0.35,0.35] 
            currentLayout = pmc.frameLayout(layoutName,l=layoutLable,bgc=kwargs["bgc"],p=self._windowUI,ebg=enableBackground)
            self._windowLayouts.append(layoutName)
            
        #Tab Layout and Tabs     
        if layoutType == "tab":
            enableBackground = True
            if "bgc" not in kwargs:
                enableBackground = False
                kwargs["bgc"] = [0.35,0.35,0.35]
            if "tabList" not in kwargs:
                kwargs["tabList"] = {"Default":"Main"}    
            #print(kwargs["tabList"])
            currentLayout = pmc.tabLayout(layoutName,bgc=kwargs["bgc"],p=self._windowUI,ebg=enableBackground)
            self._windowLayouts.append(layoutName)
            tabLayoutList = []
            
            for item in kwargs["tabList"].items():
                #print(item)
                currentTabLayout = pmc.rowColumnLayout(item[0],nc=1,p=currentLayout)
                tabLayoutList.append([currentTabLayout,item[1]])
            pmc.tabLayout(currentLayout, edit=True, tabLabel=tabLayoutList)    
            
            self._windowLayouts.append(layoutName)
            self._windowLayouts += kwargs["tabList"]




        #Row Column Layout
        if layoutType == "rowColumn":
            enableBackground = True
            if "bgc" not in kwargs:
                enableBackground = False
                kwargs["bgc"] = [0.35,0.35,0.35] 
            if "rc" not in kwargs:
                kwargs["rc"] = 1    
            currentLayout = pmc.rowColumnLayout(layoutName,bgc=kwargs["bgc"],nc = kwargs["rc"],p=self._windowUI)
            self._windowLayouts.append(currentLayout)
                    
            
############################# Controls############################################################################            
    def controlValueUpdate(self,controlName,*args,**kwargs):
        
        print(args)
        print(kwargs)
        self._controlValues[controlName] = args[0]
        print(self._controlValues)
        return 


    def createControl(self,controlType,controlName = "Control",controlLabel="Default", p="",*args,**kwargs):

        #User Info Check

        if "bgc" not in kwargs:
            enableBackground = False
            kwargs["bgc"] = [0.6,0.6,0.6] 
        if "command" not in kwargs:
            kwargs["command"] = "print(\"I was pressed\")"
        
        
        if (p == "") or (p not in self._windowLayouts):
            
           try:
               p=self._windowLayouts[0]
               
           except IndexError:
               #index empty or wrong number
               print("No Layouts Present.")
               return "failed"    
            
        
        validControls = ["button","checkBox","floatField","intField","textField","textLabel","radioButtons","separator","optionMenu","menu"]
        
        if  controlName in self._controls:
            print("Control with that name already exsists")
            return
            
        if controlType not in validControls:
            print("Huh? I dont know how to make that. Valid choices are \"button\",\"checkBox\",\"floatField\",\"textField\",\"intField\",\"textLabel\",\"radioButtons\",\"seperator\",\"optionMenu\",\"menu\"")
            return
 
 
 
 
        #Control Creations
            
        try:


            #--------------------------------------------------------------

            if controlType == "button":
                currentControl = pmc.button(controlName,l =controlLabel,p = p,bgc=kwargs["bgc"],c= kwargs["command"])
            
            #--------------------------------------------------------------    

            if controlType == "checkBox":
                if "val" not in kwargs:
                    kwargs["val"] = 0
                currentControl = pmc.checkBox(controlName,l =controlLabel,p = p ,bgc=kwargs["bgc"],value =kwargs["val"] ,cc = partial(self.controlValueUpdate,controlName))
                self.controlValueUpdate(controlName,False)
                self._controls.append(controlName)

            #--------------------------------------------------------------
            
            if controlType == "floatField":
                if "max" not in kwargs:
                    kwargs["max"] = 10.0
                if "min" not in kwargs:
                    kwargs["min"] = -10.0
                if "val" not in kwargs:
                    kwargs["val"] = 0.0                      
                currentControl = pmc.floatSliderGrp(controlName,l =controlLabel,p = p,f=1,bgc=kwargs["bgc"],value = kwargs["val"],min =kwargs["min"],max =kwargs["max"],cc = partial(self.controlValueUpdate,controlName))
                self.controlValueUpdate(controlName,kwargs["val"])
                self._controls.append(controlName)  
     
                    
           #--------------------------------------------------------------             
                    
            if controlType == "intField":
                if "max" not in kwargs:
                    kwargs["max"] = 10
                if "min" not in kwargs:
                    kwargs["min"] = -10
                if "val" not in kwargs:
                    kwargs["val"] = 0                     
                currentControl = pmc.intSliderGrp(controlName,l =controlLabel,p = p,f=1,bgc=kwargs["bgc"],value = kwargs["val"],min =kwargs["min"],max =kwargs["max"],cc = partial(self.controlValueUpdate,controlName))                
                self.controlValueUpdate(controlName,kwargs["val"])
                self._controls.append(controlName)  
            
           #--------------------------------------------------------------             
            if controlType == "textField":
                if "val" not in kwargs:
                    kwargs["val"] = 0  
                currentControl = pmc.textFieldGrp(controlName,l =controlLabel,p = p,bgc=kwargs["bgc"],tx = kwargs["val"],tcc = partial(self.controlValueUpdate,controlName))
                self.controlValueUpdate(controlName,kwargs["val"])
                self._controls.append(controlName)     
                                
          #--------------------------------------------------------------  
            if controlType == "textLabel":
                currentControl = pmc.text(controlName,l =controlLabel,p = p,bgc=kwargs["bgc"])
          #--------------------------------------------------------------
          
          
                          
            if controlType == "separator":
                currentControl = pmc.separator(controlName,style='in',p = p,bgc=kwargs["bgc"])

          #--------------------------------------------------------------
            if controlType == "radioButtons":
                if "radioList" not in kwargs:
                    kwargs["radioList"] = {"radio1":"On","radio1":"Off"}
                currentControl =pmc.radioCollection(controlName,p=p)
                print(currentControl)
                
                def radioUpdate(currentControl,*args,**kwargs):
                    
                    value = pmc.radioCollection(controlName,q=1,sl=1)
                    self._controlValues[controlName] = value
                       
                for item in kwargs["radioList"].items():
                    print(item)
                    currentButton = pmc.radioButton(item[0],l=item[1],bgc=kwargs["bgc"],collection = currentControl,cc=radioUpdate)
                radioUpdate(currentButton)
                self._controls.append(controlName)         
 
         #--------------------------------------------------------------
            if controlType == "optionMenu":
                if "optionList" not in kwargs:
                    kwargs["optionList"] = {"option1":"On","option2":"Off"}
                if "el" not in kwargs:
                    kwargs["el"] = ""
                currentControl = pmc.optionMenuGrp(controlName,l=controlLabel, p=p,bgc=kwargs["bgc"],el =kwargs["el"],cc= partial(self.controlValueUpdate,controlName))
                for option in kwargs["optionList"].items():
                    self.controlValueUpdate(controlName,option[1])
                    print(option) 
                    currentOption = pmc.menuItem(controlName,l=option[1])
                self._controls.append(controlName)           
                    

        #--------------------------------------------------------------
            if controlType == "menu":
                if "menuList" not in kwargs:
                    kwargs["menuList"] = {"menuOption":("Help",self.helpMe)}
                pmc.window(self._windowName,e=1,mbv=1)
                currentControl = pmc.menu(controlName,l=controlLabel,p=self._windowName)
                for option in kwargs["menuList"].items():
                    currentMenuItem = pmc.menuItem(option[0],l=option[1][0],c=option[1][1])

        #They broke it.
        
        
        except RuntimeError:
            print("RunTime Error: Not a valid layout or Control Flags")
            return
    def CurrentValues(self):
        print(self._controlValues)
        return self._controlValues

            
    
                        
                    
            
                  

         
####################TEST ZONE################################
def myScript(*args,**kwargs):
    print("Hello I am awesome today, I got up, I went to class, I learned things")


def test():
    myWindow = guiMaker("mainWindow","My Nifty Window")
    myWindow.createControl("checkBox",controlName ="bob",controlLabel="Uncheck",command=myScript,p="charles")
    myWindow.createLayout("hello","cat",layoutLable= "Hello",rows=1,cats=5)
    myWindow.createLayout("frame","myFrame",layoutLable="test",bgc = [250,10,0])
    myWindow.createLayout("frame","myFrame2")
    myWindow.createLayout("tab","myTabs",tabList={"tabOne":"Tab One","tabTwo":"Tab Two"})
    myWindow.createLayout("tab","myTabs2")
    myWindow.createLayout("rowColumn","simpleRows")
    myWindow.createLayout("rowColumn","Rows",rc=3)
    myWindow.createControl("button",controlName ="button1",controlLabel="Press me",p ="tabOne")
    myWindow.createControl("button",controlName ="button2",controlLabel="Press me Now",p ="tabOne",command=myScript)
    myWindow.createControl("checkBox",controlName ="checkbox1",controlLabel="Uncheck",command=myScript)
    myWindow.createControl("floatField",controlName ="floatField",controlLabel="Float",p="tabTwo")
    myWindow.createControl("intField",controlName ="intField",controlLabel="Int",p="tabTwo")
    myWindow.createControl("textField",controlName ="textField",controlLabel="Text",val="Default",p="tabTwo")
    myWindow.createControl("textLabel",controlName ="textField",controlLabel="Do this thing",p="myFrame")
    myWindow.createControl("separator",controlName= "break",p="myFrame2")
    myWindow.createControl("radioButtons",controlName= "Radios",p="myFrame2",radioList={"Option1":"Continue","Option2":"Help"})
    myWindow.createControl("optionMenu",controlName = "options", controlLabel = "options",p="tabOne")
    myWindow.createControl("menu",controlName = "MainMenu", controlLabel = "Main Menu")
    def selcted(*args,**kwargs):
        print("I was selected")  
    myWindow.createControl("menu",controlName = "SelectMenu", controlLabel = "Select Menu",menuList={"itemONE":("Select me",selcted)})
    data = myWindow.CurrentValues()
    print(data) 
   
  
if __name__ == "__main__":
    test()    