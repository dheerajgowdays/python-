#In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
def main():
    plates = input("plates: ")
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum():
        s1 = list(s)
        if len(s1) <= 6 and len(s1) > 2 and s1[0].isalpha() and s1[1].isalpha():
            d = False
            for c in s1:
                if c.isdigit():
                    if c == '0' and not d:
                        return False
                    d = True
                elif d:
                    return False
            return True
        else:
            return False
    else:
        return False

main()