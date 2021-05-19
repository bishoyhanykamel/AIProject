import DataStructure as ds


# The following are just test data
a = ds.Node("A", 0)
b = ds.Node("B", 0)
c = ds.Node("C", 0)
d = ds.Node("D", goal=False)
e = ds.Node("E", goal=True)
f = ds.Node("F", 0)
e1 = ds.Edge(a, c, 2)
e2 = ds.Edge(a, b, 1)
#e3 = ds.Edge(a, b, 10010101010)
e5 = ds.Edge(b, d, 1)
e6 = ds.Edge(d, e, 0)
e7 = ds.Edge(f, e, 0)

nodes = [a, b, c, d, e]
edges = [e1, e2, e5, e6, e7]

#####========== [ TREE TEST DATA ] =========
g1 = ds.Graph(a,edges)
(goal_dfs, dfs_tree) = g1.depth_first_search()
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

dfs_max_level = dfs_tree.get_max_tree_level()
bfs_max_level = bfs_tree.get_max_tree_level()
print("Max level of DFS: {} ---- BFS {}".format(dfs_max_level, bfs_max_level))

for i in range(1, dfs_max_level):
    # print("DFS Level ({}): - Parent: {} \n\tNodes: ({})".format(i,
    #                                                            dfs_tree.get_parents_of_level(i),
    #                                                           dfs_tree.get_nodes_of_level(i)))
    for node in dfs_tree.get_parents_of_level(i):
        print("DFS Level: {} --- Parent: {}".format(i, node))

for i in range(1, bfs_max_level):
    # print("DFS Level ({}): - Parent: {} \n\tNodes: ({})".format(i,
    #                                                           bfs_tree.get_parents_of_level(i),
    #                                                           bfs_tree.get_nodes_of_level(i)))
    for node in bfs_tree.get_parents_of_level(i):
        print("BFS Level: {} --- Parent: {}".format(i, node))


#goal_ucs = g1.uniform_cost_search()
#print(goal_ucs)
#print(goal_ucs.get_path())
goal_ids=g1.depth_limited_search(2)
#print(goal_dls)
goal_ids.get_path()
for node in goal_ids.get_path():
    print(node)



#goal_bfs = g1.breadth_first_search()
#print(goal_bfs)