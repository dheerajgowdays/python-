import re
import sys


def main():
    print(convert(input("Hours: ").lower()))


def convert(s):
    a,b=s.split("to")
    if a.endswith("am"):
        
if __name__ == "__main__":
    main()