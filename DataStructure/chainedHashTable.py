import linkedList

class ChainedHashTable:
    def __init__(self, n): # number of items
        # data, array
        self.item = 0
        self.table = [linkedList.LinkedList() for i in range(n)]

    def __hash(self, x:int):
        return x % len(self.table)

    def insert(self, x:int):
        idx = self.__hash(x)        
        self.table[idx].insert(0, x)
        self.item += 1

    def search(self, x:int) -> linkedList.ListNode:
        idx = self.__hash(x)
        if self.table[idx].isEmpty():
            return None
        else:
            head = prev = self.table[idx].__getNode(-1)
            curr = prev.next
            while curr != head:
                if curr.item == x:
                    return curr
                else:
                    prev = curr
                    curr = curr.next

    def delete(self, x:int):
        idx = self.__hash(x)
        self.table[idx].remove(x)
        self.item -= 1

    def isEmpty(self):
        return self.item == 0

    def clear(self):
        self.table = linkedList.LinkedList.clear()
        self.item = 0
