class Node ():
    def __init__(self,value,prev=None):
        self.value = value
        self.next = None
        self.prev = prev

class Dll():
    def __init__(self,prev,value,start):
        newnode = Node()
        self.prev = None
        self.value = value
        self.start = start
        self.length = 0

    def insert_first(self):
        new_node = Node()
        temp = self.start
        if self.length == 0:
            temp = new_node
            self.prev = None
        else :
            temp = new_node
            self.prev = new_node.next 

        self.length +=1

    def is_empty(self):
        if self.length == 0 or self.start == None: 
            return ("Empty")
        else:
            return("Not empty")   
    
    def 