# import linkedList


class ListStack:
    def __init__(self):
        self.__stack = []

    # 제일 위에 있는 원소 반환
    def top(self):
        if not self.isEmpty():
            return self.__stack[-1]

    # 원소 삽입
    def push(self, item):
        self.__stack.append(item)

    # 제일 위에 있는 원소 삭제
    def pop(self):
        self.__stack.pop()

    # 스택 출력
    def printStack(self):
        for i in range(len(self.__stack)):
            print(self.__stack[i])

    # 스택 비어있는지 여부
    def isEmpty(self) -> bool:
        if len(self.__stack) == 0:
            return True
        else:
            return False
#
#
# st1 = ListStack()
# print(st1.top()) # No effect
# st1.push(100)
# st1.push(200)
# print("Top is", st1.top())
# st1.pop()
# st1.push('Monday')
# st1.printStack()
# print('isEmpty?', st1.isEmpty())

# class LinkedStack:
#     def __init__(self):
#         self.__list = linkedList.LinkedList()
#
#     def push(self, x):
#         self.__list.insert(0, x)
#
#     def pop(self):
#         return self.__list.pop(0)
#
#     def top(self):
#         return self.__list.get(0)
#
#     def isEmpty(self):
#         return self.__list.isEmpty()
#
#     def popAll(self):
#         return self.__list.clear()
#
#     def printStack(self):
#         return self.__list.printList()
#
#
# st1 = LinkedStack()
# st1.push(100)
# st1.push(200)
# print("Top is", st1.top())
# st1.pop()
# st1.push('Monday')
# st1.printStack()
# print('isEmpty?', st1.isEmpty())


def evaluate(p):
    s = ListStack()
    digitPreviously = False
    for i in range(len(p)):
        ch = p[i]
        if ch.isdigit():
            if digitPreviously:
                tmp = s.pop()
                tmp = 10 * tmp + (ord(ch) - ord('0'))
                s.push(tmp)
            else:
                s.push(ord(ch) - ord('0'))
                digitPreviously = True
        elif isOperator(ch):
            s.push(operation(s.pop(), s.pop(), ch))
            digitPreviously = False
        else:
            digitPreviously = False
            return s.pop()


def isOperator(ch) -> bool:
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'


def operation(opr2:int, opr1:int, ch) -> int:
    return {'+': opr1 + opr2, '-': opr1 - opr2, '*': opr1 * opr2, '/': opr1 // opr2}[ch]


def main():
    postfix = '700 3 47 + 6 * - 4 /'
    print('input string: ', postfix)
    answer = evaluate(postfix)
    print('answer: ', answer)
    print(ord('0'), ord('9'))

if __name__ == '__main__':
    main()
    