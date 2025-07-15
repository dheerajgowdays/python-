import sys
import requests
def main():
    try:
        arg=sys.argv[1:]
        print(arg*6)
        response=requests.get()
        response.raise_for_status()
    except requests.RequestException():
        sys.exit(1)
    content = response.json()
main()
    