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


    # preorder traversal; also prints null pointer as children for each node who does not have children
    def get(self):
        currNode = self.root
        print(currNode.value)
        self._get(currNode.leftchild)
        self._get(currNode.rightchild)

    def _get(self, currNode): #private function
        if currNode is not None:
            print(currNode.value)
            if currNode.leftchild is not None:
                self._get(currNode.leftchild)
            else:
                print('Null pointer')
            if currNode.rightchild is not None:
                self._get(currNode.rightchild)
            else:
                print('Null pointer')





#main()
h = BST()
h.put(3,"red")
h.put(4,"blue")
h.put(6,"yellow")
h.put(2,"at")
h.get()