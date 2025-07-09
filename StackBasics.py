# A stack is a  data structure that uses the Last In, First Out  principle
# For example in a stack of clothes, you fold and put clothes on top(push)  and you take clothes from the top(pop).
# Basic Stack Operations
#Push: Add an element to the top of the stack
#Pop:Remove the top element from the stack
#Peek/Top: look at the top element but don't remove it
#Is Empty: check if the stack has any elements
# It can be implemented using an array/list or using a linked list
# We'll use list through Python's inbuilt method and since it supports .append() push() and pop() methods



stack = []
# creates an empty list to represent the stack

stack.append(10) # Adds 10 to the top of the stack
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

#Peek at the top element but don't remove it
top_element = stack[-1] # accesses the top element without removing it
print("Top element is: " ,top_element)

# check if the stack is empty
if len(stack) == 0:
    print("Stack is empty")
else :
    print("Stack is not empty")
class SimpleStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("STACK EMPTY")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack from bottom to top: ", self.items)
        return

if __name__ == "__main__":
    stack1 = SimpleStack()

    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)

    stack1.print_stack()

    print("Top element: ",stack1.peek())

    print("Popped: ",stack1.pop())

    print("Is stack empty?",stack1.is_empty())

    stack1.pop()
    stack1.pop()
    print("Is stack empty after popping?", stack1.is_empty())



