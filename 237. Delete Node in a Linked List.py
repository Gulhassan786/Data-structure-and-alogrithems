"""  Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list."""

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_start (self, value):
        node = Node(value, self.head)
        self.head = node
        return self.head
    
    def insert_end(self, value):
        if self.head == None:
            self.head = Node(value,None)
            return 
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(value, None)
        return iterator
    
    def get_lenght (self):
        counter = 0
        iterator = self.head
        while iterator:
            counter += 1
            iterator = iterator.next
        print(counter)
        
    def Insert_at (self, value, index):
        if index == 0 or index <= self.get_length:
            raise Exception ("Invalid Index is givin")
        if index == 0:
            self.Insert_start(value)
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index-1:
                node = Node(value, terator.next)
                iterator.next = node
                break
            iterator = iterator.next
            counter += 1
    
    def delet_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception ("Invalid Index")
        if index == 0:
            self.head = self.head.next
        counter = 0
        iterator = self.head
        while iterator:
            if counter == index - 1:
                iterator.next = iterator.next.next 
            iterator = iterator.next 
            counter +=1
            
    def del_node_val (self, node):
        node.value = node.next.value
        to_del = node.next
        node.next = node.next.next
        del(to_del)
        
    def show(self):
            iterator = self.head
            string = ''
            while iterator:
                string += str(iterator.value)+'---> '
                iterator = iterator.next 
            print(string)
          
linkedList = LinkedList()
linkedList.insert_start(1)
linkedList.insert_start(2)
node = linkedList.insert_start(3)
linkedList.insert_start(4)
linkedList.show()
linkedList.del_node_val(node)
linkedList.show()
