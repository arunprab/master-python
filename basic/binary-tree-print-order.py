#Class Node

class Node:
    
    def __init__ (self,value):
        self.key  = value
        self.left  = None
        self.right = None
        

def print_inorder(temp):
    
    if (not temp):
        return
    
    print_inorder(temp.left)
    print(temp.key)
    print_inorder(temp.right)
    
def print_preorder(temp):
    if (not temp):
        return
    
    print(temp.key)
    print_preorder(temp.left)
    print_preorder(temp.right)
    
def print_postorder(temp):
    if (not temp):
        return
    
    print_postorder(temp.left)
    print_postorder(temp.right)
    print(temp.key)


#Driver Code

root = Node(10)

root.left  = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.right = Node(8)
root.right.left  =  Node(15)


#Print Tree (Inorder)
print_inorder(root)
print("\n")

#Print Tree (Pre-order)
print_preorder(root)
print("\n")

#Print Tree (Post-order)
print_postorder(root)
print("\n")


        
