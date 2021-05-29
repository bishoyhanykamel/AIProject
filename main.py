from tkinter import Tk, Canvas, Frame, BOTH, PhotoImage, Button, Label, simpledialog, Toplevel

import DataStructure as ds
from naryTree import Tree
from buchheim import buchheim
import treeVisual

import math

import time

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

depthlimit = 0

graph = None

#no_of_goals = 1

#start_bool=False

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



    bpush = Button(root, borderwidth=0)
    bpush.pack(side='bottom')






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
        #global start_bool
        startGoalIndices.append(c)
        #startandGoal()
        if len(startGoalIndices) == 1:
            btnlist[startGoalIndices[0]].config(bg="pale green")
        if len(startGoalIndices) > 1:
            btnlist[startGoalIndices[len(startGoalIndices)-1]].config(bg="IndianRed1")

    def startandGoal():

        global mode_bool

        global nodeObjList

        global edgeObjList

        global which_search

        global depthlimit

        global graph

        #if len(startGoalIndices) == 1:
        #    btnlist[startGoalIndices[0]].config(bg="pale green")
        #if len(startGoalIndices) > 1:
        #    btnlist[startGoalIndices[len(startGoalIndices)-1]].config(bg="IndianRed1")
        #    nodeObjList[startGoalIndices[len(startGoalIndices)-1]].SET_AS_GOAL()

        if len(startGoalIndices) > 1:

            startNode = startGoalIndices[0]
            #goalNode = startGoalIndices[1]
            g = ds.Graph(nodeObjList[startNode], nodeObjList, edgeObjList)

            no_of_goals=len(startGoalIndices)-1
            for j in range(no_of_goals):
                print("index set as goal:", startGoalIndices[j+1])
                nodeObjList[startGoalIndices[j+1]].SET_AS_GOAL()

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

            elif which_search == Searches.A_STAR:
                path = g.a_star_search()
                print(path)

            elif which_search == Searches.D_LIMITED:
                path = g.depth_limited_search(depthlimit)
                print(path)
                g.reset_visited()

            elif which_search == Searches.D_ITER:
                path = g.iterative_deepening()
                print(path)
                g.reset_visited()

            #createTree(g)
            graph = g


            illuminateNodes(g.vlist, g.ivlist, g.plist, g.iter_goal_found)
            g.reset_vlist()
            g.reset_ivlist()
            g.reset_plist()
            g.iter_bool = False
            g.maxlimit = 0
            g.stop_iter=False

            startGoalIndices.clear()
            mode_bool = 0

    #______________________________

    #UNDO THIS
    btnlist = list()

    heuristicList = list()

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

        heuristicList.append(Label(root, text="h=?", bg="CadetBlue4", fg="black"))

        nodeObjList.append(ds.Node(label=len(nodeObjList)))

        #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=move))
        btnlist[len(btnlist)-1].pack(side='left')
        btnline_Dict[len(btnlist)-1] = list()

        #heuristicx = btnlist[len(btnlist)-1].winfo_rootx()
        #heuristicy = btnlist[len(btnlist)-1].winfo_rooty()-10
        #heuristicList[len(heuristicList) - 1].place(x=heuristicx, y=heuristicy)

        #bb = bb + 1
        #bttn = Button(root, image=nodeimg, width=30,height=30)
        #bttn.pack()

    #i=i+1
    #command = lambda: [funct1(), funct2()]
    #command = lambda c=i: move(c)
    #btnlist.append(Button(root, image=nodeimg, width=30, height=30, command=lambda c=i: move(c)))

    #btn.append(Button(root, text=files[i], command=lambda c=i: print(btn[c].cget("text"))))

    #mybtn = Button(root, text="Create node", command=mybtnClick)
    #mybtn.pack(side='bottom')
    #mybtn.place(x=400, y=600)

    def illuminateNodes(vlist, ivlist, plist, iter_goal_found):
        #IF WHICHSEARCH = ITER

        global which_search

        if which_search == Searches.D_ITER:
            if iter_goal_found:
                i = 1000
                for k in range(len(ivlist)-1):
                    for j in range(len(ivlist[k])):
                        # rg3tha zy ma kant
                        # shlt lenvlist-1. k2enny 3mltlha visit. w b3den l2tha goal fa hlwnha lon visited. then lon goal
                        # btnlist[vlist[j]].config(bg="lawn green")
                        # time.sleep(2)
                        root.after(i, lambda x=j, h=k: btnlist[ivlist[h][x]].config(bg="lawn green"))
                        i = i + 1000
                    root.after(i, lambda: reset_illumination())
                    i=i+1000
                last_ivlist_ind = len(ivlist)-1
                for j in range(len(ivlist[last_ivlist_ind])-1):
                    root.after(i, lambda x=j, h=last_ivlist_ind: btnlist[ivlist[h][x]].config(bg="lawn green"))
                    i = i + 1000
                last_element_ind = len(ivlist[last_ivlist_ind])-1
                if len(vlist) > 0:
                    root.after(i, lambda x=last_element_ind, h=last_ivlist_ind: btnlist[ivlist[h][x]].config(bg="firebrick1"))
        else:
            print("LENGTH OF VLIST: ", len(vlist))
            i = 1000
            for j in range(len(vlist) - 1):
                # rg3tha zy ma kant
                # shlt lenvlist-1. k2enny 3mltlha visit. w b3den l2tha goal fa hlwnha lon visited. then lon goal
                # btnlist[vlist[j]].config(bg="lawn green")
                # time.sleep(2)
                root.after(i, lambda x=j: btnlist[vlist[x]].config(bg="lawn green"))
                i = i + 1000

            if len(vlist) > 0:
                root.after(i, lambda k=(vlist[len(vlist) - 1]): btnlist[k].config(bg="firebrick1"))
            # btnlist[len(vlist)-1].config(bg="SeaGreen1")
            # sleep 0.5s
            # KOLLOHOM F FUNCTION W7DA

        if len(plist)>0:
            i = i + 1000
            root.after(i, lambda p=plist: illuminatePath(p, on_off=1))
            i = i + 1000
            root.after(i, lambda p=plist: illuminatePath(p, on_off=2))
            i = i + 1000
            root.after(i, lambda p=plist: illuminatePath(p, on_off=1))
            i = i + 1000
            root.after(i, lambda p=plist: illuminatePath(p, on_off=2))
            i = i + 1000
            root.after(i, lambda p=plist: illuminatePath(p, on_off=1))

            print("PATH LIST AFTER REVERSE: ", plist)
            #5ALLIHA T FLASH 5 MARRAT W B3DEN TFDL MNWRA

        #ELSE HA SHOW MESSAGE NO PATH FOUND

    def illuminatePath(path, on_off):
        print(len(path))
        for j in range(len(path) - 1):
            line_start_index = path[j]
            line_end_index = path[j+1]
            for i in range (len(btnline_Dict[line_start_index])):
                line_index = btnline_Dict[line_start_index][i]
                if linePoints_Dict[line_index][0] == line_end_index or linePoints_Dict[line_index][1] == line_end_index:
                    if on_off==1:
                        my_canvas.itemconfig(lineList[line_index], fill="magenta2")
                    else:
                        my_canvas.itemconfig(lineList[line_index], fill="#000")
                        #lineList[line_index].config()  # or mayb add the index to a list then color them all. 34an a flash

    def reset_illumination():
        for x in range(len(btnlist)):
            btnlist[x].config(bg="white smoke")
        for y in range(len(lineList)):
            my_canvas.itemconfig(lineList[y], fill="#000")

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




    def changeModeBool2_DFS():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.DFS
        reset_illumination()
        #no_of_goals = simpledialog.askinteger("Enter number of goals", "How many goals? (>=1)", parent=root)

    def changeModeBool2_BFS():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.BFS
        reset_illumination()
        #no_of_goals = simpledialog.askinteger("Enter number of goals", "How many goals? (>=1)", parent=root)

    def changeModeBool2_UCS():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.UCS
        reset_illumination()
        #no_of_goals = simpledialog.askinteger("Enter number of goals", "How many goals? (>=1)", parent=root)

    def changeModeBool2_GREEDY():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.GREEDY
        reset_illumination()
        #no_of_goals = simpledialog.askinteger("Enter number of goals", "How many goals? (>=1)", parent=root)

    def changeModeBool2_ASTAR():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.A_STAR
        reset_illumination()
        #no_of_goals = simpledialog.askinteger("Enter number of goals", "How many goals? (>=1)", parent=root)

    def changeModeBool2_DLIM():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.D_LIMITED
        reset_illumination()
        global depthlimit
        depthlimit = simpledialog.askinteger("Enter maximum depth", "Depth limit? (>=0)", parent=root)

    def changeModeBool2_ITERD():
        #global no_of_goals
        global mode_bool
        mode_bool = 2
        global which_search
        which_search = Searches.D_ITER
        reset_illumination()
        #global depthlimit
        #depthlimit = simpledialog.askinteger("Enter maximum depth", "Depth limit? (>=0)", parent=root)


    searchDFSbtn = Button(root, text='DFS', width='15', command=changeModeBool2_DFS)
    #searchDFSbtn.pack(side='bottom')
    searchDFSbtn.place(x=500, y=610)

    searchDLimbtn = Button(root, text='Depth Limited', width='15', command=changeModeBool2_DLIM)
    #searchDLimbtn.pack(side='bottom')
    searchDLimbtn.place(x=500, y=700)

    searchIterDbtn = Button(root, text='Iterative Deepening', width='15', command=changeModeBool2_ITERD)
    #searchIterDbtn.pack(side='bottom')
    searchIterDbtn.place(x=500, y=730)

    searchBFSbtn = Button(root, text='BFS', width='15', command=changeModeBool2_BFS)
    #searchBFSbtn.pack(side='bottom')
    searchBFSbtn.place(x=500, y=640)

    searchUCSbtn = Button(root, text='Uniform Cost', width='15', command=changeModeBool2_UCS)
    #searchUCSbtn.pack(side='bottom')
    searchUCSbtn.place(x=500, y=670)

    searchGDYbtn = Button(root, text='Greedy', width='15', command=changeModeBool2_GREEDY)
    #searchGDYbtn.pack(side='bottom')
    searchGDYbtn.place(x=920, y=610)

    searchASTRbtn = Button(root, text='A*', width='15', command=changeModeBool2_ASTAR)
    #searchASTRbtn.pack(side='bottom')
    searchASTRbtn.place(x=920, y=640)


    resetbtn = Button(root, text='Reset', width='15')
    #searchASTRbtn.pack(side='bottom')
    resetbtn.place(x=1100, y=640)



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
            heuristicList[buttonInd].place(x=x, y=y)

            #myLabel.config(text="Coords: x: "+ str(event.x) + " y: "+ str(event.y))

            for x in range(len(btnline_Dict[buttonInd])):
            # print("sss" + str(btnline_Dict[buttonInd]))
                lineInd=btnline_Dict[buttonInd][x]
                print(btnline_Dict)
                print(lineInd)
                #print(btnline_Dict[0][0])
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



    #coordinates label
    #myLabel = Label(root, text="")
    #myLabel.pack()


    #PROBLEM WHEN CURSOR TOUCHES THE BUTTON. IS INSIDE THE BUTTON
    #CHANGE RELEASE MAYB
    #or winfopointerx
    root.bind('<Motion>', motion)



    #___________________________________________________

    def hInputPopUp():
        for x in range(len(heuristicList)):
            heuristicList[x].config(bg="PaleVioletRed1")
            h_val = simpledialog.askstring("Enter heuristics", "Enter node "+str(x)+" heuristic value:", parent=hpop)
            set_h_val(x, h_val)


    def set_h_val(x, h_val):
        global nodeObjList
        heuristicList[x].config(text="h=" + h_val, bg="CadetBlue2")
        nodeObjList[x].set_heuristic(int(h_val))
        #AND EDGEOBJLIST SET VAL


    def calc_eucl_h(g_ind):
        global nodeObjList
        root.update()
        x_goal = btnlist[g_ind].winfo_x()
        y_goal = btnlist[g_ind].winfo_y()
        for i in range(len(btnlist)):
            x = btnlist[i].winfo_x()
            y = btnlist[i].winfo_y()
            delta_x = abs(x_goal-x)
            delta_y = abs(y_goal-y)
            h = math.sqrt(delta_x ^ 2 + delta_y ^ 2)
            heuristicList[i].config(text="h=" + str(int(h)), bg="CadetBlue2")
            nodeObjList[i].set_heuristic(int(h))


    def calc_manh_h(g_ind):
        global nodeObjList
        pass

    def hEuclPopUp():
        goal_ind = simpledialog.askinteger("Enter goal", "Goal index:", parent=hpop)
        calc_eucl_h(goal_ind)

    def hManhPopUp():
        goal_ind = simpledialog.askstring("Enter goal", "Goal index:", parent=hpop)
        calc_manh_h(goal_ind)


    def heuristicOptionsPopUp():
        global hpop
        hpop = Toplevel(root)
        hpop.title("Heuristic Options")

        manhattanbtn = Button(hpop, text='Manhattan Distance (could be inadmissible)', command=hManhPopUp) #no command yet
        euclbtn = Button(hpop, text='Euclidean Distance (could be inadmissible)', command=hEuclPopUp)  # no command yet
        hinputbtn = Button(hpop, text='User Input', command=hInputPopUp)
        manhattanbtn.pack(padx=50, pady=10)
        euclbtn.pack()
        hinputbtn.pack(pady=10)




    # ___________________________________________________

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

    startbtn = Button(root, text="START", command=startandGoal)
    startbtn.pack(side='bottom')

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


    bpush3 = Button(root, borderwidth=0)
    bpush3.pack(side='bottom')


    heuristicBtn = Button(root, text='Choose a heuristic', width='15', command=heuristicOptionsPopUp)
    heuristicBtn.pack(side='bottom')

    costbtn = Button(root, text='Enter costs', width='15', command=costPopUp)
    costbtn.pack(side='bottom')


    bpush5 = Button(root, borderwidth=0)
    bpush5.pack(side='bottom')


    linebtn = Button(root, text='Edge', width='15', command=changeModeBool)
    linebtn.pack(side='bottom')
    #linebtn.place(x=400, y=650)

    mybtn = Button(root, text="Node", width='15', command=mybtnClick)
    mybtn.pack(side='bottom')



    bpush111 = Button(root, width='10', borderwidth=1)
    bpush111.pack(side='left')

    bpush10 = Button(root)
    bpush10.pack(side='left')


    def createTree(g1):
        x = len(g1.tree_level_dictionary) - 1
        parentLevelDict = dict()

        y = len(g1.tree_level_dictionary)

        while y > 1:

            for i in range(len(g1.tree_level_dictionary[y])):
                # p = Tree(g1.tree_level_dictionary[y][i].get_label())
                node = g1.tree_level_dictionary[y][i]
                key = g1.tree_level_dictionary[y][i].get_parent()
                if parentLevelDict.get(key) == None:
                    parentLevelDict[key] = []
                    parentLevelDict[key].append(node)
                else:
                    parentLevelDict[key].append(node)

            y = y - 1

        treeDict = dict()

        y = len(g1.tree_level_dictionary)
        while y > 1:

            for i in range(len(g1.tree_level_dictionary[y])):

                node = g1.tree_level_dictionary[y][i]
                key = node.get_parent()
                if parentLevelDict.get(node) == None:

                    p = Tree(node.get_label())
                    # bishoyToBucDict[node]=p
                    treeDict[node] = []
                    treeDict[node].append(p)
                else:
                    childList = []
                    for k in range(len(parentLevelDict[node])):
                        child = parentLevelDict[node][k]
                        childList.append(treeDict[child][0])
                        # print(treeDict[child][0])

                    theNewGeneratedTree = Tree(node.get_label(), *childList)
                    treeDict[node] = []
                    treeDict[node].append(theNewGeneratedTree)

            y = y - 1

        y = len(g1.tree_level_dictionary[1])
        # print('----------------------------------------------------------')
        while y > 0:

            for i in range(len(g1.tree_level_dictionary[y])):

                node = g1.tree_level_dictionary[y][i]
                key = node.get_parent()
                if parentLevelDict.get(node) == None:

                    p = Tree(node.get_label())
                    treeDict[node] = []
                    treeDict[node].append(p)
                else:
                    childList = []
                    for k in range(len(parentLevelDict[node])):
                        child = parentLevelDict[node][k]
                        childList.append(treeDict[child][0])
                        # print(treeDict[child][0])

                    # print(node.get_label(), childList)
                    print('--------------------')
                    print(childList)
                    print('--------------------')
                    # childList.reverse()
                    # print(revList,'rev list')
                    theNewGeneratedTree = Tree(node.get_label(), *childList)

                    # print(node.get_label(),'  : ',theNewGeneratedTree,'---------------09 ')
                    treeDict[node] = []
                    treeDict[node].append(theNewGeneratedTree)

            y = y - 1

        y = 1

        node = g1.tree_level_dictionary[y][0]
        key = node.get_parent()

        childList = []
        for k in range(len(g1.tree_level_dictionary[y]) - 1):
            child = g1.tree_level_dictionary[y][k + 1]
            childList.append(treeDict[child][0])
            # print(treeDict[child][0])

        # print(node.get_label(), childList)
        theNewGeneratedTree = Tree(node.get_label(), *childList)
        # bishoyToBucDict[node]=theNewGeneratedTree
        treeDict[node] = []
        treeDict[node].append(theNewGeneratedTree)
        # print('---------------------------------')

        bucTree = buchheim(theNewGeneratedTree)

        nodeToXcoordDict = dict()
        levelToBucObjectDict = dict()
        treeLevelNodeToBucNodeDict = dict()

        levelToBucObjectDict[0] = []
        for key in g1.tree_level_dictionary:
            levelToBucObjectDict[key] = []


        def generate_BucLevel_BucRow_Dict(bucNode):
            if (len(bucNode.children) == 0):
                nodeToXcoordDict[bucNode] = bucNode.x
                levelToBucObjectDict[bucNode.y].append(bucNode)
                return
            else:
                for children in bucNode.children:
                    generate_BucLevel_BucRow_Dict(children)
                nodeToXcoordDict[bucNode] = bucNode.x
                levelToBucObjectDict[bucNode.y].append(bucNode)

        generate_BucLevel_BucRow_Dict(bucTree)

        treeLevelNodeToBucNodeDict[g1.tree_level_dictionary[1][0]] = levelToBucObjectDict[0][0]

        for i in range(len(g1.tree_level_dictionary[1]) - 1):
            treeLevelNodeToBucNodeDict[g1.tree_level_dictionary[1][i + 1]] = levelToBucObjectDict[1][i]

        y = len(g1.tree_level_dictionary)
        while y > 1:
            for i in range(len(g1.tree_level_dictionary[y])):
                treeLevelNodeToBucNodeDict[g1.tree_level_dictionary[y][i]] = levelToBucObjectDict[y][i]

            y = y - 1

        treeSequence = g1.tree_draw_sequence

        treeVisual.treeVisualCall(treeLevelNodeToBucNodeDict, treeSequence)



    def treePopUp():
        #global treepop
        global graph
        #treepop = Toplevel(root)
        #treepop.state('zoomed')
        #treepop.title("TREEEEEE")
        createTree(graph)







    createTreebtn = Button(root, text='Create Tree', width='15', command=treePopUp)
    #searchASTRbtn.pack(side='bottom')
    createTreebtn.place(x=1100, y=680)




    root.mainloop()


#if __name__ == '__main__':
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