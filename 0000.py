#-*- coding=utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_num(im): 
    draw = ImageDraw.Draw(im)
    fillcolor = 'red'
    font = ImageFont.truetype('C:\Windows\Fonts\BRITANIC.ttf', 30)
    width, height = im.size
    draw.text((width-40,10), u'1', font = font, fill=fillcolor)
    im.save('test1.jpg', 'jpeg')

if __name__ == '__main__':
    im = Image.open('test.jpg')
    add_num(im)

