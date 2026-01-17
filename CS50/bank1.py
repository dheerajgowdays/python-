def main():
    greet=input("Greeting:")
    print(f"${value(greet)}")


def value(greet):
     if "hello" in greet.lower():
        return 0
     elif not "hello" in greet.lower() and  greet.lower().startswith("h"):
        return 20
     else:
        return 100

if __name__ == "__main__":
    main()

