import app
import math

class InvalidPermissions(Exception):
    pass

class Calculator:

    def add(self, x, y):
        self.check_types(x, y)

        return x + y

    def substract(self, x, y):
        self.check_types(x, y)

        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)

        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        
        if x == 0 and y < 0:
            raise TypeError("0 cannot be raised to a negative power")

        return x ** y

    def sqrt(self, x):
        self.check_types(x)

        if x < 0:
            raise TypeError("Cannot compute the square root of negative number without using complex numbers")

        return math.sqrt(x)
    
    def log(self, x):
        self.check_types(x)

        if x <= 0:
            raise TypeError("Cannot compute log10 of negative numbers or zero")

        return math.log10(x)

    def check_types(self, x, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
