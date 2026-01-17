import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv)>3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv)<3:
        print("Too few command-line arguments")
        sys.exit(1)
    img1=sys.argv[1]
    img2=sys.argv[2]
    for ext in ('.png', '.jpg', '.jpeg'):
        if  img1.lower().endswith(ext) and img2.lower().endswith(ext):
            break
        elif not img1.lower().endswith(ext) and img2.lower().endswith(ext):
            print("Input and output have different extensions")
            sys.exit(1)
        elif img1.lower().endswith(ext) and not img2.lower().endswith(ext):
            print("Input and output have different extensions")
            sys.exit(1)

    else:
        if not img1.lower().endswith(('.png', '.jpg', '.jpeg')):
            print("Invalid Input")
            sys.exit(1)
        if not img2.lower().endswith(('.png', '.jpg', '.jpeg')):
            print("Invalid Output")
            sys.exit(1)
    try:
        image(img1,img2)
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

def image(f,g):
        shirt=Image.open('shirt.png')
        muppet=Image.open(f)
        muppet = ImageOps.fit(muppet, shirt.size)
        muppet.paste(shirt, shirt)
        muppet.save(g)

if __name__ == "__main__":
    main()
