from collections import deque


class Node:
    def __init__(self,racine):
        self.racine = racine
        self.left = None
        self.right = None
        
def prefix(root):
    if root :
        print(root.racine, end="")
        prefix(root.left)
        prefix(root.right)
            
def postfix(root):
    if root :
        postfix(root.left)
        postfix(root.right)
        print(root.racine, end=" ")
        
def infix(root):
    if root:
        infix(root.left)
        print(root.racine, end=" ")
        infix(root.right)
        
def parcours_en_largeur(root):
    if not root:
        return 
    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        print(node.racine, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Pre-order traversal: \n", )
prefix(root)
print("post-order traversal: \n")
postfix(root)
print('in-order traversal: \n')
infix(root)
print('parcour en largeur')
parcours_en_largeur(root)