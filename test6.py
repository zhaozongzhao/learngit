from PIL import Image
pw,ph  = 64,64
w,h = 100,200

li = Image.open('/Users/hnbl009/gitfile/selenium3.0/webdriverAPI接口/截图/1.jpg')
print([li.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)])

