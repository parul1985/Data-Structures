# array-based stack implementation
class stack_impl:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def printcontent(self):
         return self.items[len(self.items)-1]


# Interface
obj = stack_impl()
obj.push(2)
obj.push(4)
a = obj.printcontent()
print(a)
obj.pop()
a = obj.printcontent()
print(a)
