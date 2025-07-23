import sys
def main():
    try:
        i=0
        files=sys.argv[1:]
        if len(files)>1:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(files)<1:
            print("Too few command-line arguments")
            sys.exit(1)
        filename=files[0]
        if not filename.endswith(".py"):
            print("Not a Python file")
            sys.exit(1)
        with open(files[0],"r") as file:
            for line in file:
                lines=line.strip()
                if lines and not lines.startswith("#"):
                    i+=1
        print(i)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
if __name__ == "__main__": 
    main()