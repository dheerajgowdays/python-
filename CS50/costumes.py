import sys

from PIL import Image

if len(sys.argv) < 3:
    print("Usage: python costumes.py image1 image2 [image3 ...]")
    sys.exit(1)

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=images[1:], duration=400, loop=0
)
