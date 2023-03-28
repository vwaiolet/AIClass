## 파이썬 문법 

### 데이터 타입
 + int : 정수형, ex) 1, 2, 3, 4
 + float : 실수형, ex) 3.27
 + bool : True/False
 + None Type : None
 + ```type()``` 이용해서 데이터 타입 확인 가능
```python
>>>type(5)
int

>>>type(3.0)
float
```
 + 데이터 타입 변환 가능
```python
>>>float(3)
 => 3 -> 3.0
 
>>>int(3.9)
 => 3.9 -> 3
```

### 콘솔에 출력하기
```python
>>>3 + 2
5

>>>print(3 + 2)
5
```

### 산술 연산자
 + ```i + j``` 더하기
 + ```i - j``` 빼기
 + ```i * j``` 곱하기
 + ```i / j``` 나누기
 + ```i % j``` i에서 j를 나눈 나머지
 + ```i ** j``` i의 j제곱

### 변수에 값 할당
 + = 기호 사용
 + ```pi = 3.14``` pi 라는 변수에 3.14라는 값 할당
 + ```pi_approx = 22/7``` pi_approx 라는 변수에 22/7에 해당하는 값 할당
 + 변수에 값을 할당하면 컴퓨터 메모리에 저장
 + 변수 이름을 이용하여 여러 연산이 가능
```python
>>>pi = 3.14
>>>radius = 2.2
>>>area = pi * (radius ** 2)
```
 + 변수는 값을 변경할 수 있음
```python
>>>pi = 3.14
>>>radius = 2.2
>>>area = pi * (radius ** 2)
>>>radius = radius + 1
```
 + 위 코드 마지막 줄로 인해 radius는 3.2라는 값을 갖게됨

### 문자열1
 + ' '나 " "로 묶으면 문자열
 + ex) ```hi = "Hello Python"```
 + 문자열 출력 예시
```python
>>>hi = "Hello there"
>>>name = "Kim"
>>>greet = hi + " " + name
>>>print(greet)
Hello there Kim
```

### 사용자 입력 받기
 + ```input()``` 이용
```python
>>>text = input("Type anything... ")
>>>print(5 * text)
```
 + 위 코드는 입력받은 문자열을 5번 출력
 + ()안에는 콘솔창에 출력할 문장
 + 숫자를 입력받고 싶으면 ```int(input())```과 같이 형변환 이용

### 비교 연산자
 + True/False 리턴
 + ```i > j``` i가 j보다 크다
 + ```i >= j``` i가 j보다 크거나 같다
 + ```i < j``` i가 j보다 작다
 + ```i <= j``` i가 j보다 작거나 같다
 + ```i == j``` i와 j가 같다
 + ```i != j``` i와 j가 같지 않다

### bool 연산자
 + True/False 리턴
 + ```not a``` a가 False면 True, a가 True면 False
 + ```a and b``` a와 b 모두 True여야 True
 + ```a or b``` a와 b 둘중 하나만 True여도 True

### 조건문
 + 조건에 따라 다른 분기로 실행
```python
>>>if <조건>:
>>>    <코드>
>>>elif <조건>:
>>>    <코드>
>>>else:
>>>    <코드>
```

### while 반복문
 + 조건이 만족할 동안 반복
```python
>>>while <조건>:
>>>    <코드>
```

### for 반복문
 + 지정된 범위 만큼 반복
```python
>>>for <변수> in range(<시작, 끝-1, 증가 폭>):
>>>    <코드>
```

### break문
 + 만나는 즉시 반복문 탈출
```python
>>>while <조건>:
>>>    break
```

### 문자열2
 + 문자열끼리 비교 연산자로 비교 가능
 + ```len()``` 이용하여 문자열의 길이 반환
```python
>>>s = 'abc'
>>>len(s)
3
```
 + 배열처럼 인덱싱이 가능
```python
>>>s = 'abc'
>>>s[0]
a

>>>s[-2]
b
```
 + ```[시작:끝-1:증가 폭]``` 형태로 슬라이싱 가능
```python
>>>s = 'abcdefgh'
>>>s[3:6]
def

>>>s[3:6:2]
df

>>>s[::]
abcdefgh

>>>s[::-1]
hgfedbca

>>>s[4:1:-2]
ec
```
 + 인덱스를 통해 문자 변경이 불가능
```python
>>>s = 'hello'
>>>s[0] = 'y'
error
```

### 바이너리 서치
 + 절반 씩 나누면서 결과값 찾아가는 알고리즘
 + O(log N)

### 함수
 + 재사용 할 수 있고 호출하여 사용하는 코드
```python
>>>def <name>(<parameter>):
>>>    <code>
>>>
>>><name>(<parameter>)
```
