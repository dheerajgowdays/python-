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

    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            if i == len(a)-2:
                print("True")
                break
        else:
            print("False")
            break

if __name__ == "__main__":
    main()