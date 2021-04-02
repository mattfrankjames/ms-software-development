class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self._data = []
    self.head = None

  def __len__(self):
    return len(self._data)
  # Check to see if there's a head. If there isn't, the stack is empty
  def is_empty(self):
    if self.head == None:
      return True
    else:
      return False

  # Add a node to the start of the stack
  def push(self, data):
    if self.head == None:
      self.head = Node(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  # remove the current head node
  def pop(self):
    if self.is_empty():
      return None
    else:
      node_to_remove = self.head
      # Set the head to the next node
      self.head = self.head.next
      node_to_remove.next = None
      return node_to_remove.data

  # get the contents of the head without removing it
  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.head.data
  #return the size of the stack
  def size(self):
    return self.__len__()


new_stack = Stack()

new_stack.push(11)
new_stack.push(22)
new_stack.push(33)
new_stack.push(44)

# Print top element of stack
print(new_stack.peek())
print(new_stack.is_empty())
# Delete top elements of stack
new_stack.pop()
new_stack.pop()
print(new_stack.is_empty())

