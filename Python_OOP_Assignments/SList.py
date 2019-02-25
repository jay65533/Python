class Node: 
    def __init__(self,val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def addNodeAtEnd(self,newval):
        NewNode = Node(newval)
        if(self.head is None):
            self.head = NewNode
            return
        runner = self.head
        while(runner.next):
            runner = runner.next
        runner.next = NewNode

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.val)
            printval = printval.next

list1 = SinglyLinkedList()
list1.head = Node(5)
list1.addNodeAtEnd(6)
list1.addNodeAtEnd(7)

list1.listprint()

