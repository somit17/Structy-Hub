class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
      
  def insert(self, val):

    self.list.append(val)

    #sift-up
    self.sift_up(len(self.list) - 1)


  def swap(self,idx1,idx2):
    self.list[idx2],self.list[idx1] = self.list[idx1],self.list[idx2]

  def sift_up(self,idx):
    current_idx = idx
    while current_idx > 0:
      parent_idx = (current_idx - 1) // 2
      if self.list[current_idx] < self.list[parent_idx]:
        #swap
        self.swap(current_idx,parent_idx)
        current_idx = parent_idx
      else:
        break

  

    
    