# Max Heap problem discription
"""We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)"""
class Heap:
  def __init__(self):
    self.heap = []
    self.currentPosition = -1

  def insert(self, item):
    self.currentPosition = self.currentPosition + 1
    self.heap.append(item)
    self.heapifyUp(self.currentPosition)

  def heapifyUp(self, index):
    parentIndex = (index-1) // 2
    while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
      self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
      index = parentIndex
      parentIndex = (index-1) // 2

  def heapsort(self):
      for i in range(0, self.currentPosition+1):
          self.heap[0], self.heap[self.currentPosition -
                                  i] = self.heap[self.currentPosition-i], self.heap[0]
          self.heapifyDown(0, self.currentPosition-i-1)

  def heapifyDown(self, index, upto):
      while index <= upto:
          leftChild = 2*index+1
          rightChild = 2*index+2
          if leftChild < upto:
              childToSwap = None
              if rightChild > upto:
                  childToSwap = leftChild
              else:
                  if self.heap[leftChild] > self.heap[rightChild]:
                      childToSwap = leftChild
                  else:
                      childToSwap = rightChild
              if self.heap[index] < self.heap[childToSwap]:
                  self.heap[index], self.heap[childToSwap] = self.heap[childToSwap], self.heap[index]
              else:
                  break
              index = childToSwap
          else:
              break

  def Pop_Heap(self):
          self.heap[0], self.heap[self.currentPosition] = self.heap[self.currentPosition], self.heap[0]
          self.heap.pop(-1)
          self.currentPosition -= 1
          self.heapifyDown(0, self.currentPosition)

  def lastStoneWeight(self):
      first = 0
      second = 0
      while len(self.heap) > 1:
        first = self.heap[0]
        self.Pop_Heap()
        second = self.heap[0]
        self.Pop_Heap()
        if first-second > 0:
          self.insert(first-second)
      if len(self.heap) != 0:
        return self.heap[0]
      return 0


heap = Heap()
Stones = [2, 7, 4, 1, 8, 1]
for i in Stones:
  heap.insert(i)
print(heap.heap)
print(heap.lastStoneWeight())
