import DataStructure as ds
from naryTree import Tree
from buchheim import buchheim
from treeDemo import trees
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
c.add_child(c)
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
goal = g1.breadth_first_search()
for node in g1.tree_draw_sequence:
    print(node, node.parent, node.tree_level)
print("\n")
for node in g1.tree_visit_sequence:
    print(node, node.parent, node.tree_level)

for key, val in g1.tree_level_dictionary.items():
    print(key, val)

# notes for usage
# graph.tree_level_dictionary is an attribute - returns a dictionary, each level is key to identify nodes in such level
# graph.tree_draw_sequence is sequence of visiting nodes on the tree
# graph.tree_visit_sequence is sequence of path of nodes LABELS! not nodes themselves, use goal.get_path() instead
# graph.parent_dictionary is a dictionary - keys are nodes that represent parents - values are nodes inside them
for key, val in g1.parent_dictionary.items():
    for node in val:
        print("Key: {} -- node: {}".format(key, node))


# for key, val in g1.parent_dictionary.items():
#     print("Key: {} --- \n\t Val: {}".format(key, val))

# print(g1.tree_level_dictionary)
x=len(g1.tree_level_dictionary)-1
# print(x)




parentLevelDict=dict()

# bishoyToBucDict=dict()

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
            # bishoyToBucDict[node]=p
            treeDict[node]=[]
            treeDict[node].append(p)
        else:
            childList = []
            for k in range (len(parentLevelDict[node])):

                child=parentLevelDict[node][k]
                childList.append(treeDict[child][0])
                print(treeDict[child][0])

            print(node.get_label(), childList)
            theNewGeneratedTree=Tree(node.get_label(), *childList)
            treeDict[node]=[]
            treeDict[node].append(theNewGeneratedTree)


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
            theNewGeneratedTree=Tree(node.get_label(), *childList)

            # print(node.get_label(),'  : ',theNewGeneratedTree,'---------------09 ')
            treeDict[node]=[]
            treeDict[node].append(theNewGeneratedTree)


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
theNewGeneratedTree=Tree(node.get_label(), *childList)
# bishoyToBucDict[node]=theNewGeneratedTree
treeDict[node]=[]
treeDict[node].append(theNewGeneratedTree)
print('---------------------------------')

bucTree= buchheim(theNewGeneratedTree)
# print(bucTree.children[0].parent," hwa da")
# print(bucTree)
# print(bucTree.children)
# print(bucTree.children[0].children)
# print(bucTree.children[1].children)
# print(bucTree.children[1].children[1].children)
# print(bucTree.children[1].children[1].children[0].children)
# print(bucTree.children.x)
# p=bucTree


nodeToXcoordDict=dict()
levelToBucObjectDict=dict()
treeLevelNodeToBucNodeDict=dict()


levelToBucObjectDict[0]=[]
for key in g1.tree_level_dictionary:
    levelToBucObjectDict[key]=[]

print(levelToBucObjectDict,' levelbucdec')

# The x coordinate dict is useless

def generate_BucLevel_BucRow_Dict(bucNode):
    if (len(bucNode.children)==0):
        nodeToXcoordDict[bucNode]=bucNode.x
        levelToBucObjectDict[bucNode.y].append(bucNode)
        return
    else:
        for children in bucNode.children:
            generate_BucLevel_BucRow_Dict(children)
        nodeToXcoordDict[bucNode]=bucNode.x
        levelToBucObjectDict[bucNode.y].append(bucNode)

generate_BucLevel_BucRow_Dict(bucTree)

treeLevelNodeToBucNodeDict[g1.tree_level_dictionary[1][0]]=levelToBucObjectDict[0][0]
# print(treeLevelNodeToBucNodeDict)

# print(bucTree.y,'treeeeeeeeebuc')
# print(bucTree.children[0].y)
# print(bucTree.children[1].y)

for i in range(len(g1.tree_level_dictionary[1])-1):
    treeLevelNodeToBucNodeDict[g1.tree_level_dictionary[1][i+1]]=levelToBucObjectDict[1][i]



y=len(g1.tree_level_dictionary)
while y>1:
    for i in range(len(g1.tree_level_dictionary[y])):
        treeLevelNodeToBucNodeDict[g1.tree_level_dictionary[y][i]]=levelToBucObjectDict[y][i]

    y=y-1

treeSequence=g1.tree_draw_sequence




# print('seqqqqqq')
# print(treeSequence)
# print(treeLevelNodeToBucNodeDict)
# for key in treeLevelNodeToBucNodeDict:
#     print(treeLevelNodeToBucNodeDict[key].tree," : ",key.get_label())
#



# print(g1.tree_level_dictionary)
# print(len(g1.tree_level_dictionary[1]) - 1 == len(levelToBucObjectDict[1]))
# print(treeLevelNodeToBucNodeDict)
# print(bucTree.children[0].children[0].x)
# print(bucTree.children[0].children[1].x)
#
# print(bucTree.children[1].children[0].x)
# print(bucTree.children[1].children[1].x)

#

# print('-------------------After calling the function')
# print(nodeToXcoordDict)

#
# print('level to buc node dict--------------------:')
# print(levelToBucObjectDict)
# # print(indicateCoords(p.children))
# # print(treeDict)
# # print(g1.tree_level_dictionary[3][0].get_label())
# # print(g1.tree_level_dictionary[3][1].get_label())
# # print(g1.tree_level_dictionary[3][2].get_label())
# # print(g1.tree_level_dictionary[3][3].get_label())
# # print(parentLevelDict[g1.tree_level_dictionary[3][0]][2].get_label())
# # print(g1.tree_level_dictionary)
# # node = g1.tree_level_dictionary[y-1][0]
#
#
#
#
# # print(g1.tree_level_dictionary[3][0].get_label())
#
# # print(g1.parent_dictionary[g1.tree_level_dictionary[y-1][0].get_parent()])
#
# # print(g1.parent_dictionary)
# # print(g1.tree_level_dictionary[y-1][0].get_parent())
# # print(g1.tree_level_dictionary[4][0])
#
# # print(g1.parent_dictionary)
# # print(g1.tree_level_dictionary)
# #
# # print(g1.tree_level_dictionary[4][0].get_parent())
# print(levelToBucObjectDict[0][0].tree)
# print(levelToBucObjectDict[1][0].tree)
# print(g1.tree_level_dictionary[1][1].get_label())
#
# print('----------')
#
# print(levelToBucObjectDict[1][1].tree)
# print(g1.tree_level_dictionary[1][2].get_label())
