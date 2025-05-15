class BankCard:
    def __init__(self, card_number, pin_code, balance):
        self.card_number = card_number
        self.pin_code = pin_code
        self.balance = balance

    def check_pin(self, pin):
        return pin == self.pin_code

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Сумма {amount} успешно зачислена. Новый баланс: {self.balance}")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        entered_pin = input("Введите PIN-код: ")
        if not self.check_pin(entered_pin):
            print("Неверный PIN-код.")
            return False

        if amount > self.balance:
            print("Недостаточно средств на балансе.")
            return False

        self.balance -= amount
        print(f"Сумма {amount} успешно снята. Новый баланс: {self.balance}")
        return True
