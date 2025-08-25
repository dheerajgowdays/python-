from datetime import date
import sys
import inflect
class Time:
    def __init__(self):
        pass

def main():
    bod=input("Date Of Birth: ").replace("/","-")
    y,m,d=bod.split("-")
    print(y ,m , d)
    if (m<=12 and d<=31 and len(y)==4) :
        return y,m,d
    else:
        print("Invalid Input")
        sys.exit(1)

if __name__ == "__main__":
    main()
