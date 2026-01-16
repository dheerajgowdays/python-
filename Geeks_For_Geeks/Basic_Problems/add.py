class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


def main():
    try:
        a = int(input("Enter a Number A:"))
        b = int(input("Enter a Number B:"))
    except ValueError:
        print("Enter a valid input in Integer form")
        return
    calc = Calculator(a, b)
    print("The Sum:",calc.add())


if __name__ == "__main__":
    main()
