class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        if(self.head == None):
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            curr_node = self.head
            while(curr_node.next != None):
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
            new_node.next = None
    
    def listprint(self):
        vals = []
        curr_node = self.head
        while curr_node.next !=None:
            curr_node = curr_node.next
            vals.append(curr_node.data)
        print (vals)

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.listprint()