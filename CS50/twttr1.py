#In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase
def main():

    word=input("Input: ")
    result=shorten(word)
    print(f"Output:{result}")

def shorten(word):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    strin=""
    for i in word:
        if i in vowels:
            continue
        else:
            strin+=i
    return strin

if __name__ == "__main__":
    main()
