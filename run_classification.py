import os
import argparse

from time import sleep

from predict import predict

parser = argparse.ArgumentParser()
parser.add_argument('image_filename', type=str)

args = parser.parse_args()
image_filename = args.image_filename
text_filename = str(image_filename.replace(os.path.splitext(image_filename)[1], '.txt'))
result_filename = str(image_filename.replace(os.path.splitext(image_filename)[1], '.prediction'))

print(image_filename, text_filename, result_filename)

try:
    # call for CONVERTIO
    # os.system('php api/request.php ' + img_file_path + ' ' + text_file_path)

    # call for ABBY
    if result_filename in os.listdir('.'):
        print('file exist!')
        sleep(4)
    else
        os.system('python2 abby-python-api/process.py ' + image_filename + ' ' + text_filename)
        print('OCR finished')
        with open(text_filename, 'r') as f:
            text = f.read()
            print('file loaded, start prediction')
            predictions = predict(text)
            print(predictions)

        with open(result_filename, 'w') as f:
            f.write(str(predictions))

        # call for tesaract
        # text = convert_img_to_text(img_file_path)
        # with open(text_file_path, 'w') as file:
        #     file.write(text)
except Exception as e:
    print(str(e))