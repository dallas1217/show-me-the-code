#-*- coding=utf8 -*-

import os
import re
from PIL import Image

def resize_img(img_name, img):
    im = Image.open(img)
    w, h = im.size
    print('Image name: %s' % img_name)
    print('Original image size: %sx%s' % (w, h))
    im.thumbnail((w//2, h//2))
    print('Resize image to: %sx%s' % (w//2, h//2))
    im.save('%s.jpg' %(img_name + '_1'), 'jpeg')

def find_img(path):
    img_list = []
    name_list = []
    pattern = re.compile(r'(\w+).\b(jpg|png|jpeg|gif|bmp)\b')
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern.match(name):
                im_name = pattern.match(name).group(1)
                img_path = os.path.join(root, name).replace('\\', r'/')
                name_list.append(im_name)
                img_list.append(img_path)
            
    return dict(zip(name_list, img_list))

if __name__ == '__main__':
    path = 'E:\show-me-the-code'
    img = find_img(path)
    for name, path in img.items():
        resize_img(name, path)
