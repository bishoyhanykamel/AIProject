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
        self.children = sorted(self.children)

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


class Graph:
    def __init__(self, inode):
        self.initial_node = inode
        pass

    def depth_first_search(self):
        stack_list = [self.initial_node]
        while len(stack_list) >= 1:
            current_node = stack_list.pop(-1)
            if current_node.get_visited():
                continue
            if current_node.get_goal():
                return current_node
            current_node.set_visited()
            for node in sorted(current_node.get_children(), reverse=True, key=lambda x: x.get_label()):
                temp_node = Node()
                temp_node.copy_node(node)
                stack_list.append(temp_node)
                temp_node.set_parent(current_node)
            pass
        self.initial_node.visited = False
        return "No goal found - Depth First Search"
        pass

    def breadth_first_search(self):
        queue_list = [self.initial_node]
        while len(queue_list) >= 1:
            current_node = queue_list.pop(0)
            if current_node.get_visited():
                continue
            if current_node.get_goal():
                return current_node
            current_node.set_visited()
            for node in current_node.get_children():
                temp_node = Node()
                temp_node.copy_node(node)
                queue_list.append(temp_node)
                temp_node.set_parent(current_node)
            pass
        self.initial_node.visited = False
        return "No goal found - Depth First Search"
        pass

    def uniform_cost_search(self):
        pass

    def iterative_deepening(self):
        pass

    def greedy_search(self):
        pass

    def a_star_search(self):
        pass
