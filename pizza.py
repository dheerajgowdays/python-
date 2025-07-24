import sys
from tabulate import tabulate

def main():
    try:
        files=sys.argv[1:]
        if len(files)>1:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(files)<1:
            print("Too few command-line arguments")
            sys.exit(1)
        with open(files[0],"r") as file:
            filename=files[0]
            if not filename.endswith(".csv"):
                print('Not a CSV file')
                sys.exit(1)
            for line in file:
                g
            
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    
main()