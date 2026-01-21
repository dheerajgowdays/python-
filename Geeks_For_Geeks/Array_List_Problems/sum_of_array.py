def main():
    a =[]
    sum = 0
    while True:
        try:
            n = int(input("Enter the size of an array: "))
            if(n<0):
                print("Size of array cannot be negitive")
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

    for i in range(len(a)):
        sum += a[i]
    print("Sum:",sum)
if __name__ == "__main__":
    main()