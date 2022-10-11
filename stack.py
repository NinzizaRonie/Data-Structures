#NUMBER 2


# The Node class that represent the nodes to be used in the stack.
class Node:
 def __init__(self, value, next_node=None):
  self.value = value
  self.next_node = next_node
 
 def set_next_node(self, next_node):
  self.next_node = next_node
 
 def get_next_node(self):
  return self.next_node
 
 def get_value(self):
  return self.value

# The Stack class for different functions to build the stack.
class Stack:
 def __init__(self, limit=1000):
  self.top_item = None
  self.size = 0
  self.limit = limit
 
# To add elements into our stack.
 def push(self, value):
  if self.has_space():
   item = Node(value)
   item.set_next_node(self.top_item)
   self.top_item = item

    # To increase the size of our stack to keep track.
   self.size += 1
  else:
    print(" out of space!")



# To remove elements from the stack.
 def pop(self):
  if not self.is_empty():
   item_to_remove = self.top_item
   self.top_item = item_to_remove.get_next_node()

 # To reduce the size of our stack to keep track.
   self.size -= 1
   return item_to_remove.get_value()

  else:
   print("This stack is totally empty.") 
   

# To view the first element in our stack. 
 def peek(self):
  if not self.is_empty():
   return self.top_item.get_value()
  else:
   print("Nothing to see here!")

 # To check if the stack has space left.
 def has_space(self):
  return self.limit > self.size
 
 def is_empty(self):
  return self.size == 0
