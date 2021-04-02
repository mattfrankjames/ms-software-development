class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Dequeue:
  def __init__(self):
    self.front = self.rear = None
  def is_empty(self):
    return self.front == None

  # add an item to the rear of dequeue
  def addRear(self, item):
    temp = Node(item)

    if self.rear == None:
      self.front = self.rear = temp
      return
    else:
      self.rear.next = temp
      self.rear = temp
  # add an item to the front of dequeue
  def addFront(self, item):
    temp = Node(item)

    if self.front== None:
      self.rear = self.front = temp
      return
    else:
      self.front.next = temp
      self.front = temp

    # remove and item from the front of the  dequeue
  def removeFront(self):
    if self.is_empty():
      return
    temp = self.front
    self.front = temp.next

    if(self.front == None):
      self.rear = None
  def removeRear(self):
    if self.is_empty():
      return
    temp = self.rear
    self.rear = temp.next

    if(self.rear == None):
      self.front = None
d = Dequeue()
d.addRear(42)
d.addRear(51)
d.addFront(32)
print('front is:' + str(d.front.data))
d.removeFront()
d.addFront(15)
d.addFront(99)
d.addRear(33)
print('rear is:' + str(d.rear.data))
d.removeRear()