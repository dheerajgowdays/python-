def main():
    a =[]
    while True:
        try:
            n = int(input("Enter the size of an array: "))
            if(n<=0):
                print("Size of array must be positive")
                continue
            break
        except ValueError:
            print("Enter a valid input")

    for i in range(n):
        while True:
            try:
                z = int(input("Enter an array element: "))
                break
            except ValueError:
                print("Enter a valid input")
        a.append(z)
    
    while True:
        try:
            d = int(input("Enter the number postion:"))
            if n<0:
                print("Enter a postive number")
                continue
            break
        except ValueError:
            print("Enter a valid input")
    
    while True:
        try:
            a = int(input("Enter the option 1)By Rotation 2)By Reversal Algorithm 3)By split and add "))
            if a not in [1,2,3]:
                print("Enter a valid input")
                continue
            break
        except ValueError:
            print("Enter a valid input")

    match a:
        case 1:
            a[:]=a[d:]+a[:d]
            print(a)
        case 2:
            a[:d]=reversed(a[:d])
            a[d:]=reversed(a[d:])
            print(a.reverse())
        case 3:
            res = [a[(i + d) % len(a)] for i in range(len(n))]
            print(res)
    
if __name__ == "__main__":
    main()