import DataStructure as ds


# The following are just test data
a = ds.Node("A", 0)
b = ds.Node("B", 0)
c = ds.Node("C", 0)
d = ds.Node("D", goal=True)
e = ds.Node("E", 0)
f = ds.Node("F", 0)
e1 = ds.Edge(a, c, 2)
e2 = ds.Edge(a, b, 1)
#e3 = ds.Edge(a, b, 10010101010)
e5 = ds.Edge(c, d, 1)
e6 = ds.Edge(d, f, 0)
e7 = ds.Edge(f, e, 0)


nodes = [a, b, c, d, e]
edges = [e1, e2, e5, e6, e7]

g1 = ds.Graph(a,edges)
#goal_ucs = g1.uniform_cost_search()
#print(goal_ucs)
#print(goal_ucs.get_path())
goal_dls=g1.depth_limited_search(limit=3)
#print(goal_dls)
goal_dls.get_path()
for node in goal_dls.get_path():
    print(node);
print("test")


#goal_bfs = g1.breadth_first_search()
#print(goal_bfs)
