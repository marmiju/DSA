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
    
    def pop(self) :
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next) :
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length ==0 :
            self.head =None
            self.tail =None
        return temp.value




#===================
my_linkedList = LinkedList(10)
my_linkedList.append(4)
my_linkedList.append(6)
my_linkedList.append(4)
my_linkedList.append(7)
my_linkedList.print_list()
temp = my_linkedList.pop()
my_linkedList.print_list()
print(f'temt: {temp}')

