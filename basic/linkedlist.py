#Class Node

class Node:
    
    def __init__ (self,value):
        self.data = value
        self.next = None
        

class CreateLinkedList:
    
    def __init__ (self):
        self.head = None
        
    def createnode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def printnode(self):
        
        temp = self.head
        while(temp):
            print(temp.data, end = "->")
            temp = temp.next
        
    def countnodes(self):
        
        cnt=0
        temp=self.head
        while(temp):
            cnt += 1
            temp = temp.next
            
        print("\nTotal #of Nodes added", cnt)
        
    def reverselist(self):
        
        curr = self.head
        prev = None
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev    
        


#Driver Code

ll = CreateLinkedList()

ll.createnode(1)
ll.createnode(5)
ll.createnode(9)
ll.createnode(10)
ll.createnode(14)
ll.createnode(20)

#Original Linked List
ll.printnode()
ll.countnodes()

#Reversed List
ll.reverselist()

#Display
ll.printnode()
ll.countnodes()
        
