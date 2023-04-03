class ListStack:
    def __init__(self):
        self.s = []

    # 제일 위에 있는 원소 반환
    def top(self):
        if not self.isEmpty():
            return self.s[-1]

    # 원소 삽입
    def push(self, item):
        self.s.append(item)

    # 제일 위에 있는 원소 삭제
    def pop(self):
        self.s.pop()

    # 스택 출력
    def printStack(self):
        for i in range(len(self.s)):
            print(self.s[i])

    # 스택 비어있는지 여부
    def isEmpty(self) -> bool:
        if len(self.s) == 0:
            return True
        else:
            return False

st1 = ListStack()
print(st1.top()) # No effect
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print('isEmpty?', st1.isEmpty())
