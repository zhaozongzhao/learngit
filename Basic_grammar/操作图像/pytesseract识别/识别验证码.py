from PIL import Image
import pytesseract
im = Image.open('/Users/hnbl009/Desktop/测试图片/1.png')
aa = pytesseract.image_to_string(im)
print(aa)