#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os
def vercalformat(v):
    v1 = []
    for x in v:
        v1.append((x[0],x[1],x[0],x[3]))
        v1.append((x[2],x[1],x[2],x[3]))
    return v1
def putVercalline(v,imgpath):
    im = Image.open(imgpath) 
    im.show()
    for i in range(0,im.size[1]-1):
        for j in range(0,len(v)):
            im.putpixel((v[j][0],i), (0,0,0))
    im = im.convert('RGB')
    return im

def Vercal(imgpath):
    img = Image.open(imgpath)
    img_gray = img.convert('L')
    img_black_white = img_gray.point(lambda x: 0 if x < 150 else 255)
    v=vertical(img_black_white)
    v1=vercalformat(v)
    return v1

def vertical(img):
    pixdata = img.load()
    w,h = img.size
    ver_list = []
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x,y] == 0:
                black += 1
        ver_list.append(black)
    l,r = 0,0
    flag = False
    cuts = []
    for i,count in enumerate(ver_list,0):
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i-1
            flag = False
            cuts.append((l,0,r,h))
    return cuts

def resize(w, h, w_box, h_box, pil_image):  
    f1 = 1.0*w_box/w 
    f2 = 1.0*h_box/h  
    factor = min([f1, f2])  
    width = int(w*factor)  
    height = int(h*factor)  
    return pil_image.resize((width, height), Image.ANTIALIAS)  