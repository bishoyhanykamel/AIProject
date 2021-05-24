import DataStructure as ds

# The following are just test data
a = ds.Node("A", 0)
b = ds.Node("B", 0)
c = ds.Node("C", 0)
g = ds.Node("G", 0, goal=True)
s = ds.Node("S", 0)
e1 = ds.Edge(s, a, 0)
e2 = ds.Edge(s, c, 0)
e3 = ds.Edge(b, a, 0)
e4 = ds.Edge(b, c, 0)
e5 = ds.Edge(c, g, 0)

s.add_child(a)
s.add_child(c)
b.add_child(a)
b.add_child(c)
c.add_child(g)


g1 = ds.Graph(s, list(), list())

goal = g1.depth_first_search()

print("\t\tDFS Tree:")
for node in g1.tree_draw_sequence:
    print(node, node.parent.get_label(), node.tree_level)
print("\n")
for node in g1.tree_visit_sequence:
    print(node, node.parent.get_label(), node.tree_level)

print("\n")
print("\n")
print("\t\tBFS Tree:")
goal = g1.breadth_first_search()
for node in g1.tree_draw_sequence:
    print(node, node.parent.get_label(), node.tree_level)
print("\n")
for node in g1.tree_visit_sequence:
    print(node, node.parent.get_label(), node.tree_level)
