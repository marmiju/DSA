from node import Node
class LinkedList :
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1

    def print_list(self):
        temp = self.head
        while temp is not None :
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail= new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
   
         
    
   




#===================
my_linkedList = LinkedList(10)
my_linkedList.append(4)
my_linkedList.append(6)
my_linkedList.append(4)
my_linkedList.append(7)
my_linkedList.print_list()

