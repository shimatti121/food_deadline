#必要なモジュールインポート
from PIL import Image

import os
import pyocr
import cv2
import numpy as np
import re

#環境変数「PATH」にTesseract-OCRのパスを設定。
#Windowsの環境変数に設定している場合は不要。
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

def gray_ocr11(image):
  img_gray = cv2.imread(image,0)
  cv2.imwrite('gray.jpg',img_gray)
  img = Image.open('gray.jpg')
  txt = tool.image_to_string(img,lang='jpn',builder=pyocr.builders.TextBuilder(tesseract_layout=11))
  A = {}
  A = np.zeros(3)
  pattern1 = '(\d{2}|\d{4})\.(\s*(\d{2}|\d{1}))\.(\s*(\d{2}|\d{1}))'

  result = re.search(pattern1, txt)
  try:
    print(result.group())
    #print(result.group(1))
    #print(result.group(2))
    #print(result.group(3))
  except AttributeError:
    print('うまく読み込めませんでした．')

    return A
  A[0]=int(result.group(1))
  if A[0] > 999:
    A[0] = A[0]-(int(A[0]/1000)*1000)
  A[1]=int(result.group(3))
  A[2]=int(result.group(5))
  return A

B = []
B.append(gray_ocr11('zeri.jpg'))
B.append(gray_ocr11("salad_chicken.jpg"))
B.append(gray_ocr11("you.jpg"))
B.append(gray_ocr11("chicken2.jpg"))
B.append(gray_ocr11("kosyou.jpg"))
B.append(gray_ocr11("chicken.jpg"))
print(B)
sorted_data = sorted(B, key=lambda x:(x[0], x[1], x[2]))
print(sorted_data)

      
