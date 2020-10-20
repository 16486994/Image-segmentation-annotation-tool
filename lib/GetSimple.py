#!/usr/bin/env python
# coding: utf-8
import os
import urllib
def saveSimpleImg(index,url,sp,h):
    if not os.path.exists(sp):
        os.mkdir(sp)
    for i in range(h):
        u=urllib.request.urlopen(url)
        data=u.read()
        imgPath=sp+r'/%d.png' %(i+int(index))
        with open(imgPath,'wb') as f:
            f.write(data)
def gs(url,bn,h,sp):
    saveSimpleImg(bn,url,sp,h)

#使用方法：
#from lib.GetSimple import gs
StartNumber=1
number=20
#gs("http://xxxxxxxxx",StartNumber,number,"./SimpleImg")

#环境配置：
#pip install -r requirements.txt




