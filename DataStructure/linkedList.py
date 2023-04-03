class ListNode:
    def __init__(self, newItem, nextNode:'ListNode'):
        self.item = newItem
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    # i번째 인덱스에 newItem 삽입
    def insert(self, i:int, newItem):
        prev = self.__getNode(i-1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    # 맨 뒤에 newItem 삽입
    def append(self, newItem):
        prev = self.__getNode(self.__numItems-1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    # i번째 인덱스 삭제하고 알려줌
    def pop(self, i:int):   # i번 노드 삭제. 고정 파라미터
        prev = self.__getNode(i-1)
        current = prev.next
        prev.next = current.next
        retItem = current.item
        self.__numItems -= 1
        return  retItem

    # 처음으로 나타나는 x 삭제
    def remove(self, x):
        (prev, current) = self.__findNode(x)
        if current != None:
            prev.next = current.next
            self.__numItems -= 1
            return x
        else:
            return None

    # i번째 인덱스의 값 알려줌
    def get(self, i:int):
        return self.__getNode(i).item

    # x가 몇번째 인덱스인지 알려줌
    def index(self, x) -> int:
        current = self.__head.next
        for i in range(self.__numItems):
            # 리스트의 i번째 인덱스의 값이 x이면 i 값 반환
            if self.__getNode(i).item == x:
                return i
            else:
                current = current.next
    
    # 리스트가 비어있는지 확인
    def isEmpty(self) -> bool:
        if self.__head is None:
            return True
        else:
            return False
    
    # 리스트의 크기 반환
    def size(self) -> int:
        return self.__numItems

    # 리스트 비우기
    def clear(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    # 리스트에 x가 몇번 있는지 반환
    def count(self, x) -> int:
        current = self.__head.next
        count = 0
        for i in range(self.__numItems):
            # 리스트의 i 번째 인덱스에 x가 있는지 확인
            if self.__getNode(i).item == x:
                count += 1
            current = current.next

        return count

    # a(리스트)를 풀어서 리스트에 추가
    def extend(self, a): # 여기서 a는 self와 같은 타입의 리스트
        for i in range(a.size()):
            self.append(a.get(i))

    # 리스트를 복사하여 새로운 리스트를 반환
    def copy(self):
        L = LinkedList()
        for i in range(self.__numItems):
            L.append(self.get(i))
        return L

    # 리스트의 순서를 역으로 뒤집음
    def reverse(self):
        L = LinkedList()
        for i in range(self.__numItems):
            L.insert(0, self.get(i))
        self.clear()
        for idx in range(L.size()):
            self.append(L.get(idx))

    # 리스트 정렬
    def sort(self) -> None:
        L = []
        for i in range(self.__numItems):
            L.append(self.get(i))
        L.sort()
        for i in range(len(L)):
            self.append(L[i])

    #
    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head
        current = prev.next
        while current != None:
            if current.item == x:
                return (prev, current)
            else:
                prev = current; current = current.next
        return (None, None)

    # 리스트의 i번 노드 알려줌
    def __getNode(self, i:int) -> ListNode:
        current = self.__head
        for idx in range(i+1):
            current = current.next

        return current

    # 리스트 전체 출력
    def printList(self):
        current = self.__head.next
        while current is not None:
            print(current.item)
            current = current.next




#LinkedList Test

list = LinkedList()
list.append(30)
list.insert(0, 20)
a = LinkedList()
a.append(4)
a.append(3)
a.append(3)
a.append(2)
a.append(1)
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()