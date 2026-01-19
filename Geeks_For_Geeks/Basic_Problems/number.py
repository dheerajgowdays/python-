def is_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a < n:
        a, b = b, a + b

    return a == n


num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number")
else:
    print(f"{num} is NOT a Fibonacci number")
