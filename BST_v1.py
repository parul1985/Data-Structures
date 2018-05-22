# binary search tree implementation


class TreeNode:
    def __init__(self,key,value,left=None,right=None,parent=None):
        self.leftchild=left
        self.rightchild=right
        self.parentnode=parent
        self.key=key
        self.value=value

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self,key,value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)


    def _put(self, key,value,currentNode):
        if key<currentNode.key:
            if currentNode.leftchild is None:
                newnode = TreeNode(key,value)
                newnode.parent = currentNode
                currentNode.leftchild = newnode
            else:
                self._put(key, value, currentNode.leftchild)

        if key>currentNode.key:
            if currentNode.rightchild is None:
                newnode = TreeNode(key,value)
                newnode.parent = currentNode
                currentNode.rightchild = newnode
            else:
                self._put(key, value, currentNode.rightchild)


    # preorder traversal
    def get(self):
        currNode = self.root
        while currNode is not None:
            print(currNode.value)
            currNode =  currNode.rightchild




#main()
h = BST()
h.put(3,"red")
h.put(5,"yellow")
h.get