import sys

from PIL import Image 
images=[]
for argr in sys.argv[1:]:
    image=Image.open(argr)
    images.append(image)
images[0].save(
    "costumes.gif",save_all=True,append_images=[images[1]],duration=400,loop=0
)
