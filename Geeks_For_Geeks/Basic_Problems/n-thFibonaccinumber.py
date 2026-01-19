import math
def main():
    while True:
        try:
            n = int(input("Enter a Number:"))
            if n<=0:
                print("Enter a valid input")
                continue
            break
        except ValueError:
            print("Enter a valid input")
        
    f = (((1 + math.sqrt(5)) ** n) - ((1-math.sqrt(5)) ** n)) / ((2 ** n)*math.sqrt(5))
    print(f"{round(f)} is {n}th fibonacci number")

if __name__ == "__main__":
    main()