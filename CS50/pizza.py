import sys
import csv
from tabulate import tabulate

def main():
    try:
        fil=sys.argv[1:]
        if len(fil)>1:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(fil)<1:
            print("Too few command-line arguments")
            sys.exit(1)
        filename=fil[0]
        if not filename.endswith(".csv"):
                print('Not a CSV file')
                sys.exit(1)
        with open(filename,"r") as file:
            reader = csv.DictReader(file)
            table=list(reader)
            print(tabulate(table, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

main()
