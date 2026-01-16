import math
def armstrong_number(a):
    r = str(a)
    n = len(r)
    result = 0
    for i in range(n):
        result += float(math.pow(int(r[i]),n))
    return result

def main():
    try:
        a = int(input("Enter a Number: "))
    except ValueError:
        print("Enter a valid input")
        return
    if (a<0):
        print("Enter a Number Greater than ZERO")
        return
    an = armstrong_number(a)
    if(a==an):
        print(f"{a} is Armstrong Number")
    else:
        print(f"{a} Not a Armstrong Number")

if __name__ == "__main__":
    main()