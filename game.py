'''In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.'''
import random
import sys
def main():
    while True:
        try:
            n=int(input("Level: "))
            if n>0:
                break
            else:
                continue
        except ValueError:
            continue
    guess=random.randrange(n)
    while True:
        try:
            g=int(input("Guess: "))
            if guess<g:
                print("Too large!")
                continue
            elif g<guess:
                print("Too small!")
                continue
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            continue
main()    