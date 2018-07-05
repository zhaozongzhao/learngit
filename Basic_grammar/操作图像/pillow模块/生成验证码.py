from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random

class generate_random():



    def random_char(self):
        return chr(random.randint(65,90))#chr根据生成的数字按照asII码,生成字母)

    def random_color(self):
        return  (random.randint(64,255),random.randint(64,255),random.randint(64,255))

    def random_color2(self):
        return  (random.randint(32,127),random.randint(32,127),random.randint(32,127))

    def generate_validation(self,width,height):

        image = Image.new('RGB',(width,height),(255,182,193))
        #创建font对象
        font = ImageFont.truetype('Arial.ttf',36)
        #创建一个draw对象
        draw  = ImageDraw.Draw(image)
        #填充像素
        for x in range(width):
            for y in range(height):
                draw.point((x,y),fill=self.random_color())

        #输出文字
        for t in range(4):
            draw.text((60*t+10,10),self.random_char(),font=font,fill=self.random_color2())

        # image = image.filter(ImageFilter.BLUR)
        image.save('/Users/hnbl009/Desktop/测试图片/10.jpg')




if __name__ == '__main__':

    gr = generate_random()
    print(gr.random_char(),gr.random_color(),gr.generate_validation(240,60))



