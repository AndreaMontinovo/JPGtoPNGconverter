import sys
import os
from PIL import Image

origin_dir = sys.argv[1]
new_dir = sys.argv[2]

if not os.path.isdir(new_dir):
    os.mkdir(new_dir)

for file in os.listdir(origin_dir):
    image = Image.open(origin_dir + "/" + file)
    f, e = os.path.splitext(file)
    outfile = "./" + new_dir + "/" + f + ".png"
    image.save(outfile)
