# 사용자에게 입력받은 수 만큼 별 찍기
'''
number = int(input("별의 갯수를 입력 : "))
for i in range(0, number):
    print('*', end='')

print()
print('*' * number)
'''

# True / False
'''
pset_time = 15
sleep_time = 8
if sleep_time > pset_time:
    print(sleep_time > pset_time)
else:
    print(pset_time)
derive = True
drink = False
both = drink and derive
print(both)
'''

# x와 y 입력 받아서 크기 비교
'''
x = float(input('Enter a number for x : '))
y = float(input('Enter a number for y : '))
if x == y:
    print('x and y are equal')
    if y != 0:
        print('therefore, x / y is', x / y)
elif x < y:
    print('x is smaller')
else:
    print('y is smaller')
print('thanks!')
'''

# for문을 이용하여 1부터 100까지의 합 출력
'''
sum = 0
for i in range(1, 101, 1):
    sum += i
print(sum)
'''

# 숫자를 입력 받고 0까지 출력, 음수 입력 시 에러 메시지
'''
num = int(input('enter a number : '))
if num < 0:
    print('input error')
else:
    for i in range(num, -1, -1):
        print(i, end=' ')
'''

# 문자열에서 H가 몇번째 인덱스에 있는지 출력
'''
s = 'Hello World'
for i in range(0, len(s), 1):
    if s[i] == 'H':
        print('H is', i, 'in the string')
        break
'''

# 1부터 10까지 홀수만 출력
'''
for i in range(1, 11, 2):
    print(i, end=' ')
'''

# s1과 s2의 길이가 같을 때, 같은 문자를 가지고 있으면 common letter 출력
'''
s1 = 'mit u rock'
s2 = 'i rule mit'
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print('common letter')
                break
'''

# 입력받은 값의 3제곱근 찾기
'''
cube = int(input('cube : '))
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of '+str(cube)+' is '+str(guess))
'''

# 위 코드 개선
# cube == -1 < 0 and 0 < 1 일때 어떻게 할지 생각해보기(바이너리 서치)
'''
cube = int(input('cube : '))
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
'''    

