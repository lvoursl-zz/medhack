import os
import argparse
from img_to_text import convert_img_to_text

parser = argparse.ArgumentParser()
parser.add_argument('image_directry', type=str)
parser.add_argument('text_directry', type=str)

args = parser.parse_args()
image_directry = args.image_directry
text_directry = args.text_directry

print(image_directry, text_directry)

for root, sub_folder, files in os.walk(image_directry):
    for item in files:
        folder = os.path.basename(os.path.normpath(root))

        img_file_path = str(os.path.join(root, item))
        text_file_path = str(os.path.join(text_directry, folder, item.replace(os.path.splitext(img_file_path)[1], '.txt')))
        print(img_file_path, text_file_path)
        text = convert_img_to_text(img_file_path)

        with open(text_file_path, 'w') as file:
            file.write(text)