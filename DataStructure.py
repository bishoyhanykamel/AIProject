# import main

# from main import illuminateNode
# =======================================================================================
# ====================================[Node of Graph]====================================
# =======================================================================================
class Node:
    def __init__(self, label="", val=0, visited=False, goal=False, heuristic=-1, depth=0, cpy_node=None):
        if cpy_node is not None:
            self.copy_node(cpy_node)
        else:
            self.depth = depth
            self.value = val
            self.label = label
            self.children = list()
            self.visited = visited
            self.goal = goal
            self.parent = None
            self.heuristic = heuristic
            self.astar_value = 0
            self.edges = list()
            self.tree_level = 0
            self.tree_children = list()
            self.depth = depth

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

    def copy_node(self, node):
        self.value = node.value
        self.label = node.label
        self.children = node.children
        self.visited = node.visited
        self.parent = node.parent
        self.goal = node.goal
        self.heuristic = node.heuristic
        self.tree_level = node.tree_level
        self.tree_children = node.tree_children
        self.edges = node.edges
        self.astar_value = node.get_astar_value()
        self.edges = node.get_edges()

    def get_tree_level(self):
        return self.tree_level

    def get_tree_children(self):
        return self.tree_children

    def add_tree_child(self, c1):
        temp_tree_node = Node(cpy_node=c1)
        temp_tree_node.tree_level += 1
        self.tree_children.append(temp_tree_node)

    def set_astar_value(self, v):
        self.astar_value = v

    def get_astar_value(self):
        return self.astar_value

    def add_edge(self, e):
        self.edges.append(e)

        # mlhash lzma l cost 0
        # ASCENDING SORT
        # self.edges = sorted(self.edges, reverse=False, key=lambda k: k.get_value())
        # self.children = sorted(self.children)

        # mlhash lzma l cost 0
        for x in range(len(self.edges)):
            # print(x, " th child")
            print("node ", str(self.get_label()), " edge cost: ", self.edges[x].get_value())
            # print(self.children[x].get_label())

    def get_edges(self):
        return self.edges

    def set_parent(self, p):
        self.parent = p

    def set_visited(self):
        self.visited = True

    # _______

    def reset_v(self):
        self.visited = False

    def SET_AS_GOAL(self):
        self.goal = True

    def reset_goal(self):
        self.goal = False

    def reset_parent(self):
        self.parent = None

    # _______

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_value(self):
        return self.value

    def get_node_value(self):
        return self.value

    def get_label(self):
        return self.label

    def add_child(self, c1):
        self.children.append(c1)
        self.children = sorted(self.children, key=lambda x: x.label)
        for x in range(len(self.children)):
            # print(x, " th child")
            print("index of ", x, "child (after sort): ", self.children[x].get_label())
            # print(self.children[x].get_label())

    def get_goal(self):
        return self.goal

    def get_heuristic(self):
        return self.heuristic

    def set_heuristic(self, h):
        self.heuristic = h

    def get_visited(self):
        return self.visited

    def set_node_value(self, value):
        self.value = value

    def get_path(self):
        path_list = []
        tempnode = self
        while tempnode is not None:
            path_list.append(tempnode)
            tempnode = tempnode.get_parent()
        return path_list

    def __str__(self):
        if self.get_parent() is None:
            parent = "None"
        else:
            parent = self.get_parent().get_label()
        return "Node {} - Parent {}".format(self.get_label(), parent)


# =======================================================================================
# ====================================[Edge of Graph]=====================================
# =======================================================================================
class Edge:
    def __init__(self, s, e, v):
        self.start_node = s
        self.end_node = e
        self.value = v

        # self.start_node.get_children().append(e)
        # self.end_node.get_children().append(s)

        # self.end_node.set_parent(s)

    def set_start_node(self, s):
        self.start_node = s

    def set_end_node(self, e):
        self.end_node = e

    def get_start_node(self):
        return self.start_node

    def get_end_node(self):
        return self.end_node

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

    def __str__(self):
        return "Edge: ({}) -> ({})  || Value: {}". \
            format(self.start_node, self.end_node, self.value)


# =======================================================================================
# =====================================[Algorithms]======================================
# =======================================================================================
# note: all algorithms will return a tuple (goal_node, tree generated)
class Graph:
    def __init__(self, inode, nodeObjList, edgeObjList):
        self.initial_node = inode
        # self.edgelist = edges
        self.nodeObjList = nodeObjList
        self.edgeObjList = edgeObjList
        self.vlist = list()
        self.plist = list()
        self.tree_draw_sequence = list()
        self.tree_visit_sequence = list()
        self.tree_level_dictionary = dict()
        pass

    def create_level_dictionary(self):
        for node in self.tree_draw_sequence:
            self.tree_level_dictionary[node.tree_level] = self.tree_level_dictionary.get(node.tree_level, list()) \
                                                       + [node]

    pass

    def reset_levels(self):
        level = 1
        current_level_children = [self.tree_draw_sequence[0]]
        for i in range(len(self.tree_draw_sequence)):
            node = self.tree_draw_sequence[i]
            node_parent = node.parent
            parent_of_brother = current_level_children[-1].parent
            grand_of_node = None
            grand_of_brother = None
            if parent_of_brother is not None:
                grand_of_brother = parent_of_brother.parent
            if node_parent is not None:
                grand_of_node = node_parent.parent
            if node_parent == parent_of_brother or grand_of_brother == grand_of_node:
                node.tree_level = level
                current_level_children.append(node)
                continue
            else:
                level += 1
                current_level_children.clear()
                node.tree_level = level
                current_level_children.append(node)
        self.create_level_dictionary()
        pass

    def depth_first_search(self):

        initial_node = Node(cpy_node=self.initial_node)
        stack_list = [initial_node]

        # code for tree
        self.tree_draw_sequence.clear()
        self.tree_visit_sequence.clear()
        self.tree_draw_sequence.append(initial_node)
        # continue algorithm

        visited = []
        while len(stack_list) >= 1:
            # print("been here")
            current_node = stack_list.pop(-1)
            # print(current_node.get_visited())
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                self.vlist = visited.copy()
                self.vlist.append(current_node.get_label())

                # self.illuminate_anim(visited)
                pathlist = current_node.get_path()
                # self.plist = pathlist.copy()
                # self.plist.reverse()
                print("path found by dfs: ", end=" ")
                while len(pathlist) > 0:
                    # print("path: ", pathlist.pop().get_label())
                    self.plist.append(pathlist[len(pathlist) - 1].get_label())  # HL DI SHALLOWS COPY???????
                    print(pathlist.pop().get_label(), end=" ")
                print(" ")
                # self.plist.reverse()
                # APPEND F PATHLIST ATTRIBUTE FL GRAPH. W TALLA3 MESSAGEBOX FI NO3 L SEARCH,START/GOALINDICES,
                #                   PATH FOUND
                # for j in range(len(pathlist)):
                #    print(pathlist[j].get_label()),

                # print("init node visited or not", self.initial_node.get_visited())
                # print("goal b4 reset", current_node.get_goal())
                self.reset_visited()
                stack_list.clear()
                visited.clear()
                # print("init node visited or not AFTER RESET", self.initial_node.get_visited())
                # print("goal after reset", current_node.get_goal())
                self.reset_levels()
                return current_node
            # print(current_node.get_visited())
            current_node.set_visited()

            # illuminateNode(current_node.get_label())

            # print(current_node.get_visited())
            self.tree_visit_sequence.append(current_node)
            visited.append(current_node.get_label())
            # print(len(current_node.get_children()))
            for node in sorted(current_node.get_children(), reverse=True, key=lambda x: x.get_label()):
                temp_node = Node(cpy_node=node)
                stack_list.append(temp_node)
                temp_node.set_parent(current_node)

                # code for tree
                self.tree_draw_sequence.append(temp_node)
                # continue algorithm

            pass
        return "No goal found - Depth First Search"
        pass

    def breadth_first_search(self):
        initial_node = Node(cpy_node=self.initial_node)
        queue_list = [initial_node]
        visited = []
        # code for tree
        self.tree_draw_sequence.clear()
        self.tree_visit_sequence.clear()
        self.tree_draw_sequence.append(initial_node)
        # continue algorithm
        while len(queue_list) >= 1:
            current_node = queue_list.pop(0)
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                self.vlist = visited.copy()
                self.vlist.append(current_node.get_label())

                pathlist = current_node.get_path()
                print("path found by bfs: ", end=" ")
                while len(pathlist) > 0:
                    self.plist.append(pathlist[len(pathlist) - 1].get_label())

                    print(pathlist.pop().get_label(), end=" ")
                print(" ")

                self.reset_visited()
                queue_list.clear()
                visited.clear()
                self.reset_levels()
                return current_node
            current_node.set_visited()
            visited.append(current_node.get_label())
            self.tree_visit_sequence.append(current_node)
            for node in sorted(current_node.get_children(), key=lambda x: x.get_label()):
                temp_node = Node(cpy_node=node)
                queue_list.append(temp_node)
                temp_node.set_parent(current_node)
                # code for tree
                self.tree_draw_sequence.append(temp_node)
                # continue algorithm
            pass
        return "No goal found - Breadth First Search"
        pass

    #    def uniform_cost_search(self):
    #        self.initial_node.set_node_value(0)
    #        inode = Node()
    #        inode.copy_node(self.initial_node)
    #        fringe = [inode]
    #        visited = []
    #        while len(fringe) >= 1:
    #            print("entered here")
    #            current_node = fringe.pop(0)

    #            if current_node.get_visited() or current_node.get_label() in visited:
    #                continue

    #            if current_node.get_goal() == True:
    #                self.reset_visited()
    #                fringe.clear()
    #                visited.clear()
    #                return current_node

    #            current_node.set_visited()
    #            visited.append(current_node.get_label())

    #            for edge in current_node.get_edges():
    #                print("entered edge loop")
    #                print(edge.get_start_node().get_label())
    #                print(edge.get_end_node().get_label())

    # if edge.get_end_node().get_label() == current_node.get_label():

    #    if edge.get_end_node().get_label() not in visited or edge.get_start_node().get_label() not in visited:
    #         print("this was done")
    #          new_node = Node()
    #           if edge.get_end_node().get_label() == current_node.get_label():
    #                new_node.copy_node(edge.get_start_node())
    #             else:
    #                  new_node.copy_node(edge.get_end_node())
    #               new_node.set_parent(current_node)
    #                new_node.set_node_value(current_node.get_node_value() + edge.get_value())
    #                 fringe.append(new_node)

    #          fringe.sort(key=lambda x: x.get_node_value())

    #       self.reset_visited()
    #        fringe.clear()
    #        visited.clear()
    #        print("No goal found - Uniform Cost Search")
    #        pass

    def uniform_cost_search(self):
        self.initial_node.set_node_value(0)
        inode = Node()
        inode.copy_node(self.initial_node)
        fringe = [inode]
        visited = []

        # code for tree
        self.tree_draw_sequence.clear()
        self.tree_visit_sequence.clear()
        self.tree_draw_sequence.append(inode)
        # continue algorithm

        while len(fringe) >= 1:
            print("entered here")
            current_node = fringe.pop(0)

            if current_node.get_visited() or current_node.get_label() in visited:
                continue

            if current_node.get_goal() == True:

                self.vlist = visited.copy()
                self.vlist.append(current_node.get_label())

                pathlist = current_node.get_path()
                print("path found by ucs: ", end=" ")
                while len(pathlist) > 0:
                    self.plist.append(pathlist[len(pathlist) - 1].get_label())

                    print(pathlist.pop().get_label(), end=" ")
                print(" ")

                self.reset_visited()
                fringe.clear()
                visited.clear()
                self.reset_levels()
                return current_node

            current_node.set_visited()
            self.tree_visit_sequence.append(current_node)
            visited.append(current_node.get_label())

            for edge in current_node.get_edges():
                print("entered edge loop")
                print(edge.get_start_node().get_label())
                print(edge.get_end_node().get_label())

                # if edge.get_end_node().get_label() == current_node.get_label():

                if edge.get_end_node().get_label() not in visited or edge.get_start_node().get_label() not in visited:
                    print("this was done")
                    new_node = Node()
                    if edge.get_end_node().get_label() == current_node.get_label():
                        new_node.copy_node(edge.get_start_node())
                    else:
                        new_node.copy_node(edge.get_end_node())
                    new_node.set_parent(current_node)
                    new_node.set_node_value(current_node.get_node_value() + edge.get_value())
                    fringe.append(new_node)
                    # code for tree
                    self.tree_draw_sequence.append(new_node)
                    # continue algorithm

            fringe.sort(key=lambda x: x.get_node_value())

        self.reset_visited()
        fringe.clear()
        visited.clear()
        print("No goal found - Uniform Cost Search")
        pass

    def iterative_deepening(self, maxlimit):
        # for i in range(1, maxlimit + 1):
        #     dls_result = self.depth_limited_search(i)
        #     if not dls_result == -1:
        #         break
        # return dls_result
        pass

    def greedy_search(self):
        inode = Node()
        inode.copy_node(self.initial_node)
        fringe = [inode]
        visited = []
        # code for tree
        self.tree_draw_sequence.clear()
        self.tree_visit_sequence.clear()
        self.tree_draw_sequence.append(inode)
        # continue algorithm
        while fringe:
            current_node = fringe.pop(0)

            if current_node.get_visited() or current_node.get_label() in visited:
                continue

            if current_node.get_goal() == True:
                self.vlist = visited.copy()
                self.vlist.append(current_node.get_label())

                pathlist = current_node.get_path()
                print("path found by greedy: ", end=" ")
                while len(pathlist) > 0:
                    self.plist.append(pathlist[len(pathlist) - 1].get_label())

                    print(pathlist.pop().get_label(), end=" ")
                print(" ")

                self.reset_visited()
                fringe.clear()
                visited.clear()
                self.reset_levels()
                return current_node

            current_node.set_visited()
            self.tree_visit_sequence.append(current_node)
            visited.append(current_node.get_label())

            for node in current_node.get_children():
                if node.get_label() not in visited:
                    newnode = Node()
                    newnode.copy_node(node)
                    newnode.set_parent(current_node)
                    fringe.append(newnode)
                    # code for tree
                    self.tree_draw_sequence.append(newnode)
                    # continue algorithm
            fringe.sort(key=lambda x: x.get_heuristic())

        self.reset_visited()
        fringe.clear()
        visited.clear()
        print("no path found - Greedy Search")
        pass

    def a_star_search(self):
        self.initial_node.set_astar_value(self.initial_node.get_heuristic())
        inode = Node()
        inode.copy_node(self.initial_node)
        fringe = [inode]
        visited = []
        # visited_nodes_values = {}
        # code for tree
        self.tree_draw_sequence.clear()
        self.tree_visit_sequence.clear()
        self.tree_draw_sequence.append(inode)
        # continue algorithm
        while fringe:
            current_node = fringe.pop(0)

            if current_node.get_visited() or current_node.get_label() in visited:
                continue

            if current_node.get_goal() == True:
                self.vlist = visited.copy()
                self.vlist.append(current_node.get_label())

                pathlist = current_node.get_path()
                print("path found by a*: ", end=" ")
                while len(pathlist) > 0:
                    self.plist.append(pathlist[len(pathlist) - 1].get_label())

                    print(pathlist.pop().get_label(), end=" ")
                print(" ")

                self.reset_visited()
                fringe.clear()
                visited.clear()
                self.reset_levels()
                return current_node

            current_node.set_visited()
            self.tree_visit_sequence.append(current_node)
            visited.append(current_node.get_label())

            # visited_nodes_values[current_node.get_label()] = current_node.get_node_value()
            # current_node.set_node_value(current_node.get_node_value() - current_node.get_heuristic())

            for edge in current_node.get_edges():
                print("entered edge loop")
                print(edge.get_start_node().get_label())
                print(edge.get_end_node().get_label())

                # if edge.get_end_node().get_label() == current_node.get_label():

                if edge.get_end_node().get_label() not in visited or edge.get_start_node().get_label() not in visited:
                    print("this was done")
                    newnode = Node()
                    if edge.get_end_node().get_label() == current_node.get_label():
                        newnode.copy_node(edge.get_start_node())
                    else:
                        newnode.copy_node(edge.get_end_node())
                    newnode.set_parent(current_node)
                    newnode.set_node_value(current_node.get_node_value() + edge.get_value())
                    newnode.set_astar_value(newnode.get_node_value() + newnode.get_heuristic())
                    # mmkn 23ml l astar fl class 3la tul nodevalue+heuristic
                    fringe.append(newnode)
                    # code for tree
                    self.tree_draw_sequence.append(newnode)
                    # continue algorithm

            fringe.sort(key=lambda x: x.get_astar_value())

        self.reset_visited()
        fringe.clear()
        visited.clear()
        print("no path found - A* Search")
        pass

    def reset_visited(self):
        # global nodeObjList
        # print("LENGTH: ", len(self.nodeObjList))
        for x in range(len(self.nodeObjList)):
            # print("IN NODEOBJLIST b4", self.nodeObjList[x].get_visited())
            # print("GOAL THING B4", self.nodeObjList[x].get_goal())
            self.nodeObjList[x].reset_v()
            self.nodeObjList[x].reset_goal()
            self.nodeObjList[x].reset_parent()
            self.nodeObjList[x].set_node_value(0)
            # print("IN NODEOBJLIST", self.nodeObjList[x].get_visited())
            # print("GOAL THING after", self.nodeObjList[x].get_goal())

    def reset_vlist(self):
        self.vlist = list()

    def reset_plist(self):
        self.plist = list()

    # def illuminate_anim(self, vlist):
    # illuminateNode(self)
    #    illuminateNode(vlist)

    # def illuminate_visited(self, ind):

# def reset_visited():
#    global nodeObjList
#    for x in range(len(main.nodeObjList)):
#        main.nodeObjList[x].reset_v()
#        main.nodeObjList[x].reset_goal()
#        main.nodeObjList[x].reset_parent()
