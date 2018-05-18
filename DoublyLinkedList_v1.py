# doubly linked list
# Each node has two pointers next and previous

class Node:
    def __init__(self):
        self.data = 0
        self.nextNode = None
        self.prevNode = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # adding first node
    def insertNode(self, item):
        newNode = Node()
        newNode.data = item
        newNode.nextNode = self.head
        newNode.prevNode = None
        if (self.size>=1):
            self.head.prevNode = newNode
        self.head = newNode
        self.size = self.size+1

    # deleting first node
    def deleteNode(self):
        if self.head is None:
            print("empty list")
        else:
            currpointer = self.head
            self.head = currpointer.nextNode
            self.head.prevNode = None
            self.size = self.size-1


    def printLL(self):
        if self.head is None:
            print("empty list")
        else:
            nextpointer = self.head
            while nextpointer:
                print(nextpointer.data)
                currpointer = nextpointer
                nextpointer = nextpointer.nextNode

            print('traversing in opposite direction')
            nextpointer = currpointer
            while nextpointer:
                 print(nextpointer.data)
                 nextpointer = nextpointer.prevNode


# API
myobject = doublyLinkedList()
myobject.insertNode(2)
myobject.insertNode(3)
myobject.insertNode(41)
myobject.printLL()
myobject.deleteNode()
myobject.deleteNode()
#myobject.deleteNode() --> gives error
myobject.printLL()
