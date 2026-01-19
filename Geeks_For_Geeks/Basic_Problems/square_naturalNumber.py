class Natrual:
    def __init__(self, n):
        self.n = n

    def square(self):
        sum = 0
        for i in range(self.n + 1):
            sum += i**2
        return sum


def main():
    try:
        n = int(input("Enter a Number: "))
    except ValueError:
        print("Enter a valid input")
        return
    sum = Natrual(n)
    print("Sum:", sum.square())


if __name__ == "__main__":
    main()
