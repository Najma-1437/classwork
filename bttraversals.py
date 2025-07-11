
class TreeNode:
     def __init__(self,value):
         # None is a placeholder for an object
         # value acts as a parent node
         self.left = None# left and right are pointers
         self.right = None
         self.value = value
         pass
     def insert(self,qvalue):
         #check if it is greater or equal to the parent node

         if qvalue < self.value:
            if  self.left is None:
                self.left=TreeNode(qvalue) # insertion on the left side
            else:
                self.left.insert(qvalue)
         elif qvalue > self.value:# greater than the parent node
             if self.right is None:
                 self.right=TreeNode(qvalue)
             else: # traverse till
                 self.right.insert(qvalue)


     def find(self,qvalue):
         # return type is boolean
        if qvalue < self.value:

            if self.left is None:
                return False
            else:
                return self.left.find(qvalue)
        elif qvalue < self.value:
            if self.right is None:
                return False
            else:
              return self.right.find(qvalue)
        else:
            return True



     def preorder_traversal(self): # visiting a node for the fist time
       # print first before (50,11,12
         print(self.value)
         if self.left:  # will return a boolean value
             # print before
             # call the method recursively to deepen your search if not None
             self.left.preorder_traversal()

         if self.right:


             self.right.preorder_traversal()


     def inorder_traversal(self): # print when you pass by a node for the second time
         # checking if you're in the left subtree
          if  self.left: # will return a boolean value
               # call the method recursively to deepen your search if not None
              self.left.inorder_traversal()
          print(self.value)
          if self.right:
             self.right.inorder_traversal()






     def postorder_traversal(self):# visiting a node for the last time
         # checking if you're in the left subtree
         if self.left:  # will return a boolean value
             # call the method recursively to deepen your search if not None
             self.left.postorder_traversal()

         if self.right:
             self.right.postorder_traversal()
         print(self.value)



if __name__ == "__main__":
    objtree = TreeNode(50)  # parent node
    objtree.insert(11)
    objtree.insert(12)
    objtree.insert(13)
    objtree.insert(14)
    # now going to the right subtree

    objtree.insert(72)
    objtree.insert(62)
    objtree.insert(51)
    objtree.insert(67)

    objtree.preorder_traversal()
    # objtree.inorder_traversal()
    # objtree.postorder_traversal()

