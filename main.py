from tkinter import Tk, Canvas, Frame, BOTH, PhotoImage, Button, Label, simpledialog

import DataStructure as ds

import enum


class Searches(enum.Enum):
   DFS = 0
   BFS = 1
   UCS = 2
   D_LIMITED = 3
   D_ITER = 4
   GREEDY = 5
   A_STAR = 6

#import random


# class Example(Frame):
#
#     def __init__(self):
#         super().__init__()
#         moving_button = Button()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.master.title("Lines")
#         self.pack(fill=BOTH, expand=1)
#
#         canvas = Canvas(self)
#         canvas.create_line(15, 25, 200, 10, fill="#AAA", width=2)
#         canvas.create_line(15, 25, 200, 10, fill="#000", width=0.5)
#         # canvas.create_line(15, 10, 200, 0, width=10)
#         # canvas.create_line(300, 35, 300, 200, dash=(4, 2))
#         # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, width=5)
#
#         nodeimg = PhotoImage(file='C:/Users/mohgh/Desktop/testnode.png')
#         btn = Button(self.master, image=nodeimg)
#         btn.pack()
#
#
#         canvas.pack(fill=BOTH, expand=1)

mode_bool=0

which_search = 0

btnIndices = list()
moveBtn = False
startGoalIndices = list()
nodeObjList = list()
edgeObjList = list()

#btnlist = list()

#btnlistc=list()

#def illuminateNode(ind):
#    print(len(btnlistc))
#    #    #    global btnlist
#    btnlistc[ind].config(bg="lawn green")

#visited_list = list()

#def illuminateNode(vlist):
#    global visited_list
#    #visited_list = g.visited()
#    visited_list = vlist
#   btnlistc[ind].config(bg="lawn green")


def main():


    root = Tk()
    # ex = Example()
    canvas = Canvas()
    nodeimg = PhotoImage(file='C:/Users/mohgh/Desktop/rednode2.png')
    # img = nodeimg.zoom(2)

    #most recent
    #btns = list()
    #btns.append(Button(root, text="A", image=nodeimg, width=30,height=30))
    #btns.append(Button(root, image=nodeimg, text="A", width=30, height=30))

    # btn = Button(root, image=nodeimg, width=30,height=30)

    #most recent
    #lbl = Label(text="A")
    #btns[0].place(x=250.5,y=0)
    #btns[1].place(x=250, y=50)
    #lbl.place(x=250,y=0)

    #root.attributes("-fullscreen", True)
    #root.overrideredirect(False)

    #root.geometry("400x250+300+300")
    #root.geometry("400x400")

    root.state('zoomed')

    #w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    #root.geometry("%dx%d+0+0" % (w-10, h-100))

    #______________________________




    def modeSelect (c):
        global mode_bool
        if mode_bool == 0:
            move(c)

        elif mode_bool == 1:
            createLine(c)

        else:
            startSearch(c)

    def createLine (c):
        global btnIndices
        btnIndices.append(c)
        functLine()


    def startSearch (c):
        global startGoalIndices
        startGoalIndices.append(c)
        startandGoal()

    def startandGoal():

        global mode_bool

        global nodeObjList

        global edgeObjList

        global which_search

        if len(startGoalIndices) == 2:

            startNode = startGoalIndices[0]
            goalNode = startGoalIndices[1]
            g = ds.Graph(nodeObjList[startNode], nodeObjList, edgeObjList)
            nodeObjList[goalNode].SET_AS_GOAL()

            if which_search == Searches.DFS:
                path = g.depth_first_search()
                print(path)

            elif which_search == Searches.BFS:
                path = g.breadth_first_search()
                print(path)

            elif which_search == Searches.UCS:
                path = g.uniform_cost_search()
                print(path)

            elif which_search == Searches.GREEDY:
                path = g.greedy_search()
                print(path)

            illuminateNodes(g.vlist)
            g.reset_vlist()

            startGoalIndices.clear()
            mode_bool = 0

    #______________________________

    #UNDO THIS
    btnlist = list()


    #btnlistc = btnlist
    #nodeObjList = list()

    #edgeObjList = list()

    #globalY=0
    def mybtnClick():
        #global globalY
        #global bb
        #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=lambda c=len(btnlist): move(c)))
        #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=lambda c=len(btnlist): print(c)))

        global nodeObjList

        #global btnlist

        #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=lambda c=len(btnlist): move(c)))
        #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=lambda c=len(btnlist): modeSelect(c)))
        btnlist.append(Button(root, text=len(btnlist), width=3, height=1, command=lambda c=len(btnlist): modeSelect(c)))

        nodeObjList.append(ds.Node(label=len(nodeObjList)))

        #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=move))
        btnlist[len(btnlist)-1].pack()
        btnline_Dict[len(btnlist)-1] = list()

        #bb = bb + 1
        #bttn = Button(root, image=nodeimg, width=30,height=30)
        #bttn.pack()

    #i=i+1
    #command = lambda: [funct1(), funct2()]
    #command = lambda c=i: move(c)
    #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=lambda c=i: move(c)))

    #btn.append(Button(root, text=files[i], command=lambda c=i: print(btn[c].cget("text"))))

    mybtn = Button(root, text="Create node", command=mybtnClick)
    mybtn.pack(side='bottom')

    def illuminateNodes(vlist):
        print("LENGTH OF VLIST: ", len(vlist))
        for j in range(len(vlist)):
            btnlist[vlist[j]].config(bg="lawn green")
            #sleep 0.5s

    #def illuminateNode(ind):
    #    #    global btnlist
    #    btnlist[ind].config(bg="lawn green")

    def costPopUp():
        for x in range(len(labelList)):
            labelList[x].config(bg="VioletRed1")
            e_cost = simpledialog.askstring("Enter costs", "Enter edge "+str(x)+" cost:", parent=root)
            set_e_cost(x, e_cost)

            #ASKINTEGER

    def set_e_cost(x, e_cost):
        global edgeObjList
        labelList[x].config(text="cost " + e_cost, bg="RoyalBlue1")
        edgeObjList[x].set_value(int(e_cost))
        #AND EDGEOBJLIST SET VAL

    costbtn = Button(root, text='Enter costs', command=costPopUp)
    costbtn.pack(side='bottom')


    def changeModeBool2_DFS():
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.DFS

    def changeModeBool2_BFS():
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.BFS

    def changeModeBool2_UCS():
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.UCS

    def changeModeBool2_GREEDY():
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.GREEDY

    searchDFSbtn = Button(root, text='DFS', command=changeModeBool2_DFS)
    searchDFSbtn.pack(side='bottom')

    searchBFSbtn = Button(root, text='BFS', command=changeModeBool2_BFS)
    searchBFSbtn.pack(side='bottom')

    searchUCSbtn = Button(root, text='Uniform Cost', command=changeModeBool2_UCS)
    searchUCSbtn.pack(side='bottom')

    searchGDYbtn = Button(root, text='Greedy', command=changeModeBool2_GREEDY)
    searchGDYbtn.pack(side='bottom')

    #mybtn.place()

    #______________________________

    #bttn2 = Button(root, image=nodeimg, width=30, height=30)
    #bttn2.pack()

    #def move(e):
    #    bttn2.place(x=e.x, y=e.y)

    buttonInd=-1

    def move(v):
        global moveBtn
        global buttonInd
        buttonInd=v
        print((v))

        if moveBtn:
            moveBtn = False
        else:
            moveBtn = True

    #moving_button = Button(root, text='Click Meee', command=move)

    #moving_button.place(x=50, y=50)

    def motion(event):
        global buttonInd

        #global btnlist
        #x, y = event.x, event.y
        x, y = event.widget.winfo_pointerxy()
        #print(moveBtn)
        if moveBtn == True:
            # moving_button.place(x=x-800, y=y-410)
            #moving_button = Button(root, text='Click Meee', command=move)

            #moving_button.place(x=event.x, y=event.y, anchor="s")
            #moving_button.place(x=x, y=y, anchor="s")
            btnlist[buttonInd].place(x=x, y=y, anchor="s")
            #myLabel.config(text="Coords: x: "+ str(event.x) + " y: "+ str(event.y))
            try:
                for x in range(len(btnline_Dict[buttonInd])):
                # print("sss" + str(btnline_Dict[buttonInd]))
                    lineInd=btnline_Dict[buttonInd][x]
                    print(btnline_Dict)
                    print(lineInd)
                    print(btnline_Dict[0][0])
                    btnStartInd=linePoints_Dict[lineInd][0]
                    print(btnStartInd)
                    btnEndInd = linePoints_Dict[lineInd][1]

                    xx1, yy1 = btnlist[btnStartInd].winfo_rootx(), btnlist[btnStartInd].winfo_rooty()
                    xx2, yy2 = btnlist[btnEndInd].winfo_rootx(), btnlist[btnEndInd].winfo_rooty()


                    print("xx1:" + str(xx1))
                    print("yy1:" + str(yy1))
                    print("xx1:" + str(xx2))
                    print("yy2:" + str(yy2))

                    my_canvas.coords(lineList[lineInd], xx1, yy1, xx2, yy2)

                    xxmid = (xx1 + xx2) / 2
                    yymid = (yy1 + yy2) / 2
                    labelList[lineInd].place(x=xxmid, y=yymid)

            except Exception as e:
                print(e)


    #coordinates label
    #myLabel = Label(root, text="")
    #myLabel.pack()


    #PROBLEM WHEN CURSOR TOUCHES THE BUTTON. IS INSIDE THE BUTTON
    #CHANGE RELEASE MAYB
    #or winfopointerx
    root.bind('<Motion>', motion)



    #___________________________________________________

    #HOMA FEN HOMA FEN HOMA FEN
    #mybtn1 = Button(root, text="Node1")
    #mybtn1.place(x=500, y=410)

    #mybtn2 = Button(root, text="Node2")
    #mybtn2.place(x=100, y=200)

    my_canvas = Canvas(root, width=300, height=200, bg="bisque2")
    my_canvas.pack(fill=BOTH, expand=1)

    lineList = list()
    btnline_Dict = dict()

    linePoints_Dict = dict()

    labelList = list()
    #lineLabel_Dict = dict() #might need it


    #tmp = list()
    #tmp.append('A')
    #tmp.append('B')
    #btnline_Dict[4] = tmp

    def functLine():
        global mode_bool

        global nodeObjList

        global edgeObjList

        #global btnlist

        #x1, y1 = root.btnlist[0].winfo_rootx(), root.btnlist[0].winfo_rooty()
        #x2, y2 = root.btnlist[1].winfo_rootx(), root.btnlist[1].winfo_rooty()
        if len(btnIndices)==2:
            x1, y1 = btnlist[btnIndices[0]].winfo_rootx(), btnlist[btnIndices[0]].winfo_rooty()
            x2, y2 = btnlist[btnIndices[1]].winfo_rootx(), btnlist[btnIndices[1]].winfo_rooty()
            print(x1)
            print(y1)
            print(x2)
            print(x2)
            lineList.append(my_canvas.create_line(x1, y1, x2, y2, fill="#000", width=2))
            print(len(lineList))

            labelList.append(Label(root, text="edge "+ str(len(labelList)), bg="#FFFF00", fg="black"))
            labelx = (x1 + x2) / 2
            labely = (y1 + y2) / 2
            labelList[len(labelList)-1].place(x=labelx, y=labely)


            # myLabel = Label(root, text="")
            # myLabel.pack()

            edgeObjList.append(ds.Edge(nodeObjList[btnIndices[0]], nodeObjList[btnIndices[1]], 0))
            nodeObjList[btnIndices[0]].add_child(nodeObjList[btnIndices[1]])
            nodeObjList[btnIndices[1]].add_child(nodeObjList[btnIndices[0]])

            nodeObjList[btnIndices[0]].add_edge(edgeObjList[len(edgeObjList)-1])
            nodeObjList[btnIndices[1]].add_edge(edgeObjList[len(edgeObjList)-1])


            linePoints_Dict[(len(lineList)-1)]=list()
            linePoints_Dict[(len(lineList) - 1)].append(btnIndices[0])
            linePoints_Dict[(len(lineList) - 1)].append(btnIndices[1])
            print(linePoints_Dict)

            btnline_Dict[btnIndices[0]].append(len(lineList) - 1)
            btnline_Dict[btnIndices[1]].append(len(lineList) - 1)
            btnIndices.clear()
            mode_bool=0


    def changeModeBool():
        global mode_bool
        mode_bool = 1

    linebtn = Button(root, text='Click Lineee', command=changeModeBool)
    linebtn.pack(side='bottom')

    #my_canvas.pack(pady=20)
    #         canvas = Canvas(self)
    #         canvas.create_line(15, 25, 200, 10, fill="#AAA", width=2)
    #         canvas.create_line(15, 25, 200, 10, fill="#000", width=0.5)
    #         # canvas.create_line(15, 10, 200, 0, width=10)
    #         # canvas.create_line(300, 35, 300, 200, dash=(4, 2))
    #         # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, width=5)
    #
    #         nodeimg = PhotoImage(file='C:/Users/mohgh/Desktop/testnode.png')
    #         btn = Button(self.master, image=nodeimg)
    #         btn.pack()
    #
    #
    #         canvas.pack(fill=BOTH, expand=1)

    root.mainloop()


if __name__ == '__main__':
    print(type(main()))
    main()
################################################################################
# from tkinter import *
#
# root = Tk()
#
# files = [] #creates list to replace your actual inputs for troubleshooting purposes
# btn = [] #creates list to store the buttons ins
#
# for i in range(50): #this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
#     files.append("Button"+str(i))
#
# for i in range(len(files)): #this says for *counter* in *however many elements there are in the list files*
#     #the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
#     #btn.append(Button(root, text=files[i], command=lambda c=i: print(btn[c].cget("text"))))
#
#     btn.append(Button(root, text=files[i], command=lambda c=i: move(c)))
#     btn[i].pack() #this packs the buttons
#     i=i+1
#
# root.mainloop()