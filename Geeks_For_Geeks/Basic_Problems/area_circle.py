import math

def area(r):
    """Calculate the area of a circle given its radius."""
    return math.pi * r ** 2 
def main():
    try:
        r = float(input("Enter radius:"))
    except ValueError:
        print("Enter a valid input")
        return
    
    if r<0:
        print("Radius cannot be negative")
        return

    print("Area:",round(area(r),2))


if __name__ == "__main__":
        main()