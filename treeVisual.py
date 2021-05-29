import copy
import math
import tkinter
from tkinter import YES, BOTH
from tkinter.ttk import *
from test_ds import treeLevelNodeToBucNodeDict,treeSequence

mainWindow = tkinter.Tk()
mainWindow.geometry('1080x720+150+10')
mainWindow.resizable(0,0)
cols=31
levels=10
numberOfParentChildren=2

mainWindow.title('Tree Visualization')
mainWindow.state('zoomed')

mainCanvas=tkinter.Canvas(mainWindow, width=300, height=200, bg="bisque2")
mainCanvas.pack(expand=1, fill=BOTH)


nodeGridPosition=dict()
nodeDict= {}



edgeList=list()
edgeDict= dict()
frameList=[[] for i in range (levels)]
labelList= [[] for i in range (levels)]

# Adjusting row weight for Main window and Canvas
for i in range(levels):
    mainCanvas.rowconfigure(i, weight=2)
    mainWindow.rowconfigure(i,weight=2)

for i in range(cols):
    mainCanvas.columnconfigure(i, weight=1)
    mainWindow.columnconfigure(i, weight=1)


#



def updatePos():
    for i in range (len(edgeList)):
        mainCanvas.coords(edgeList[i],
                          edgeDict[i][0].winfo_x()
                          ,edgeDict[i][0].winfo_y()
                          ,edgeDict[i][1].winfo_x()
                          ,edgeDict[i][1].winfo_y())


becNodeToGridLabelDict=dict()

def delayNode(becToDsNode):
    lbl=tkinter.Label(mainCanvas,borderwidth=4, relief='solid',height=2,width=2,text=becToDsNode.tree,padx='2',pady='2')
    xCord=becToDsNode.x*2
    becNodeToGridLabelDict[becToDsNode]=lbl
    lbl.grid(row=int(becToDsNode.y),column=int(xCord)+13)
    mainWindow.update()
    if becToDsNode.parent==None:
        return
    else:
        delayEdge(becNodeToGridLabelDict[becToDsNode.parent],becNodeToGridLabelDict[becToDsNode])
        # updatePos()
        # mainWindow.update()
    updatePos()
    mainWindow.update()
lbll=tkinter.Label()
lbll.winfo_rootx()

def delayEdge(startNode,endNode):
    mainWindow.update()
    slope= ((endNode.winfo_y())-startNode.winfo_y())/((endNode.winfo_x())-startNode.winfo_x()+1)
    print(slope)
    newEdge=mainCanvas.create_line(startNode.winfo_x()+1 ,
                           startNode.winfo_y()+1 ,
                           startNode.winfo_x()+1,
                           startNode.winfo_y()+1,
                           arrow=tkinter.LAST)
    mainWindow.update()
    print(startNode.winfo_x(),startNode.winfo_y() ,
                           endNode.winfo_x(),
                           endNode.winfo_y())
    edgeList.append(newEdge)
    edgeDict[len(edgeList)-1]=list()
    edgeDict[len(edgeList)-1].append(startNode)
    edgeDict[len(edgeList) - 1].append(endNode)

    mainWindow.update()

    for y_anim in range(startNode.winfo_y(), endNode.winfo_y(), 3):
        # mainWindow.update()
        x_anim = (endNode.winfo_x()) - (((endNode.winfo_y()) - y_anim) / (slope))
        # print(startNode.winfo_x(), startNode.winfo_y(),
        #       endNode.winfo_x(),
        #       endNode.winfo_y())
        mainCanvas.coords(newEdge, startNode.winfo_x()+2,
                                   startNode.winfo_y() ,
                                   x_anim,
                                   y_anim,
                                   )

        mainWindow.update()
        updatePos()

#
def drawTree(delayTime,treeseq):


    for i in range (len(treeseq)):
        mainCanvas.after(delayTime, delayNode(treeLevelNodeToBucNodeDict[treeSequence[i]]))
        mainWindow.update()



drawTree(500,treeSequence)



mainWindow.mainloop()

