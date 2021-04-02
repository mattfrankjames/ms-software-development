#mark as private since this class is just used for internal programs
class _DoublyLinkedBase:
  class _Node:

    def __init__(self, element, prev, next):
      self._element = element
      self._prev = prev
      self._next = next

  def __init__(self):
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    # trailer comes after header and we're initializing the object to a length of 0
    self._header._next = self._trailer
    # header comes after trailer as we're initializing to a length of 0 with a circular array pattern
    self._trailer._prev = self._header
    self._size = 0

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def _insert_between(self, el, predecessor, successor):
    newest = self._Node(el, predecessor, successor)
    predecessor._next = newest
    successor._prev = newest
    self._size += 1 # increment the size of the list by one
    return newest

  def _delete_node(self, node):
    predecessor = node._prev
    successor = node._next
    # make sure to point the reference from the preceding element of what's being removed to the following element and vice versa
    predecessor._next = successor
    successor._prev = predecessor
    # decrement the size of the list by one
    self._size -= 1
    element = node._element
    node._prev = node._next = node._element = None #set all related references involving the element to none
    return element #return the deleted element

class LinkedDeque(_DoublyLinkedBase):
  def first(self):
    if self.is_empty():
      raise Empty('Deque is empty')
    else:
      return self._header._next._element
  def last(self):
    if self.is_empty():
      raise Empty('Deque is empty')
    else:
      return self._trailer._prev._element
  def insert_first(self, el):
    # the header comes before the element and _header._next is the first physical element
    self._insert_between(el, self._header, self._header._next)

  def insert_last(self, el):
    # the trailer comes after the last element, so inserting before that and the _prev (last physical element), adds this to the end of the list
    self._insert_between(el, self._trailer._prev, self._trailer)
  def delete_first(self):
    if self.is_empty():
      raise Empty('Deque is empty')
    else:
      return self._delete_node(self._header._next)
  def delete_last(self):
    if self.is_empty():
      raise Empty('Deque is empty')
    else:
      return self._delete_node(self._trailer._prev)

d = LinkedDeque()
d.insert_last(42)
d.insert_last(51)
d.insert_first(32)
print(d.__len__())
d.delete_first()
print(d.__len__())
d.insert_first(15)
d.insert_first(99)
d.insert_last(33)
print(d.__len__())
d.delete_last()
print(d.__len__())