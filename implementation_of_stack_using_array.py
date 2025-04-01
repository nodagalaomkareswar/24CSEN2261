# Create a stack with given capacity
class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.top = -1
        self.a = [0] * cap

    def push(self, x):
        if self.top >= self.cap - 1:
            print("Stack Overflow")
            return False
        self.top += 1
        self.a[self.top] = x
        return True

    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
            return 0
        popped = self.a[self.top]
        self.top -= 1
        return popped

    def peek(self):
        if self.top < 0:
            print("Stack is Empty")
            return 0
        return self.a[self.top]

    def is_empty(self):
        return self.top < 0

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
print(s.pop(), "popped from stack")

print("Top element is:", s.peek())

print("Elements present in stack:", end=" ")
while not s.is_empty():
    print(s.peek(), end=" ")
    s.pop()

OUTPUT:
30 popped from stack
Top element is: 20
Elements present in stack: 20 10 
