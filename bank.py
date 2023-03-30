# 계좌 관리 클래스
class BankAccount:
    def __init__(self, account_number, balance, account_holder_name):
        self.account_number = account_number
        self.balance = balance
        self.account_holder_name = account_holder_name

    # 입금 메서드
    # 액수 받아서 총 잔액에 추가
    # 어느 계좌에 얼마가 입금 됐는지 출력
    def deposit(self, money):
        self.balance += money
        print(f'{money} deposited to {self.account_number}')

    # 출금 메서드
    # 액수 받아서 총 잔액에서 차감
    # 어느 계좌에서 얼마가 빠졌는지 출력
    def withdraw(self, money):
        self.balance -= money
        print(f'{money} withdrawn from {self.account_number}')


    def get_bankaccountinfo(self):
        return self


# 계좌 생성, 1000원 입금, 2000원 출금
account1 = BankAccount('1234567890', 5000, 'John Doe')
account1.deposit(1000)
account1.withdraw(2000)
