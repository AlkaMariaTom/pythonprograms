class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)

            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data, None)

    def get_positions(self):
        positions = []
        itr = self.head
        index = 0

        while itr:
            positions.append((index, itr.data))  # Append a tuple (index, data)
            itr = itr.next  # Move to the next node
            index += 1  # Increment the index

        return positions
    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count = count + 1
            itr=itr.next
        return  count


if __name__ == '__main__':
    ll = LinkedList()
    #ll.insert_at_begining("banana")
    #ll.insert_at_begining(5)
    #ll.insert_at_begining(89)
    #ll.insert_at_end(100)
    ll.insert_values(["Apple","Orange","Banana"])
    ll.print()
    print("Length of string:",ll.get_length())
    positions = ll.get_positions()
    print(positions)
