class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = self.rear = None
  def is_empty(self):
    return self.front == None

  # add an item to the queue (last in)
  def enqueue(self, item):
    temp = Node(item)

    if self.rear == None:
      self.front = self.rear = temp
      return
    else:
      self.rear.next = temp
      self.rear = temp

    # remove and item from the queue (first out)
  def dequeue(self):
    if self.is_empty():
      return
    temp = self.front
    self.front = temp.next

    if(self.front == None):
      self.rear = None
q = Queue()
q.enqueue(42)
q.enqueue(51)
q.enqueue(32)
q.dequeue()
q.enqueue(15)
q.enqueue(99)
q.enqueue(33)
q.dequeue()
print('front is:' + str(q.front.data))
print('rear is:' + str(q.rear.data))