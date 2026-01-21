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

    max_value = a[0]
    for i in range(1,len(a)):
        if a[i]>max_value:
            max_value = a[i]

    print("Maximum value in array is:",max_value)

if __name__ == "__main__":
    main()