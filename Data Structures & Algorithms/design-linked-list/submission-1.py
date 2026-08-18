class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        new_node = ListNode(val)
        self.head.next = new_node
        new_node.next = temp
        new_node.prev = self.head
        temp.prev = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        temp = self.tail.prev
        new_node = ListNode(val)
        self.tail.prev = new_node
        new_node.prev = temp
        new_node.next = self.tail
        temp.next = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if index > self.size:
            return None
        elif index == self.size:
            temp = self.tail.prev
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = temp
            temp.next = new_node
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            temp = curr.next
            new_node = ListNode(val)
            curr.next = new_node
            new_node.next = temp
            new_node.prev = curr
            temp.prev = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        temp = curr
        curr = curr.next
        curr.prev = temp
        self.size -= 1


class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)