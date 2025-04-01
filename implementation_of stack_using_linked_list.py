# python program to implement a stack using singly linked
# list

# Class representing a node in the linked list
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Class to implement stack using a singly linked list
class Stack:
    def __init__(self):

        # head of the linked list
        self.head = None

    # Function to check if the stack is empty
    def is_empty(self):

        # If head is None, the stack is empty
        return self.head is None

    # Function to push an element onto the stack
    def push(self, new_data):

        # Create a new node with given data
        new_node = Node(new_data)

        # Check if memory allocation for the new node failed
        if not new_node:
            print("\nStack Overflow")
            return

        # Link the new node to the current top node
        new_node.next = self.head

        # Update the top to the new node
        self.head = new_node

    # Function to remove the top element from the stack
    def pop(self):

        # Check for stack underflow
        if self.is_empty():
            print("\nStack Underflow")
        else:

            # Assign the current top to a temporary variable
            temp = self.head

            # Update the top to the next node
            self.head = self.head.next

            # Deallocate the memory of the old top node
            del temp

    # Function to return the top element of the stack
    def peek(self):

        # If stack is not empty, return the top element
        if not self.is_empty():
            return self.head.data
        else:
            print("\nStack is empty")
            return float('-inf')


# Creating a stack
st = Stack()

# Push elements onto the stack
st.push(11)
st.push(22)
st.push(33)
st.push(44)

# Print top element of the stack
print("Top element is", st.peek())

# removing two elemements from the top
print("Removing two elements...");
st.pop()
st.pop()

# Print top element of the stack
print("Top element is", st.peek())

OUTPUT:
Top element is 44
Removing two elements...
Top element is 22
