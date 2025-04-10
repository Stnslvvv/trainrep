class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
    
    def deposit(self, money):
        if money>0:
            self.balance += money
            print(f"Вы успешно пополнили счет! Сумма на счете: {self.balance}")

    def withdraw(self, money):
        if money>self.balance:
            print(f"Недостаточно денег на счету! Сумма на счете: {self.balance}")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} руб. Сумма на счете: {self.balance} ")

    def all_balance(self):
        print(f"Сумма на счете: {self.balance}")

man = Account(id="12345", balance= 600)
man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)