from random import randrange

class BinHeap:
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0
  def percUp(self,i):
    while i // 2 > 0:
      if self.heapList[i] < self.heapList[i // 2]:
        tmp = self.heapList[i // 2]
        self.heapList[i // 2] = self.heapList[i]
        self.heapList[i] = tmp
      i = i // 2
  def insert(self,k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)
    return self.heapList
  def percDown(self,i):
    while (i * 2) <= self.currentSize:
      mc = self.minChild(i)
      if self.heapList[i] > self.heapList[mc]:
          tmp = self.heapList[i]
          self.heapList[i] = self.heapList[mc]
          self.heapList[mc] = tmp
      i = mc
  def minChild(self,i):
    if i * 2 + 1 > self.currentSize:
      return i * 2
    else:
        if self.heapList[i*2] < self.heapList[i*2+1]:
          return i * 2
        else:
          return i * 2 + 1
  def delMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize = self.currentSize - 1
    self.heapList.pop()
    self.percDown(1)
    return retval
  def buildHeap(self,alist):
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while (i > 0):
      self.percDown(i)
      i = i - 1
    return self.heapList
  def access_heap_list(self):
    return self.heapList;

heap_one = BinHeap()

rand_list = []

def generate_list():
  for i in range(1, 16):
    rand_list.append(randrange(1, 50))

def single_item_insert():
  heap_two = BinHeap()
  for i in range(len(rand_list)):
    BinHeap.insert(heap_two, rand_list[i])
  return heap_two.access_heap_list()
generate_list()

tree_with_list_arg = BinHeap.buildHeap(heap_one, rand_list)
tree_list_single = single_item_insert()

print(rand_list)

print(tree_with_list_arg)
print(tree_list_single)