import DataStructure as ds


# The following are just test data
a = ds.Node("A", 0)
b = ds.Node("B", 0)
c = ds.Node("C", 0)
d = ds.Node("D", 0)
e = ds.Node("E", 0, goal=True)
f = ds.Node("F", 0)
e1 = ds.Edge(a, b, 0)
e2 = ds.Edge(a, c, 0)
e3 = ds.Edge(a, d, 0)
e5 = ds.Edge(a, e, 0)
e6 = ds.Edge(b, e, 0)
e11 = ds.Edge(b, d, 0)
e7 = ds.Edge(b, f, 0)
e8 = ds.Edge(d, c, 0)
e9 = ds.Edge(d, f, 0)
e10 = ds.Edge(e, f, 0)

nodes = [a, b, c, d, e, f]
edges = [e1, e2, e3, e5, e6, e7, e8, e9, e10, e11]

g1 = ds.Graph(b)
(goal_dfs, dfs_tree) = g1.depth_first_search()
# print(goal_dfs)
dfs_tree.print_tree()
level_map = dfs_tree.get_level_parent()
for key, val in level_map.items():
    for v in val:
        print("Key: {} - Value: {}".format(key, v))


print("\n\n")

goal_bfs, bfs_tree = g1.breadth_first_search()
bfs_tree.print_tree()
level_map = bfs_tree.get_level_parent()
for key, val in level_map.items():
    for v in val:
        print("Key: {} - Value: {}".format(key, v))
