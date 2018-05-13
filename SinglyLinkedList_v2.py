# Queue Singly Linked List implementation
# FIFO

class Node:
    def __init__(self):
        self.data = 0
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self,data):
        newNode = Node()
        newNode.nextNode = self.head
        newNode.data = data
        self.head = newNode
        self.size = self.size +1

    def deleteNode(self):
        currpointer = self.head
        nextpointer = currpointer.nextNode


        while nextpointer.nextNode:
            currpointer = nextpointer
            nextpointer = nextpointer.nextNode
        currpointer.nextNode = None
        self.size = self.size - 1


    def printLL(self):
        nextpointer = self.head
        while nextpointer:
            print(nextpointer.data)
            nextpointer = nextpointer.nextNode


#API
newList = LinkedList()
newList.addNode(2)
newList.addNode(4)
newList.addNode(8)
newList.addNode(16)
newList.printLL()
#print(newList.head.data)
newList.deleteNode()
#print(newList.head)
newList.printLL()