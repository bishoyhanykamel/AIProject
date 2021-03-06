import os


class Tree:
    def __init__(self, node="", *children):
        self.node = node
        self.width = len(str(node))
        if children:
            self.children = children
        else:
            self.children = []

    def __str__(self):
        return "%s" % (self.node)

    def __repr__(self):
        return "%s" % (self.node)

    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, slice):
            return self.children[key]
        if isinstance(key, str):
            for child in self.children:
                if child.node == key: return child

    def __iter__(self):
        return self.children.__iter__()

    def __len__(self):
        return len(self.children)


def gentree(path):
    root = Tree(os.path.basename(path))
    if os.path.isdir(path):
        for f in os.listdir(path):
            root.children.append(gentree(os.path.join(path, f)))
    return root

joe = Tree('1',2,3)
joe2=Tree('2',4,5)
joe3=Tree('3',6,7)
# print(joe.children)
# print(joe2.children)
# print(joe3.children)