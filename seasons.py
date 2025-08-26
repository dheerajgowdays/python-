from datetime import date , datetime
import sys
import inflect
class Time:
    def __init__(self):
        pass

def main():
    bod1 = get_bod()
    

def get_bod():
    bod=input("Date Of Birth: ").replace("/","-")
    try:
        bod = datetime.strptime(bod, "%Y-%m-%d").date()
        return Time(bod)
    except ValueError:
        print("Invalid Input")
        sys.exit(1)

if __name__ == "__main__":
    main()
