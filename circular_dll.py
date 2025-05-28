class CircularListNode:
   def __init__(self,value):
# Storing the actual data or value in this node
       self.value= value
# 'next_node', is an attribute of type pointer that will point to the next node in the list
# Initially, when the node is created, we don't know the next node, so we set it to None, or null
       self.next_node=None
# Will also have 'previous_node', which is an attribute that  will point to the previous node in the list
# Initially, we set to None since Llist is empty at this point

       self.previous_node = None


class CircularDoublyLinkedList:
    def __init__(self):
        #We need to tell the compiler about the first chainlink, or the first node of our LList which is the head
        #Here in this code,  The 'head_node', attribute will be our head and it will keep track of the first node in the list (the head)
        # If the list is empty, 'head_node' will be None

        self.head_node=None

# 1) Method to insert a new node with a given value  at the end of the circular doubly linked list.
    def insert_at_end(self,value):
        new_node = CircularListNode(value)
        # we have to check if the list is empty
        if self.head_node is None:
            #Since the list is empty, the new_node will be the only one in the list
            #Since it's a circular list, the node points to itself in the previous side and forward side
            new_node.next_node=new_node
            new_node.previous_node=new_node
            #now updating that the head_node is no longer none
            self.head_node=new_node #reassigns the variable of the head node which is none to point  the new node
        else:
        # now what if the list has contents?
        # now actually adding the last_node at the end
        # we access the last node using the previous pointer of the head node
    # chained attribute access or attribute chaining
    # Here it is : 'self.start_node.previous_node' means:
    #   - 'self.start_node' gives us the first node in the list
    #   - '.previous_node' accesses the node that comes before the start_node
    # You're navigating object references through chained attributes — essentially, following links (pointers) between objects.
   # In data structures (like linked lists), this is also described as:
    # 1.Pointer traversal in object-oriented programming.

    # 2. Link following in node-based structures.

    # So, self.start_node.previous_node is an example of pointer traversal via attribute chaining in a linked structure.
         last_node = self.head_node.previous_node # since the node before the hesd node is the last node
        # now linking the new_node into the list
        # First,  The current last_node's 'next_node' should point to the new_node
         last_node.next_node = new_node
        #Secondly, The new_node's 'previous_node' should point back to the last_node
         new_node.previous_node=last_node
        # Thirdly,  The new_node's 'next_node' should point to the head_node to maintain circularity
         new_node.next_node=self.head_node
        # lastly, The head_node's 'previous_node' should now point back to the new_node, which is the new last node
         self.head_node.previous_node=new_node
#2)Inserting a new node with the given 'value' at the beginning of a circular doubly linked list
    def insert_at_the_beginning(self,value):
        #To optimize our code, We are going reuse the insert_at_end method to add the node at the end first
        self.insert_at_end(value)
# After adding the new node at the end, we move the start_node pointer backward to the new node
        # Here is the mark_down;
        # - 'self.head_node' is currently the first node
        # - 'self.head_node.previous_node' is the node just added at the end
        # By setting head_node to head_node.previous_node, we simply make the new node the first node
        self.head_node = self.head_node.previous_node
#3) Removing a given valur from the linked list
    def removing_given_value(self,value):
        #Check if list is empty otherwise there's nothing to remove
        if self.head_node is None:
            print("The list is empty, Cannot remove any node.")
            return
        # If not, We start by traversing  from the head_node
        # current_node being a temporary variable used to help you traverse the linked list
        current_node = self.head_node
        # We will iterate through the LList until we come back to the head_node, since it's circularly linked list
        while True:
         if current_node.value== value:
        # We only enter this block if we find the node to remove

        # After finding the node to remove, there are a few cases we need to consider,

        # the first case is that the list has only one node (which is current_node)
        # case 1:
           if current_node.next_node==current_node:
            # Since it's the only node, removing it makes the list empty
              self.head_node = None
           else:
            # case 2:
            # The list has multiple nodes
            # So, inorder to remove current_node, we need to announce our intentions to our neighbours,
            # by updating the links of these neighbours
            # Remember the pointer traversal via attribute chaining, in as that 'current_node.previous_node.next_node = current_node.next_node' which basically implies,
            # -The node before current_node should now point forward to the node after current_node
                   current_node.previous_node.next_node = current_node.next_node

            # 'current_node.next_node.previous_node = current_node.previous_node' Implies that,
            #   - The node after current_node should now point backward to the node before current_node
                   current_node.next_node.previous_node = current_node.previous_node
            # If we are removing the start_node, move the start_node pointer forward

                   if current_node == self.head_node:
                        self.head_node = current_node.next_node

                # By this point, the Node is removed, and we can peacefully exit the method
           return
        # Moving to the next node in the list
         current_node = current_node.next_node
        # If we by any chance have looped back to the start_node, the value was not found
         if current_node == self.head_node:
            print(f" Value {value} not found in the list.")
            break


#4) Traversing and showing the list forward wise
    def show_list_forward(self):
        # start by checking if the list is empty
       if self.head_node is None:
           print('The list is empty. ')
           return
       # setting a temporary variable to help us traverse the list
       current_node = self.head_node
     # Then we Create an empty list to collect/ gather the string representations (which means we convert the sata part of the node to string) of node values
       values_list = []

     # Traverse through the LList until we come back to the start_node
       while True:
# Add the current node's value to the list as a string
          values_list.append(str(current_node.value)) #Here str() is an inbuilt method that converts a given value to a string

            # Then we do our incrementation here by utilizing the pointers
          current_node = current_node.next_node


# We then check a condition where we have completed a full circle, and if so, we MAKE A STOP
          if current_node == self.head_node:
             break
             # Doing a formatted output
        #Here's how to do it, We Join all the values in 'values_list' into a single string separated by ' -> '

        # Explanation of join inbuilt method:
        # - ' -> ' is a string separator
        # - '.join(values_list)' takes all elements in 'values_list' and concatenates them into one string,
        #   putting ' -> ' between each element
        # For example, if values_list = ['5', '10', '15'], the result will be '5 -> 10 -> 15'
          output_string = " -> ".join(values_list)

# Print the resulting string to show the list contents
          print(output_string)
#5) Traversing and showcasing the list backward
    def show_list_backward(self):
      # If the list is empty, print a message and exit the method via (return)
      if self.head_node is None:
          print("The list is empty.")
          return

      # Here, the last node is the one before the start_node (because the list is circular)
      last_node = self.head_node.previous_node
      # If you are wondering why not store a  self.last_node separately
      # It's because it adds redundancy and risks de-synchronization,
      # Instead,  we just access what we need through the links.

      # Now for the printing part, Start from the last node
      current_node = last_node

      # Create an empty list to collect the string representations of node values
      values_list = []

      # Traverse the list backward until we come back to the last_node
      while True:
          # Add the current node's value to the list as a string
          values_list.append(str(current_node.value))

          # Move to the previous node
          current_node = current_node.previous_node

          # Stop if we have completed a full circle
          if current_node == last_node:
              break

      # Join all the values in 'values_list' into a single string separated by ' <- '
      # - ' <- ' is our separator that now indicates backward direction
      # - '.join(values_list)' concatenates all elements in 'values_list' with ' <- ' between them
      # e.g  if values_list = ['30', '20', '10'], the result will be '30 <- 20 <- 10'

      output_string = " <- ".join(values_list)

      # Print the resulting string to show the list contents backward
      print(output_string)


if __name__ == "__main__":
    # Create a node by Instantiating that class via the creating of an object
    my_circular_list = CircularDoublyLinkedList()

    # Then insert values by calling the insertion method we created
    my_circular_list.insert_at_end("QUICK")
    my_circular_list.insert_at_end("BROWN")
    my_circular_list.insert_at_end("FOX")

    print("List after inserting at the end:")
    # Call the print forward method
    my_circular_list.show_list_forward()

    my_circular_list.insert_at_the_beginning("THE")
    print("List after inserting at the beginning:")
    my_circular_list.show_list_forward()

    print("List displayed backward:")
    my_circular_list.show_list_backward()

    my_circular_list.removing_given_value("QUICK")
    print("List after removing QUICK:")
    my_circular_list.show_list_forward()

    my_circular_list.removing_given_value("QUICK")  # Not found
    my_circular_list.removing_given_value("SLOW")  # Not found

    my_circular_list.removing_given_value("BROWN")
    print("List after removing BROWN:")
    my_circular_list.show_list_forward()

    # Attempting to empty the LList by removing the remining elements
    my_circular_list.removing_given_value("THE")
    my_circular_list.removing_given_value("FOX")
    print("List after removing all:")

    my_circular_list.show_list_forward()











