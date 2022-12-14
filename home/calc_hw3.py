class Calculator:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x


x1 = Calculator(28)
x2 = Calculator(7)
ad = x1 + x2
s = x1 - x2
mu = x1 * x2
trd = x1 / x2
print(ad, s, mu, trd)