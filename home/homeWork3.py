class Bank:
    bank = 'bank'

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return (f'user_name: {self._name}\n'
                f'user_balance: {self._balance}')

    def moneyX(self):
        plus = int(input('сколько денег хотите добавить? '))
        self._balance += plus

    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10

    def _copybalance(self):
        user._balance += user2._balance


user = Bank('Aldiiar', 50000)
user2 = Bank('Bekbolot', 35000)

print(user)
user.moneyX()
# user._kill()
# user._Bank__jackpot()
# user._copybalance()
print(user)








