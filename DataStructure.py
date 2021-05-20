# import main
# from main import resetNodeObj

# =======================================================================================
# ====================================[Node of Graph]====================================
# =======================================================================================
class Node:
    def __init__(self, label="", val=0, visited=False, goal=False, heuristic=-1, lvl=0, cpy_node=None, depth=0):
        if cpy_node is not None:
            self.copy_node(cpy_node)
        else:
            self.value = val
            self.label = label
            self.children = list()
            self.visited = visited
            self.goal = goal
            self.parent = None
            self.heuristic = heuristic
            self.tree_level = lvl
            self.tree_children = list()
            self.depth = depth
            self.edges = list()

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

    def get_tree_level(self):
        return self.tree_level

    def get_tree_children(self):
        return self.tree_children

    def add_tree_child(self, c1):
        temp_tree_node = Node(cpy_node=c1)
        temp_tree_node.tree_level += 1
        self.tree_children.append(temp_tree_node)

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

    # def add_child(self, c1):
    # self.children.append(c1)

    # ASCENDING SORT
    # self.children = sorted(self.children, reverse=False, key=lambda k: k.get_label())
    # self.children = sorted(self.children)

    # for x in range(len(self.children)):
    # print(x, " th child")
    # print("index of ", x, "child (after sort): ", self.children[x].get_label())
    # print(self.children[x].get_label())

    def get_goal(self):
        return self.goal

    def get_heuristic(self):
        return self.heuristic

    def get_visited(self):
        return self.visited

    def set_node_value(self, value):
        self.value = value

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
        return "Node {} - Parent {}".format(self.get_label(), parent)


# =======================================================================================
# ====================================[Edge of Graph]=====================================
# =======================================================================================
class Edge:
    def __init__(self, s, e, v):
        self.start_node = s
        self.end_node = e
        self.value = v
        self.start_node.add_child(e)
        self.end_node.add_child(s)

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
    def __init__(self, inode, edges, nodeObjList, edgeObjList):
        self.initial_node = inode
        self.edgelist = edges
        self.nodeObjList = nodeObjList
        self.edgeObjList = edgeObjList
        pass

    def depth_first_search(self):
        initial_node = Node(cpy_node=self.initial_node)
        stack_list = [initial_node]
        visited = []
        # code for tree
        dfs_tree = Tree(initial_node)
        # continue algorithm
        while len(stack_list) >= 1:
            current_node = stack_list.pop(-1)
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                dfs_tree.reset_levels()
                dfs_tree.set_level_parent()
                return current_node, dfs_tree
            current_node.set_visited()
            visited.append(current_node.get_label())
            for node in sorted(current_node.get_children(), reverse=True, key=lambda x: x.get_label()):
                temp_node = Node(cpy_node=node)
                stack_list.append(temp_node)
                temp_node.set_parent(current_node)
                # code for tree
                current_node.add_tree_child(temp_node)
                dfs_tree.add_node(temp_node)
                # continue algorithm
            pass
        return "No goal found - Depth First Search", "No tree generated"
        pass

    def breadth_first_search(self):
        initial_node = Node(cpy_node=self.initial_node)
        queue_list = [initial_node]
        visited = []
        # code for tree
        bfs_tree = Tree(initial_node)
        # continue algorithm
        while len(queue_list) >= 1:
            current_node = queue_list.pop(0)
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                bfs_tree.reset_levels()
                bfs_tree.set_level_parent()
                return current_node, bfs_tree
            current_node.set_visited()
            visited.append(current_node.get_label())
            for node in sorted(current_node.get_children(), key=lambda x: x.get_label()):
                temp_node = Node(cpy_node=node)
                queue_list.append(temp_node)
                temp_node.set_parent(current_node)
                # code for tree
                current_node.add_tree_child(temp_node)
                bfs_tree.add_node(temp_node)
                # continue algorithm
            pass
        return "No goal found - Breadth First Search", "No tree generated"
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
        inode = Node(cpy_node=self.initial_node)
        fringe = [inode]
        visited = []
        # code for tree
        ucs_tree = Tree(inode)
        # continue algorithm
        while fringe:
            testednode = fringe.pop(0)
            if testednode.get_goal() == True:
                ucs_tree.reset_levels()
                ucs_tree.set_level_parent()
                return testednode, ucs_tree
            else:
                visited.append(testednode.get_label())
            for edge in self.edgelist:
                if edge.get_start_node().get_label() == testednode.get_label() and edge.get_end_node().get_label() not in visited:
                    newnode = Node(cpy_node=edge.get_end_node())
                    newnode.set_parent(testednode)
                    newnode.set_node_value(edge.get_start_node().get_node_value() + edge.get_value())
                    fringe.append(newnode)
                    # code for tree
                    testednode.add_tree_child(newnode)
                    ucs_tree.add_node(newnode)
                    # continue algorithm
                elif edge.get_end_node().get_label() == testednode.get_label() and edge.get_start_node().get_label() not in visited:
                    newnode = Node(cpy_node=edge.get_end_node())
                    newnode.set_parent(testednode)
                    newnode.set_node_value(edge.get_end_node().get_node_value() + edge.get_value())
                    fringe.append(newnode)
                    # code for tree
                    testednode.add_tree_child(newnode)
                    ucs_tree.add_node(newnode)
                    # continue algorithm
            fringe.sort(key=lambda x: x.get_node_value())
        print("no path found - uniform cost search")

    def depth_limited_search(self, limit):
        self.initial_node.set_depth(0)
        inode = Node()
        inode.copy_node(self.initial_node)
        fringe = [inode]
        visited = []
        # code for tree
        dls_tree = Tree(inode)
        # continue algorithm
        while fringe:
            testednode = fringe.pop(-1)
            if testednode.get_depth() > limit:
                break
            elif testednode.get_goal() == True and testednode.get_label():
                dls_tree.reset_levels()
                dls_tree.set_level_parent()
                return testednode, dls_tree

            else:
                visited.append(testednode.get_label())
                for node in testednode.get_children():
                    if node.get_label() not in visited:
                        newnode = Node(cpy_node=node)
                        newnode.set_parent(testednode)
                        newnode.set_depth(testednode.get_depth() + 1)
                        fringe.append(newnode)
                        # code for tree
                        testednode.add_tree_child(newnode)
                        dls_tree.add_node(newnode)
                        # continue algorithm
        return None

    def iterative_deepening(self, maxlimit):
        for i in range(1, maxlimit + 1):
            dls_result = self.depth_limited_search(i)
            if not dls_result == -1:
                break
        return dls_result

    # ## --------------not tested yet------------------- #####
    def greedy_search(self):
        inode = Node()
        inode.copy_node(self.initial_node)
        fringe = [inode]
        visited = []
        # code for tree
        greedy_tree = Tree(inode)
        # continue algorithm
        while fringe:
            testednode = fringe.pop(0)
            if (testednode.get_goal() == True):
                greedy_tree.reset_levels()
                greedy_tree.set_level_parent()
                return testednode, greedy_tree

            else:
                visited.append(testednode.get_label())
                for node in testednode.get_children():
                    if node.get_label() not in visited:
                        newnode = Node(cpy_node=node)
                        newnode.copy_node(node)
                        newnode.set_parent(testednode)
                        fringe.append(newnode)
                        # code for tree
                        testednode.add_tree_child(newnode)
                        greedy_tree.add_node(newnode)
                        # continue algorithm
                fringe.sort(key=lambda x: x.get_heuristic())
        print("no path found - Greedy Search")

        print("no path found")

    #####################################################################
    def a_star_search(self):
        self.initial_node.set_node_value(self.initial_node.get_heuristic())
        inode = Node()
        inode.copy_node(self.initial_node)
        fringe = [inode]
        visited_labels = []
        visited_nodes_values = {}
        # code for tree
        dls_tree = Tree(inode)
        # continue algorithm
        while fringe:
            testednode = fringe.pop(0)
            if testednode.get_goal() == True:
                return testednode
            else:
                visited_labels.append(testednode.get_label())
                visited_nodes_values[testednode.get_label()] = testednode.get_node_value()
                testednode.set_node_value(testednode.get_node_value() - testednode.get_heuristic())
            for edge in self.edgelist:
                if edge.get_start_node().get_label() == testednode.get_label():
                    newnode = Node()
                    newnode.copy_node(edge.get_end_node())
                    newval = edge.get_value() + edge.get_start_node().get_node_value() + newnode.get_heuristic()
                    if (edge.get_end_node().get_label() not in visited_labels) or (
                            visited_nodes_values[edge.get_end_node().get_label()] > newval):
                        newnode.set_parent(testednode)
                        newnode.set_node_value(newval)
                        fringe.append(newnode)
                elif edge.get_end_node().get_label() == testednode.get_label():
                    newnode = Node()
                    newnode.copy_node(edge.get_start_node())
                    newval = edge.get_value() + edge.get_end_node().get_node_value() + newnode.get_heuristic()
                    if (edge.get_start_node().get_label() not in visited_labels) or (
                            visited_nodes_values[edge.get_start_node().get_label()] > newval):
                        newnode.set_parent(testednode)
                        newnode.set_node_value(
                            edge.get_end_node().get_node_value() + edge.get_value() + newnode.get_heuristic())
                        fringe.append(newnode)
            fringe.sort(key=lambda x: x.get_node_value())
        print("no path found - A* search")

        pass


# =======================================================================================
# =======================================[Tree]==========================================
# =======================================================================================

def print_node_children(node):
    for n in node.get_tree_children():
        return n


class Tree:
    def __init__(self, n1):
        self.nodes = list()
        self.add_node(n1)
        self.level_map = dict()

    def add_node(self, n):
        self.nodes.append(n)

    def get_initial_node(self):
        return self.nodes[0]

    def get_tree_nodes(self):
        return self.nodes

    def print_tree(self):
        for node in self.nodes:
            print("Level: {} - Node: {}".format(node.tree_level, node))

    def reset_levels(self):
        level = 1
        current_level_children = [self.nodes[0]]
        for i in range(len(self.nodes)):
            node = self.nodes[i]
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

    def set_level_parent(self):
        level_parent_map = dict()
        for n in self.nodes:
            if n is None:
                continue
            level_parent_map[n.tree_level] = [n.parent] + level_parent_map.get(n.tree_level, [])
        self.level_map = level_parent_map

    def get_level_parent(self):
        return self.level_map

    # returns maximum level of generated search tree
    def get_max_tree_level(self):
        max_level = 0
        for level in self.level_map.keys():
            if max_level < level:
                max_level = level
        return max_level

    # returns a list of all parent nodes of a specified level
    def get_parents_of_level(self, lvl):
        return self.level_map[lvl]

    # returns a list of all the nodes that belong to the same level
    def get_nodes_of_level(self, lvl):
        nodes_list = []
        for node in self.nodes:
            if node is None:
                continue
            if node.tree_level == lvl:
                nodes_list.append(node)

        return nodes_list
        pass

    # def reset_visited(self):
    # global nodeObjList
    # print("LENGTH: ", len(self.nodeObjList))
    # for x in range(len(self.nodeObjList)):
    # print("IN NODEOBJLIST b4", self.nodeObjList[x].get_visited())
    # print("GOAL THING B4", self.nodeObjList[x].get_goal())
    # self.nodeObjList[x].reset_v()
    # self.nodeObjList[x].reset_goal()
    # self.nodeObjList[x].reset_parent()
    # self.nodeObjList[x].set_node_value(0)
    # print("IN NODEOBJLIST", self.nodeObjList[x].get_visited())
    # print("GOAL THING after", self.nodeObjList[x].get_goal())

# def reset_visited():
#    global nodeObjList
#    for x in range(len(main.nodeObjList)):
#        main.nodeObjList[x].reset_v()
#        main.nodeObjList[x].reset_goal()
#        main.nodeObjList[x].reset_parent()
