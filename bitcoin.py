import sys
import requests


def main():
    try:
        args=sys.argv[1:]
        if len(args)==1:
            arg=float(args[0])
        elif len(args)==0:
            print("Missing command-line argument")
            sys.exit(1)
        else:
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
    content=response.json()
    price = float(content["data"][0]["priceUsd"])
    amount=arg*price
    print(f"${amount:,.4f}")

main()
    