import sys
import requests


def main():
    try:
        arg=sys.argv[1]
        if len(arg)==1:
            if arg.isnumeric():
                arg=float(arg)
                print(arg)
            else:
                print("Command-line argument is not a number")
                sys.exit(1)
        elif len(arg)==0:
            print("Missing command-line argument")
            sys.exit(1)
        else:
            print(len(arg))
            print(arg)
            sys.exit(1)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    operation(arg)      
        
def operation(arg):
    try:
        response=requests.get("https://rest.coincap.io/v3/assets?apiKey=3677663f5ce0fb99788ae587557d5c9bf0937784bc4a7ced2644967f3ea37721")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit(1)
    content = response.json()
    print(content)
main()
    