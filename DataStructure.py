# import main
# from main import resetNodeObj

class Node:
    def __init__(self, label="", val=0, visited=False, goal=False, heuristic=-1):
        self.value = val
        self.label = label
        self.children = list()
        self.visited = visited
        self.goal = goal
        self.parent = None
        self.heuristic = heuristic

    def copy_node(self, node):
        self.value = node.get_value()
        self.label = node.get_label()
        self.children = node.get_children()
        self.visited = node.get_visited()
        self.parent = node.get_parent()
        self.goal = node.get_goal()
        self.heuristic = node.get_heuristic()

    def set_parent(self, p):
        self.parent = p

    def set_visited(self):
        self.visited = True

    #_______


    def reset_v(self):
        self.visited = False

    def SET_AS_GOAL(self):
        self.goal = True

    def reset_goal(self):
        self.goal = False

    def reset_parent(self):
        self.parent = None
    #_______

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_value(self):
        return self.value

    def get_label(self):
        return self.label

    def add_child(self, c1):
        self.children.append(c1)
        for x in range(len(self.children)):
            print(x)
            print("index")
            print(self.children[x].get_label())
        #self.children = sorted(self.children)

    def get_goal(self):
        return self.goal

    def get_heuristic(self):
        return self.heuristic

    def get_visited(self):
        return self.visited

    def get_path(self):
        prev_node = self.get_parent()
        temp_list = []
        while prev_node is not None:
            temp_list.insert(0, prev_node)
            prev_node = prev_node.get_parent()
        return temp_list

    def __str__(self):
        if self.get_parent() is None:
            parent = "None"
        else:
            parent = self.get_parent().get_label()
        return "Node {} Parent {}".format(self.get_label(),
                                              parent)


class Edge:
    def __init__(self, s, e, v):
        self.start_node = s
        self.end_node = e
        self.value = v

        #self.start_node.get_children().append(e)
        #self.end_node.get_children().append(s)

        # self.end_node.set_parent(s)

    def get_start_node(self):
        return self.start_node

    def get_end_node(self):
        return self.end_node

    def get_value(self):
        return self.value

    def __str__(self):
        return "Edge: ({}) -> ({})  || Value: {}". \
            format(self.start_node, self.end_node, self.value)


class Graph:
    def __init__(self, inode, nodeObjList):
        self.initial_node = inode
        self.nodeObjList = nodeObjList
        pass

    def depth_first_search(self):
        stack_list = [self.initial_node]
        visited = []
        while len(stack_list) >= 1:
            print("been here")
            current_node = stack_list.pop(-1)
            print(current_node.get_visited())
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                print("init node visited or not", self.initial_node.get_visited())
                print("goal b4 reset", current_node.get_goal())
                self.reset_visited()
                stack_list.clear()
                visited.clear()
                print("init node visited or not AFTER RESET", self.initial_node.get_visited())
                print("goal after reset", current_node.get_goal())
                return current_node
            print(current_node.get_visited())
            current_node.set_visited()
            print(current_node.get_visited())
            visited.append(current_node.get_label())
            print(len(current_node.get_children()))
            for node in sorted(current_node.get_children(), reverse=True, key=lambda x: x.get_label()):
                temp_node = Node()
                temp_node.copy_node(node)
                stack_list.append(temp_node)
                temp_node.set_parent(current_node)
            pass
        self.initial_node.visited = False
        print(current_node.get_visited())
        self.reset_visited()
        stack_list.clear()
        visited.clear()
        print(current_node.get_visited())
        return "No goal found - Depth First Search"
        pass

    def breadth_first_search(self):
        queue_list = [self.initial_node]
        visited = []
        while len(queue_list) >= 1:
            current_node = queue_list.pop(0)
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                return current_node
            current_node.set_visited()
            visited.append(current_node.get_label())
            for node in current_node.get_children():
                temp_node = Node()
                temp_node.copy_node(node)
                queue_list.append(temp_node)
                temp_node.set_parent(current_node)
            pass
        self.initial_node.visited = False
        return "No goal found - Breadth First Search"
        pass

    def uniform_cost_search(self):
        pass

    def iterative_deepening(self):
        pass

    def greedy_search(self):
        pass

    def a_star_search(self):
        pass

    def reset_visited(self):
        # global nodeObjList
        print("LENGTH: ", len(self.nodeObjList))
        for x in range(len(self.nodeObjList)):
            print("IN NODEOBJLIST b4", self.nodeObjList[x].get_visited())
            print("GOAL THING B4", self.nodeObjList[x].get_goal())
            self.nodeObjList[x].reset_v()
            self.nodeObjList[x].reset_goal()
            self.nodeObjList[x].reset_parent()
            print("IN NODEOBJLIST", self.nodeObjList[x].get_visited())
            print("GOAL THING after", self.nodeObjList[x].get_goal())

#def reset_visited():
#    global nodeObjList
#    for x in range(len(main.nodeObjList)):
#        main.nodeObjList[x].reset_v()
#        main.nodeObjList[x].reset_goal()
#        main.nodeObjList[x].reset_parent()
