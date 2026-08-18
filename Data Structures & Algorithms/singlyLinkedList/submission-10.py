class LinkedList:
    
    def __init__(self):
        self.head = Node(-1) #start with dummy node
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.value
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        return_list = []
        cur = self.head.next
        while cur:
            return_list.append(cur.value)
            cur = cur.next
        return return_list
        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None