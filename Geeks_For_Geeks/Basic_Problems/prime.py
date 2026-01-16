from sympy import *

""" Checking Number is prime number or not """
def main():
    try:
        a = int(input("Enter a number:"))
    except ValueError:
        print("Enter a valid number")
        return
    if a<=0:
        print("Negative numbers are not prime numbers")
    elif isprime(a):
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")


if __name__ == "__main__":
    main()