class Natrual:
    def __init__(self ,a):
        self.a = a
    
    def cube(self):
        sum = 0
        for i in range(self.a+1):
            sum += i ** 3
        return sum

def main():
    try:
        a = int(input("Enter a Number: "))
    except ValueError:
        print("Enter a valid input")
        return
    sum = Natrual(a)
    print("Sum:",sum.cube())

if __name__ == "__main__":
    main()