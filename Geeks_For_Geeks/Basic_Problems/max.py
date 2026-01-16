def main():
    try:
        a=int(input("Enter a Number A:"))
        b=int(input("Enter a Number B:"))
    except ValueError:
        print("Enter a valid input")
    print("Maximmum Value",max(a,b))

if __name__ == "__main__":
    main()
