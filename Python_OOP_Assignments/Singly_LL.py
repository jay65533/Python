class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__ (self):
        self.head = Node()

    def addVal (self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None: 
            curr = curr.next
        curr.next = new_node

    def listprint(self):
        vals = []
        curr_node = self.head
        while curr_node.next !=None:
            curr_node = curr_node.next
            vals.append(curr_node.data)
        print (vals)
    
    def removeVal(self, index):
        curr_index = 0
        curr_node = self.head
        while curr_node.next !=None:
            last_node = curr_node
            curr_node = curr_node.next
            if(curr_index == index):
                last_node.next = curr_node.next
                curr_node.next = None
                return
            curr_index = curr_index + 1

    def removeKthFromLast(self, index):
        count = 0
        curr_index = 0
        curr_node = self.head    
        while curr_node.next != None:
            curr_node = curr_node.next
            count = count + 1
        remove_index = count - index - 1
        curr_node = self.head
        while curr_node.next != None:
            last_node = curr_node
            curr_node = curr_node.next
            if(curr_index == remove_index):
                last_node.next = curr_node.next
                return
            curr_index = curr_index + 1
        
my_list = SinglyLinkedList()
my_list.addVal(1)
my_list.addVal(2)
my_list.addVal(3)
my_list.addVal(5)
my_list.listprint()
#my_list.removeVal(0)
my_list.removeVal(0)
#my_list.removeKthFromLast(1)
my_list.listprint()
