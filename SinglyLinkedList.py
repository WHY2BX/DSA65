class DataNode:
    def __init__(self, name=""):
        self.name = name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        if self.head != None:
            pointer = self.head
            while pointer != None:
                print("->", pointer.name, end=" ")
                pointer = pointer.next
            print("")
        else:
            print("This is an empty list")
        return
    def insertFront(self, name):
        pNew = DataNode(name)
        if self.head != None:
            pNew.next = self.head
            self.head = pNew
        else:
            self.head = pNew
        self.count += 1
        return
    def insertLast(self, name):
        pNew = DataNode(name)
        if self.head != None:
            pointer = self.head
            while pointer != None:
                pointer = pointer.next
                if pointer.next.next == None:
                    pointer.next.next = pNew
                    break
        else:
            self.head = pNew
        self.count += 1
        return

    def insertBefore(self, new, name):
        pNew = DataNode(new)
        pointer = self.head
        next_to = self.head.next
        if self.head == None:
            print('Cannot insert, ' + name + ' does not exist')
        elif pointer.name == name:
            pNew.next = self.head
            self.head = pNew
            return
        # print(next_to.name)
        while next_to.name != name:
            if next_to.next == None:
                print('Cannot insert, ' + name + ' does not exist')
                break
            else:
                pointer = pointer.next
                next_to = next_to.next
            # print(next_to.name)
        
        if next_to.name == name:
            pointer.next = pNew
            pNew.next = next_to
        # if next_to.name != name and next_to.next == None:
        #     print('Cannot insert, ' + name + ' does not exist')
        self.count += 1
        return

    def delete(self, name):
        pointer = self.head
        next_to = self.head.next
        if self.head == None:
            print('Cannot delete, ' + name + ' does not exist')

        elif pointer.name == name:
            self.head = next_to
            self.count -= 1
        while next_to.next != None:
            if next_to.name == name:
                pointer.next = next_to.next
                self.count -= 1
                break
            pointer = pointer.next
            next_to = next_to.next
            if next_to.next == None:
                print('Cannot delete, ' + name + ' does not exist')
                break
        return
        
    
mylist = SinglyLinkedList()
pNew = DataNode("John")
mylist.head = pNew

pNew = DataNode("Tony")
mylist.head.next = pNew
mylist.traverse()

mylist.insertFront("Bill")
mylist.traverse()

mylist.insertLast("Steve")
mylist.traverse()

mylist.insertBefore("Alex", "Bill")
mylist.traverse()

mylist.delete("z")
mylist.traverse()
