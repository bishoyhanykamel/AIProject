import copy
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

# labelList[0].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))
# labelList[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='2',padx='2',pady='2'))
# labelList[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='3',padx='2',pady='2'))
# labelList[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='4',padx='2',pady='2'))
# labelList[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='5',padx='2',pady='2'))
# labelList[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='6',padx='2',pady='2'))
# labelList[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='7',padx='2',pady='2'))
#
#
#
# nodeDict[0]=[]
# nodeDict[0].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))





# nodeDict[1]=[]
# nodeDict[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='2',padx='2',pady='2'))
# nodeDict[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='3',padx='2',pady='2'))
# nodeDict[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='4',padx='2',pady='2'))
# nodeDict[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))
# nodeDict[1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))
#
#
# nodeDict[2]=[]
# nodeDict[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='5',padx='2',pady='2'))
# nodeDict[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='6',padx='2',pady='2'))
# nodeDict[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))
# nodeDict[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))
# nodeDict[2].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='1',padx='2',pady='2'))




# nodeDict[1]=[[] for i in range (numberOfParentChildren)]
# nodeDict[1][0]=tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='2',padx='2',pady='2')
# nodeDict[1][1]=tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='3',padx='2',pady='2')


#
# nodeDict[2]=[[] for i in range (len(nodeDict[1]))]
# nodeDict[2][0].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='4',padx='2',pady='2'))
# nodeDict[2][0].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='5',padx='2',pady='2'))
#
#
# nodeDict[2][1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='4',padx='2',pady='2'))
# nodeDict[2][1].append(tkinter.Label(mainCanvas,borderwidth=4, bg='white', relief='solid', width=2, height=2,text='5',padx='2',pady='2'))





# print(nodeDict)
# print(gridColList)
#
#
# def calcCoords(numberOfNodes,level):
#     nodeGridPosition[level]=[]
#     dist=cols//(numberOfNodes+1)
#     nodeGridPosition[level].append(dist)
#     for x in range(numberOfNodes-1):
#         nodeGridPosition[level].append(dist*(x+2))
#
#
#
#
# calcCoords(len(nodeDict[0]),0)
# calcCoords(len(nodeDict[1]),1)
# calcCoords(len(nodeDict[2]),2)



# ToDo
#
# def generateNodeColumnIndex(nodeDict):
#
#     nodeGridPosition[0] = []
#     nodeGridPosition[0].append(cols//2)
#     nodeGridPosition[1]=[[] for i in range (numberOfParentChildren)]
#
#     for v in range(numberOfParentChildren):
#         tempFactor=0
#         nodeGridPosition[1][v]=(nodeGridPosition[0][0]//len(nodeDict[1]))+(nodeGridPosition[0][0]*tempFactor)
#         tempFactor
#
#     for i in range(2,len(nodeDict)):
#
#         for j in range(len(nodeDict[i-1])):
#
#
#
#
#
#
#
#             if (nodeDict[i][j] != list):
#                nodeGridPosition[i]=[]
#                nodeGridPosition[i].append(0)
#             else:
#                 for k in range(len(nodeDict[i][j])):
#
#


print('test')
print(treeLevelNodeToBucNodeDict[treeSequence[0]].y)


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
    lbl.grid(row=int(becToDsNode.y),column=int(xCord)+10)
    Label()
    updatePos()
    mainWindow.update()


def delayEdge(startNode,endNode):

    slope= ((endNode.winfo_y())-startNode.winfo_y())/((endNode.winfo_x())-startNode.winfo_x()+10)
    print(slope)
    newEdge=mainCanvas.create_line(startNode.winfo_x() ,
                           startNode.winfo_y() ,
                           startNode.winfo_x(),
                           startNode.winfo_y(),
                           arrow=tkinter.LAST)
    edgeList.append(newEdge)
    edgeDict[len(edgeList)-1]=list()
    edgeDict[len(edgeList)-1].append(startNode)
    edgeDict[len(edgeList) - 1].append(endNode)

    mainWindow.update()

    for y_anim in range (startNode.winfo_y(),endNode.winfo_y(),1):
        x_anim = (endNode.winfo_x()) - (((endNode.winfo_y()) - y_anim) / (slope))

        mainCanvas.coords(newEdge, startNode.winfo_x(),
                                   startNode.winfo_y() ,
                                   x_anim,
                                   y_anim,
                                   )

        mainWindow.update()
        updatePos()


def drawTree(delayTime,treeseq):


    for i in range (len(treeseq)):
        mainCanvas.after(delayTime, delayNode(treeLevelNodeToBucNodeDict[treeSequence[i]]))






        mainWindow.update()


drawTree(1000,treeSequence)
# mainCanvas.after(1000, delayNode(0, 0, 10))
# updatePos()
# mainWindow.update()
#
#
# mainCanvas.after(1000,delayNode(1,0,5))
# updatePos()
# mainCanvas.update()
#
# mainCanvas.after(1000,delayNode(1,1,15))
# updatePos()
# mainCanvas.update()
#
# mainCanvas.after(1000,delayEdge(labelList[0][0],labelList[1][0]))
# mainCanvas.after(1000,delayEdge(labelList[0][0],labelList[1][1]))
#
# mainCanvas.after((1000),delayNode(2,0,2))
# updatePos()
# mainCanvas.after((1000),delayNode(2,1,8))
# updatePos()
# mainCanvas.after(1000,delayNode(2,2,12))
# mainCanvas.after(1000,delayNode(2,3,18))
#
#
# mainCanvas.after(3000,delayEdge(labelList[1][0],labelList[2][0]))
# mainCanvas.after(3000,delayEdge(labelList[1][0],labelList[2][1]))
#
# mainWindow.update()
#


# mainCanvas.after(3000,delayEdge(labelList[1][0],labelList[2][0]))


# mainWindow.update()
# # mainCanvas.after(3000,delayEdge(labelList[0][0],labelList[1][0]))
#
#
#
# mainWindow.update()



# labelList[0][0].grid(row=0, column=cols // 2)
# labelList[0][1].grid(row=1, column=cols // 2)


mainWindow.mainloop()

