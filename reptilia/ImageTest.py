#encoding=gbk
'''
Created on 2012-12-18

@author: virusyang
'''

from PIL import Image, ImageFilter, ImageEnhance
from Matrix import Matrix, MatrixHandler

image_name = "E:/Downloads/captcha1.jpg"

im = Image.open(image_name,'r')

#if(im.mode !=Image.getmodebase("RGB")):
#    print ""
#    exit()

im = im.filter(ImageFilter.MaxFilter)
#
enhancer = ImageEnhance.Contrast(im)

im = enhancer.enhance(2)
#
#im = im.convert('P')
#
#im.show()
#print im.format, im.mode, im.size 

#Lim = im
Lim = im.convert('L')  
#Lim.save('E:/Downloads/captchaxx.jpg')  
threshold = 80 
table = []  

for i in range(256):  
    if i < threshold: 
        table.append(0)  
    else:  
        table.append(1)  

bim = Lim.point(table, '1')  

m=Matrix(bim)
h=MatrixHandler(m.getMatrix())
h.doHandler()

#bim.show()
##
#Lim.save('captchaxxx.jpg')
# 