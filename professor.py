'''In a file called professor.py, implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
 Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:'''
import random


def main():
    level=get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            n= int(input("Level: "))
            if n>0 and n<4:
                return n
                break
            else:
                continue
        except ValueError:
            continue
def generate_integer(level):
    k=0
    i=1
    while i<=10:
        if level == 1:
            x=random.randrange(1,9)
            y=random.randrange(1,9)
            z=x+y
            
            try:
                sum=int(input(f"{x}+{y}="))
                if sum == z:
                    k+=1
                    i+=1
                    continue
                else:
                    i+=1
                    raise ValueError("EEE")
            except ValueError as e:
                print(e)
                continue
        elif level==2:
            x=random.randrange(10,99)
            y=random.randrange(10,99)
            z=x+y
            while i<4:
                try:
                    sum=int(input(f"{x}+{y}="))
                    if sum == z:
                        k=+1
                        continue
                    else:
                        raise ValueError("EEE")
                except ValueError as e:
                    print(e)
                    continue
        else:
            x=random.randrange(100,999)
            y=random.randrange(100,999)
            z=x+y
            try:
                sum=int(input(f"{x}+{y}="))
                if sum == z:
                    k+=1
                    i+=1
                    continue
                else:
                    raise ValueError("EEE")
            except ValueError as e:
                print(e)
                continue
    print(f"Score:{k}")
if __name__ == "__main__":
    main()