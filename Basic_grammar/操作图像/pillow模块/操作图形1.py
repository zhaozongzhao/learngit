from PIL import Image,ImageFilter

#打开一个jpg图像
#地址 /Users/hnbl009/Desktop/测试图片/5.jpg
im = Image.open('/Users/hnbl009/Desktop/测试图片/5.jpg')

#获得图像尺寸
wide,high = im.size
print('原始图像的大小wide:{},hign:{}'.format(wide,high))

#缩放图像到原来的50%
im.thumbnail((wide//2,high//2))
print('缩小后的图片大小{} {}'.format(wide//2,high//2))

#应用滤镜
im2 = im.filter(ImageFilter.BLUR)


#保存缩小的图片
im2.save('/Users/hnbl009/Desktop/测试图片/8.jpg','jpeg')
