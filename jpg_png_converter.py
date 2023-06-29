from PIL import Image, ImageFilter
import os
import sys

from performance_chk_decorator import performance
@performance
def jpg_png_converter():
    try:
        image_path=sys.argv[1]
        output_path=sys.argv[2]
    except IndexError:
        print('''
        please enter *python {program path} {image folder/file path} {output folder path}
        eg: python 
         
        ''')
        sys.exit()
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if os.path.isfile(image_path):
        img = Image.open(f'{image_path}')
        base_name = os.path.basename(image_path)
        clean_name = os.path.splitext(base_name)[0]
        img.save(f'{output_path}{clean_name}.png','png')
        print('Good to go!!')
    elif os.path.isdir(image_path):
        for file in os.listdir(image_path):
            img = Image.open(f'{image_path}{file}')
            clean_name = os.path.splitext(file)[0]
            img.save(f'{output_path}{clean_name}.png','png')
            print('Good to go!!')
jpg_png_converter()