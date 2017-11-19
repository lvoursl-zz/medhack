import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('image', type=str)
parser.add_argument('text', type=str)

args = parser.parse_args()
image_directry = args.image
text_directry = args.text

print(image_directry, text_directry)

try:
    # call for CONVERTIO
    # os.system('php api/request.php ' + img_file_path + ' ' + text_file_path)

    # call for ABBY
    os.system('python2 abby-python-api/process.py ' + image_directry + ' ' + text_directry)
    print('OCR finished')
    with open(text_directry, 'r') as f:
        text = f.read()
        predict(text)

    # call for tesaract
    # text = convert_img_to_text(img_file_path)
    # with open(text_file_path, 'w') as file:
    #     file.write(text)
except Exception as e:
    print(str(e))