class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1 
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head;
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
