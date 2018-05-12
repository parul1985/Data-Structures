# list-based queue implementation (FIFO)

# Implementation
class queue_imp:
    def __init__(self):
        self.queueList = []

    def printcontent(self):
        if (len(self.queueList) >= 1):
                print (self.queueList[len(self.queueList)-1])
        else:
            print('Queue is empty')

    def enque(self,item):
        self.queueList.append(item)

    def deque(self):
        if (len(self.queueList)>=1):
            self.queueList.pop(0)
        else:
            print('Queue is empty')


#API
que_object = queue_imp()
que_object.enque(2)
que_object.enque(4)
que_object.printcontent()
que_object.deque()
que_object.printcontent()
que_object.deque()