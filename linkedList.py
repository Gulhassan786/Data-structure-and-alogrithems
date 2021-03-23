class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
class linkedList:
    def __init__(self):
        self.head = None
    
    def insert_start(self, value):
        node = Node(value, self.head)
        self.head = node
    
    def insert_end(self, value):
        if self.head == None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)
    
    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter
    
    def remove_at (self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index ==0:
            self.head = self.head.next
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index-1:
                itr.next = itr.next.next
            itr = itr.next 
            counter +=1
    
    def insert_at( self, value, index):
        if index <0 or index >= self.get_length():
            raise Exception (" Invalid index is givin")
        if index == 0:
            self.insert_start(value)    
        counter = 0
        itr = self.head
        while itr:
            if counter == index-1:
                node = Node( value , itr.next)
                itr.next = node
                break
            itr = itr.next
            counter +=1

    def show (self):
        if self.head == None:
            print("Head is None")
        itr = self.head
        lis = []
        while itr:
             lis.append(itr.data)
             itr = itr.next
        print(lis)
      
        
linked_list = linkedList() # Creating the object of linkeList class
linked_list.insert_start(1) # Inserting the value in linkedlist by calling funciton
linked_list.insert_start(0)
linked_list.insert_end(4)
linked_list.insert_end(5)
# linked_list.remove_at(1)
linked_list.insert_at(100,1)
print(linked_list.get_length())
linked_list.show()
