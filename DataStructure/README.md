## 자료구조

### Linked List
 + 리스트의 단점을 극복하기 위한 자료구조
 + 리스트는 연속된 공간에 저장하므로 삽입/삭제 시 시프트 작업 필요
 + 노드에 값과 다음 노드의 주소를 저장
 + 리스트 중간에 삽입/삭제가 용이

### Circular Linked List
 + Linked List의 마지막 노드가 다음 노드의 주소를 None이 아닌 첫번째 노드의 주소를 저장

### Doubly Linked List
 + 노드에 값과 이전/다음 노드의 주소를 저장

### Stack
 + LIFO(Last In First Out)
 + 가장 최근에 삽입한 원소에만 접근 가능
 + ex) 웹브라우저, 스택 메모리...

### Queue
 + FIFO(First In First Out)
 + 가장 먼저 삽입한 원소에만 접근 가능

### Priority Queue
 + 우선순위를 가진 자료구조

### Heap
 + 대표적인 우선순위 큐
 + 완전 이진 트리여야 하며 모든 노드는 값을 가짐
 + 최대힙은 루트가 최대값을 가짐
 + 최소힙은 루트가 최소값을 가짐