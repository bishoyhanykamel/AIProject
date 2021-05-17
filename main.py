import DataStructure as ds


# The following are just test data
a = ds.Node("A", 0)
b = ds.Node("B", 0)
c = ds.Node("C", 0, goal = True)
d = ds.Node("D", 0)
e = ds.Node("E", 0)
e1 = ds.Edge(a, b, 0)
e2 = ds.Edge(a, c, 0)
e3 = ds.Edge(a, d, 0)
e4 = ds.Edge(a, e, 0)
e5 = ds.Edge(b, c, 0)
e6 = ds.Edge(b, d, 0)
e7 = ds.Edge(b, e, 0)
e8 = ds.Edge(c, d, 0)
e9 = ds.Edge(c, e, 0)
e0 = ds.Edge(d, e, 0)

nodes = [a, b, c, d, e]
edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e0]

g1 = ds.Graph(a)
goal_dps = g1.depth_first_search()
print(goal_dps)

for node in nodes:
    node.visited = False

goal_bfs = g1.breadth_first_search()
print(goal_bfs)
