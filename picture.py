#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:50:55 2017

@author: no1
"""


import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--file',default='4.jpg')

args = parser.parse_args()
imgpath = args.file

ascii_char = ['@','#','$','%','*','/',',','.',' ']

                  
def select_ascii_char(r, g, b): 
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16) 
    unit = 256.0/len(ascii_char) 
    return ascii_char[int(gray/unit)]


def output(imgpath, width=100, height=100): 
    im = cv2.imread(imgpath) 
    im = cv2.resize(im,(width, height)) 
    txt = "" 
    for h in range(height):
        for w in range(width): 
            r,g,b=im[h,w,:3]
            txt += select_ascii_char(r,g,b)
            
        txt += '\n' 
    return txt

def save_as_txtfile(txt):
    with open('imgtochar.txt', 'w') as f:
        f.write(txt)
        
if __name__ == '__main__':
    save_as_txtfile(output(imgpath, 300, 300))

