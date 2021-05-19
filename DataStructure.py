# =======================================================================================
# ====================================[Node of Graph]====================================
# =======================================================================================
class Node:
    def __init__(self, label="", val=0, visited=False, goal=False, heuristic=-1, lvl=0, cpy_node=None):
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

    def get_tree_level(self):
        return self.tree_level

    def get_tree_children(self):
        return self.tree_children

    def add_tree_child(self, c1):
        temp_tree_node = Node(cpy_node=c1)
        temp_tree_node.tree_level += 1
        self.tree_children.append(temp_tree_node)

    def set_parent(self, p):
        self.parent = p

    def set_visited(self):
        self.visited = True

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
        self.children = sorted(self.children, key=lambda x: x.label)

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


# =======================================================================================
# ====================================[Edge of Graph]=====================================
# =======================================================================================
class Edge:
    def __init__(self, s, e, v):
        self.start_node = s
        self.end_node = e
        self.value = v
        self.start_node.get_children().append(e)
        self.end_node.get_children().append(s)
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


# =======================================================================================
# =====================================[Algorithms]======================================
# =======================================================================================
# note: all algorithms will return a tuple (goal_node, tree generated)
class Graph:
    def __init__(self, inode):
        self.initial_node = inode
        pass

    def depth_first_search(self):
        # modified version of ds for marking nodes as visited
        initial_node = Node(cpy_node=self.initial_node)
        # initial_node.copy_node(self.initial_node)
        stack_list = [initial_node]
        # code for tree
        dfs_tree = Tree(initial_node)
        # continue algorithm
        visited = []
        while len(stack_list) >= 1:
            current_node = stack_list.pop(-1)
            # code for tree
            # dfs_tree.add_node(current_node)
            # continue algorithm
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                dfs_tree.reset_levels()
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
        # initial_node.copy_node(self.initial_node)
        queue_list = [initial_node]
        # code for tree
        bfs_tree = Tree(initial_node)
        # continue algorithm
        visited = []
        while len(queue_list) >= 1:
            current_node = queue_list.pop(0)
            # function call to pass current node to tree structure
            if current_node.get_visited() or current_node.get_label() in visited:
                continue
            if current_node.get_goal():
                bfs_tree.reset_levels()
                return current_node, bfs_tree
            current_node.set_visited()
            visited.append(current_node.get_label())
            for node in sorted(current_node.get_children(), key=lambda x: x.get_label()):
                temp_node = Node(cpy_node=node)
                # temp_node.copy_node(node)
                queue_list.append(temp_node)
                temp_node.set_parent(current_node)
                # code for tree
                current_node.add_tree_child(temp_node)
                bfs_tree.add_node(temp_node)
                # continue algorithm
            pass
        return "No goal found - Breadth First Search", "No tree generated"
        pass

    def uniform_cost_search(self):
        pass

    def iterative_deepening(self):
        pass

    def greedy_search(self):
        pass

    def a_star_search(self):
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

    def add_node(self, n):
        self.nodes.append(n)

    def get_initial_node(self):
        return self.nodes[0]

    def get_tree_nodes(self):
        return self.nodes

    def print_tree(self):
        for node in self.nodes:
            # print("Level: {} - Parent: {} - Children: {}".format(
            #    node.get_tree_level(), node.get_label(), print_node_children(node)
            # ))
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
                i = i - 1
                current_level_children.clear()
                node.tree_level = level
                current_level_children.append(node)


    def get_level_parent(self):
        level_parent_map = dict()
        for n in self.nodes:
            level_parent_map[n.tree_level] = [n.parent] + level_parent_map.get(n.tree_level, [])
            pass
        return level_parent_map
