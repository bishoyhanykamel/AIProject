import DataStructure as ds

# The following are just test data
a = ds.Node("A", 0)
b = ds.Node("B", 0)
c = ds.Node("C", 0)
d = ds.Node("D", 0)
e = ds.Node("E", goal=True)
f = ds.Node("F", 0)
e1 = ds.Edge(a, b, 1)
e2 = ds.Edge(a, c, 4)
e3 = ds.Edge(b, c, 1)
e5 = ds.Edge(c, f, 1)
e6 = ds.Edge(c, d, 1)
e7 = ds.Edge(d, e, 200)
e8 = ds.Edge(f, e, 1)


nodes = [a, b, c, d, e, f]
edges = [e1, e2, e3, e5, e6, e7, e8]


g1 = ds.Graph(a, edges)

# ###========== [ TREE TEST DATA ] =========

# (goal_dfs, dfs_tree) = g1.depth_first_search()
# dfs_tree.print_tree()
# level_map = dfs_tree.get_level_parent()
# for key, val in level_map.items():
#    for v in val:
#        print("Key: {} - Value: {}".format(key, v))

# print("\n\n")

# goal_bfs, bfs_tree = g1.breadth_first_search()
# bfs_tree.print_tree()
# level_map = bfs_tree.get_level_parent()
# for key, val in level_map.items():
#    for v in val:
#       print("Key: {} - Value: {}".format(key, v))
#
# dfs_max_level = dfs_tree.get_max_tree_level()
# bfs_max_level = bfs_tree.get_max_tree_level()
# print("Max level of DFS: {} ---- BFS {}".format(dfs_max_level, bfs_max_level))

# for i in range(1, dfs_max_level):
# print("DFS Level ({}): - Parent: {} \n\tNodes: ({})".format(i,
#                                                            dfs_tree.get_parents_of_level(i),
#                                                           dfs_tree.get_nodes_of_level(i)))
# for node in dfs_tree.get_parents_of_level(i):
#   print("DFS Level: {} --- Parent: {}".format(i, node))

# for i in range(1, bfs_max_level):
# print("DFS Level ({}): - Parent: {} \n\tNodes: ({})".format(i,
#                                                           bfs_tree.get_parents_of_level(i),
#                                                           bfs_tree.get_nodes_of_level(i)))
#    for node in bfs_tree.get_parents_of_level(i):
#       print("BFS Level: {} --- Parent: {}".format(i, node))

goal_bfs, bfs_tree = g1.breadth_first_search()
bfs_tree.print_tree()
for node in goal_bfs.get_path():
    print(node)

goal_ucs, ucs_tree = g1.uniform_cost_search()
print(goal_ucs)
ucs_tree.print_tree()

for node in goal_ucs.get_path():
    print(node)
# goal_ids = g1.depth_limited_search(2)
# print(goal_dls)
# goal_ids.get_path()
# for node in goal_ids.get_path():
#    print(node)

# goal_bfs = g1.breadth_first_search()
# print(goal_bfs)
