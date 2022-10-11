# our Node class.
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

# Implementing a queue
class Queue:

#constructor method
 def __init__(self, max_size=None):
  self.head = None
  self.tail = None
  self.max_size = max_size
  self.size = 0

#enqueue method 
 def enqueue(self, value):
  if self.has_space():
   item_to_add = Node(value)
   print("Adding " + str(item_to_add.get_value()) + " to the queue!")
  if self.is_empty():
   self.head = item_to_add
   self.tail = item_to_add
  else:
   self.tail.set_next_node(item_to_add)
   self.tail = item_to_add
   
   self.size += 1
 
 
 #dequeue method
 def dequeue(self):
   if not self.is_empty():
    item_to_remove = self.head
   print("Removing " + str(item_to_remove.get_value()) + " from the queue!") 

   if self.get_size() == 1:
    self.head = None
    self.tail = None
   else:
    self.head = self.head.get_next_node()
    self.size -= 1
    return item_to_remove.get_value()


 
# A method to help us view the first element in the queue.
def peek(self):
 if self.is_empty():
  print("Nothing to see here!")
 else:
  return self.head.get_value()
 # A method that returns the size of our queue.
 def get_size(self):
  return self.size
# A method that checks whether the queue has space .
 def has_space(self):
   if self.max_size == None:
    return True
   else:
    return self.max_size > self.get_size()
 
 def is_empty(self):
  return self.size == 0
6