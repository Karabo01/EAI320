###Code here
#I'll try start bulding after my class test tomorrow. You can do some research about which dfs and bfs to use in python
# I still need to decide what kinda arrays I'll be using
# yeah I started with the research vele. I'll see if I can find any solid algorithms tomorrow 
# #and then we'll just decide which array would work best
# https://qvault.io/python/binary-search-tree-in-python/
play = ""
began= False
class Node(object):

    def __init__(self,character):
        self.character = character
        self.left = None
        self.center = None
        self.right = None
        self.parent= None
        self.full=0
        self.height=0


class RPS(object):

    def __init__(self):
        self.rootNode = None

    """The best president guy. This is the function that brought it all together. Inspired by the 
        great Vladimir Putin, this function is fast, efficient, and precise. No nonsense and get the job done"""

    def putin(self,levels):
        i=0
        j=0
        while(j<=levels ):
            i=0
            while(i<3**(levels-j)):

                if(self.rootNode==None):
                    self.rootNode = self.putItem(self.rootNode, "start")
                else:
                    self.rootNode = self.putItem(self.rootNode, "R")
                    self.rootNode = self.putItem(self.rootNode, "P")
                    self.rootNode = self.putItem(self.rootNode, "S")
                    i += 1
            j+=1

    """This function would serve to actually insert the relevant node at the opening.
        It will be used during the initialisation of the RPS tree."""

    def putItem(self, node,key):

        if node == None:
            node = Node(key)
            return node


        if(node.full==3):
            node=self.check(node,key)

        if(key=="R"):
            node.left = self.putItem(node.left, key)
            node.left.parent = node
            node.full += 1

        if (key == "P"):
            node.center = self.putItem(node.center, key)
            node.center.parent = node
            node.full += 1

        if (key == "S"):
            node.right = self.putItem(node.right, key)
            node.right.parent = node
            node.full += 1




        return self.rootNode

    """ Function to check whether the visited node and/or its kids is/are full(has three kids) 
        and choose which node will be appended by comparing the heights of the node"""

    def check(self, node, key):

        if (node.left.full < 3):
            return node.left
        elif (node.center.full < 3):
            return node.center
        elif (node.right.full < 3):
            return node.right
        else:
            if (rheight(node.left) > rheight(node.center)):
                return self.check(node.center,key)
            elif(rheight(node.center) > rheight(node.right)):
                return self.check(node.right,key)
            else:
                return self.check(node.left,key)




"""Function to print level order traversal of tree and will be
   the main Breadth First Search
"""

def printLevelOrder(root,began):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i,began)

""" Print nodes at a current level of the tree and is a helper function 
    to the printLevelOrder function which is used for the breadth first search"""

def printCurrentLevel(root, level, began):
    temp = root

    allParents = ""
    if root is None:
        return
    if level == 1:
        finished = root.character
        while temp.character != "start" and temp.parent.character != "start":
            allParents = allParents + temp.parent.character
            temp = temp.parent
        #finished = printP(root, play, began)
        print(allParents + root.character, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1, began)
        printCurrentLevel(root.center, level - 1, began)
        printCurrentLevel(root.right, level-1, began)

"""printP will be the function that recursively prints the parents of the current node
when using Depth First search. Nodes will be returned in post order"""
def printP(node, play):
    if node is None:
        return ""
    elif node.parent is None:
        return ""
    elif node.parent.character == "start":
        play += node.character
        return play
    else:
        play += printP(node.parent, play) + node.character
        return play

""" Compute the height of a tree after all three leaf nodes have been 
    inserted --the number of nodes along the longest path from the root 
    node down to the farthest RIGHT leaf of the node
"""

def rheight(node):
    Rheight=0
    if node is None:
        return 0
    else:
        while(node!=None):
            node=node.right
            Rheight+=1
        return Rheight

""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
        cheight = height(node.center)
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        elif(cheight>rheight):
            return cheight+1
        else:
            return rheight+1



def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        printPostorder(root.center)
        # the recur on right child
        printPostorder(root.right)
        print(printP(root.parent, "") + root.character)

        # now print the data of node

#Main is here
def main():

    levels=3
    print("Hello World!")
    tree = RPS()

    tree.putin(levels-1)
    print("tree has 3 levels")

# LETS SEE

    print("Level order traversal of binary tree is -")
    printLevelOrder(tree.rootNode,began)
    print("")
    printPostorder(tree.rootNode)
  #  tree.put("R")
   # tree.put("P")
   # tree.put("S")

if __name__ == "__main__":
    main()
 
