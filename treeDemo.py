from naryTree import Tree


treeList=dict()
treeList[3]=[]
treeList[2]=[]
treeList[1]=[]


treeList[3].append(Tree('6'))
treeList[3].append(Tree('7'))

treeList[2].append(Tree('4'))
treeList[2].append(Tree('5'))

# treeList[1].append(treeList[2][0])
# treeList[1].append(treeList[3][0])

treeList[1].append(Tree('2',*treeList[2]))
treeList[1].append(Tree('3',*treeList[3]))


trees = [
#0 simple test
Tree("root",
     Tree("l"),
     Tree("r")),

#1 deep left
Tree("root",
  Tree("l1",
    Tree("l2",
      Tree("l3",
        Tree("l4")))),
  Tree("r1")),

#2 deep right
Tree("root",
  Tree("l1"),
  Tree("r1",
    Tree("r2",
      Tree("r3",
        Tree("r4"))))
  ),

#3 tight right
Tree("root",
  Tree("l1",
    Tree("l2",
      Tree("l3"), Tree("l4"))),
  Tree("r1",
    Tree("rl1"),
    Tree("rr1",
      Tree("rr2"), Tree("rr3")))),

#4 unbalanced
Tree("root",
  Tree("l1",
    Tree("l2",
      Tree("l3",
        Tree("l4",
          Tree("l5"),
          Tree("l6")),
        Tree("l7")),
      Tree("l8")),
    Tree("l9")),
  Tree("r1",
    Tree("r2",
      Tree("r3"),
      Tree("r4")),
    Tree("r5"))),

#5 Wetherell-Shannon Tree
Tree("root",
  Tree("l1",
    Tree("ll1"),
    Tree("lr1",
      Tree("lrl"),
      Tree("lrr"))),
  Tree("r1",
    Tree("rr2",
      Tree("rr3",
        Tree("rrl",
          Tree("rrll",
            Tree("rrlll"),
            Tree("rrllr")),
          Tree("rrlr")))))),

#6 Buchheim Failure
Tree("root",
  Tree("l",
    Tree("ll"),
      Tree("lr")),
  Tree("r",
    Tree("rl"),
    Tree("rr"))),

#7 simple n-ary
Tree("root",
  Tree("l"),
  Tree("m"),
  Tree("r")),

#8 buchheim n-ary tree
#this works perfectly.
Tree("root",
  Tree("bigleft",
    Tree("l1"),
    Tree("l2"),
    Tree("l3"),
    Tree("l4"),
    Tree("l5"),
    Tree("l6"),
    Tree("l7", Tree("ll1"))),
  Tree("m1"),
  Tree("m2"),
  Tree("m3", Tree("m31")),
  Tree("m4"),
  Tree("bigright",
    Tree("brr",
      Tree("br1"),
      Tree("br2"),
      Tree("br3"),
      Tree("br4"),
      Tree("br5"),
      Tree("br6"),
      Tree("br7")))),

#9 random tree from http://www.brpreiss.com/books/opus5/html/page257.html
# so... the "tree to the right thing" is actually a bug
Tree("root",
  Tree("E",
    Tree("F",
      Tree("F1"),
      Tree("F2"),
      Tree("F3")),
    Tree("E2"),
    Tree("E3")),
  Tree("G",
    Tree("H",
      Tree("I",
        Tree("I1"),
        Tree("I2"),
        Tree("I3")),
      Tree("H2"),
      Tree("H3")),
    Tree("J",
      Tree("K",
        Tree("K1"),
        Tree("K2"),
        Tree("K3")),
      Tree("L",
        Tree("L1"),
        Tree("L2"),
        Tree("L3")),
      Tree("J3")),
    Tree("M",
      Tree("M1"),
      Tree("M2"),
      Tree("M3"))),
  Tree("D3")),

#10 big tree for testing
Tree("t",
  Tree("rr",
    Tree("rr1",
      Tree("yy",
        Tree("ab"), Tree("bc")),
      Tree("zz",
        Tree("a"),
        Tree("b",
          Tree("c"),
          Tree("d",
            Tree("e"),
            Tree("f",
              Tree("g"),
              Tree("h",
                Tree("i"))))))),
    Tree("rr2", Tree("rr22"))),
  Tree("root",
    Tree("l1",
      Tree("ll1"),
      Tree("lr1",
        Tree("lrl"),
        Tree("lrr"))),
    Tree("r1",
      Tree("rr2",
        Tree("rr3",
          Tree("rrl",
            Tree("rrll",
              Tree("rrlll",
                Tree("98"), Tree("99")),
              Tree("rrllr")),
            Tree("rrlr"))))))),

#11
Tree('1',
     Tree('2',
          Tree('4'),
          Tree('5')),

     Tree('3',
          Tree('6'),
          Tree('7'))
     ),
  #12
Tree('1',
     *treeList[1]
     ),

]




# t=treeList[11]

# print(treeList[11])