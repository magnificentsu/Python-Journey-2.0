import sys
import os
from PIL import Image

origin_directory = sys.argv[1]
final_directory = sys.argv[2]

if not os.path.exists(final_directory):
    os.makedirs(final_directory)

for files in os.listdir(origin_directory):
    img = Image.open(f'{origin_directory}/{files}')
    clean_name = os.path.splitext(files)[0]
    img.save(f'{final_directory}/{clean_name}.png','png')
    print('All Done!')
