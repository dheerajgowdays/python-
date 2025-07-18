"""In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""
import sys
import random
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    fonts=figlet.getFonts()
    args = sys.argv[1:]
    if not args:
        figlet.setFont(font=random.choice(fonts))
    elif len(sys.argv) == 1:
        choice_font=random.choice(sys.argv)
        figlet.setFont(font=choice_font)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f','-font']:
        choice_font=sys.argv[2]
        if choice_font not in fonts :
            sys.exit("Invalid usage")
        figlet.setFont(font=choice_font)
    else:
         sys.exit("Invalid usage")
    sentance=input("Input:")
    print(figlet.renderText(sentance))
if __name__ == "__main__":
    main()
