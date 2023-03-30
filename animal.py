# 동물 클래스
# 이름과 종을 받아서 저장
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # 울음 소리
    def make_sound(self):
        return


# 개 클래스
# 동물 클래스 상속
class Dog(Animal):
    # 울음 소리 출력
    def make_sound(self):
        print('Woof!')

# class Dog:
#     def __init__(self, name, breed):
#         super().__init__(name, species='Dog')
#         Animal().__init__(name, species="Dog")
#         super(self, Animal).__init__(name, species='Dog')
#         self.breed = breed
#
#     def make_sound(self):
#         print('Woof!')


# 고양이 클래스
# 동물 클래스 상속
class Cat(Animal):
    # 울음 소리 출력
    def make_sound(self):
        print('Meow!')


# 개와 고양이 생성
dog1 = Dog('Fido', 'Golden Retriever')
cat1 = Cat('Fluffy', 'White')

# 개와 고양이 이름 출력
print(dog1.name) # Fido 출력
print(cat1.name) # Fluffy 출력

# 개와 고양이 울음소리 출력
dog1.make_sound() # Woof! 출력
cat1.make_sound() # Meow! 출력
