class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    if self.head == None:
      print("test of length 0")
      return None
    elif self.head.get_next() == None:
      print("test of length 1")
      return self
    else:
      # This works for a list of length 2
      print("longer list test")
      print(self.head.value)
      left = None
      current = self.head
      right = self.head.get_next()
      while current:
        current.set_next(left)
        left = current
        current = right
        if right:
          right = current.get_next()
      self.head = left








    # # Make a solution LInked List
    # solution_list = LinkedList()
    # # read from self.head and make it the head of the new list, REPEAT 
    # node = Node()
    # while self.head != None:
    #   new_list_head = self.head.value
    #   solution_list.add_to_head(new_list_head)
    #   self.head = self.head.next_node
    # print("\n")
    # return solution_list


# example = LinkedList()
# example.add_to_head(4)
# example.add_to_head(3)
# example.add_to_head(2)
# example.add_to_head(1)


# # print the example so we can see it
# node = example.head
# while node:
#   print(node.value)
#   node = node.next_node

# reverse_example = example.reverse_list()   # which is solution_list in the method

# #print the reversed example
# node = reverse_example.head
# print("entering While to reverse...")
# while node:
#   #print("reversed...")
#   print(node.value)
#   node = node.next_node





