"""Printing ASCII vlaue of character"""

def main():
    try:
        a = (input("Enter a character: "))
    except ValueError:
        print("Enter valid input")
        return
    n = len(a)
    if n!=1:
        print("Enter a single character")
        return
    print("ASCII value of character is :", ord(a))


if __name__ == "__main__":
    main()
