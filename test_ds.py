import DataStructure as ds
from naryTree import Tree
from buchheim import buchheim
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
a.add_child(s)
s.add_child(c)
c.add_child(s)
b.add_child(a)
a.add_child(b)
b.add_child(c)
c.add_child(b)
c.add_child(g)
g.add_child(c)

g1 = ds.Graph(s, list(), list())

goal = g1.depth_first_search()

print("\t\tDFS Tree:")
for node in g1.tree_draw_sequence:
    print(node, node.parent, node.tree_level)
print("\n")
for node in g1.tree_visit_sequence:
    print(node, node.parent, node.tree_level)

print("\n")
print("\n")
print("\t\tBFS Tree:")
# goal = g1.breadth_first_search()
# for node in g1.tree_draw_sequence:
#     print(node, node.parent, node.tree_level)
print("\n")
# for node in g1.tree_visit_sequence:
#     print(node, node.parent, node.tree_level)
#
# for key, val in g1.tree_level_dictionary.items():
#     print(key, val)

# notes for usage
# graph.tree_level_dictionary is an attribute - returns a dictionary, each level is key to identify nodes in such level
# graph.tree_draw_sequence is sequence of visiting nodes on the tree
# graph.tree_visit_sequence is sequence of path of nodes LABELS! not nodes themselves, use goal.get_path() instead
# graph.parent_dictionary is a dictionary - keys are nodes that represent parents - values are nodes inside them


# for key, val in g1.parent_dictionary.items():
#     print("Key: {} --- \n\t Val: {}".format(key, val))

# print(g1.tree_level_dictionary)
x=len(g1.tree_level_dictionary)-1
# print(x)



# while  x>=1:
#     childrenList=[]
#     childrenList.append(g1.tree_level_dictionary[x][0])
#     for i in range(len(g1.tree_level_dictionary[x])-1):
#         node=g1.tree_level_dictionary[x][i+1]
#         if g1.parent_dictionary[node]==g1.parent_dictionary[childrenList[0]]:
#             childrenList.append(node)

parentLevelDict=dict()



y=len(g1.tree_level_dictionary)

while y>1:

    for i in range(len(g1.tree_level_dictionary[y])):
        # p = Tree(g1.tree_level_dictionary[y][i].get_label())
        node = g1.tree_level_dictionary[y][i]
        key = g1.tree_level_dictionary[y][i].get_parent()
        if parentLevelDict.get(key) == None:
            parentLevelDict[key] = []
            parentLevelDict[key].append(node)
        else:
            parentLevelDict[key].append(node)

    y=y-1



treeDict=dict()

y=len(g1.tree_level_dictionary)
while y>1:

    for i in range(len(g1.tree_level_dictionary[y])):

        node = g1.tree_level_dictionary[y][i]
        key = node.get_parent()
        if parentLevelDict.get(node) == None:

            p = Tree(node.get_label())
            treeDict[node]=[]
            treeDict[node].append(p)
        else:
            childList = []
            for k in range (len(parentLevelDict[node])):

                child=parentLevelDict[node][k]
                childList.append(treeDict[child][0])
                print(treeDict[child][0])

            print(node.get_label(), childList)
            n=Tree(node.get_label(),*childList)
            treeDict[node]=[]
            treeDict[node].append(n)


    y=y-1

y=len(g1.tree_level_dictionary[1])
print('----------------------------------------------------------')
while y>0:

    for i in range(len(g1.tree_level_dictionary[y])):

        node = g1.tree_level_dictionary[y][i]
        key = node.get_parent()
        if parentLevelDict.get(node) == None:

            p = Tree(node.get_label())
            treeDict[node]=[]
            treeDict[node].append(p)
        else:
            childList = []
            for k in range (len(parentLevelDict[node])):

                child=parentLevelDict[node][k]
                childList.append(treeDict[child][0])
                print(treeDict[child][0])

            print(node.get_label(), childList)
            n=Tree(node.get_label(),*childList)
            treeDict[node]=[]
            treeDict[node].append(n)


    y=y-1

y=1

node = g1.tree_level_dictionary[y][0]
key = node.get_parent()
# if parentLevelDict.get(node) == None:
#
#     p = Tree(node.get_label())
#     treeDict[node]=[]
#     treeDict[node].append(p)
print('heloooooo')
childList = []
for k in range (len(g1.tree_level_dictionary[y])-1):

    child=g1.tree_level_dictionary[y][k+1]
    childList.append(treeDict[child][0])
    print(treeDict[child][0])

print(node.get_label(), childList)
n=Tree(node.get_label(),*childList)
treeDict[node]=[]
treeDict[node].append(n)
print('---------------------------------')

bucTree= buchheim(n)
# print(bucTree)
# print(bucTree.children)
# print(bucTree.children[0].children)
# print(bucTree.children[1].children)
# print(bucTree.children[1].children[1].children)
# print(bucTree.children[1].children[1].children[0].children)


# print(bucTree.children.x)
p=bucTree
for i in range(len(p.children)):

    c=p.children[i]
    print(c.tree," :",c.x)


# ToDo
def indicateCoords(pChildren):
    for i in range(len(pChildren)):
        if pChildren[i].children==None:
            print(pChildren[i].x)
            return
        indicateCoords(pChildren[i].children)


print(indicateCoords(p.children))







# print(treeDict)
# print(g1.tree_level_dictionary[3][0].get_label())
# print(g1.tree_level_dictionary[3][1].get_label())
# print(g1.tree_level_dictionary[3][2].get_label())
# print(g1.tree_level_dictionary[3][3].get_label())

# print(parentLevelDict[g1.tree_level_dictionary[3][0]][2].get_label())


# print(g1.tree_level_dictionary)
# node = g1.tree_level_dictionary[y-1][0]




# print(g1.tree_level_dictionary[3][0].get_label())

# print(g1.parent_dictionary[g1.tree_level_dictionary[y-1][0].get_parent()])

# print(g1.parent_dictionary)
# print(g1.tree_level_dictionary[y-1][0].get_parent())
# print(g1.tree_level_dictionary[4][0])

# print(g1.parent_dictionary)
# print(g1.tree_level_dictionary)
#
# print(g1.tree_level_dictionary[4][0].get_parent())