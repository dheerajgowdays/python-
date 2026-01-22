def main():
    arr = []
    while True:
        try:
            a = int(input("Enter the size of Array:"))
            if a<0:
                print("Enter a positive number")
                continue
            break
        except ValueError:
            print("Enter a valid input")
    for _ in range(a):
        while True:
            try:
                n = int(input("Enter the elements of array:"))
                if n<0:
                    print("Enter positive Numbers")
                    continue
                break
            except ValueError:
                print("Enter a valid input")
        arr.append(n)
    sum =1
    while True:
        try:
            x = int(input("Enter the number to divide:"))
            if x<0:
                print("Enter positive Numbers")
                continue
            break
        except ValueError:
            print("Enter a valid input")
    for i in range(len(arr)):
        sum *= (arr[i])
    print("Result:",(sum % x))

if __name__ == "__main__":
    main()