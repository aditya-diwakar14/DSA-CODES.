class Node():
    def __init__(self,item):# HERE None is added for the case if node is empty
        self.item = item
        self.next = None

class Sll():
    def __init__(self,item):
        node = Node(item)
        self.start = None
        self.tail = None
        self.length = 0


    def is_empty(self):      
        if self.length == 0:
            print("Empty Singly Linked List")
            return None
        else:
            print("Not empty")

    def insert_at_start(self,item):
        newNode = Node(item)
        if self.length ==0:
            self.start = newNode
            self.tail = newNode
        else:
            self.start = newNode.next
            

        self.length +=1

    def insert_at_end(self):
        if self.length == 0 :
            self.start=Node()            
            self.tail=Node()
        else:
            self.tail.next = self.tail
            self.start = self.start

        self.length +=1

    def search(self,item):
        temp = self.start
        while temp is not None:
            if temp.item == item:
                return temp
            temp = temp.next
        return None    