from PIL import Image, ImageDraw, ImageFont

class AddWaterMark():
    def __init__(self, image_path):
        self.input_image = Image.open(image_path) # creating a new object image
        self.input_image = self.input_image.convert('RGBA') # convert the image in RGBA
        self.width, self.height = self.input_image.size # Get the size (width,height)
        self.watermarked_image = Image.new('RGBA', self.input_image.size, color=(255,255,255,0))

    def add_watermark_overlay (self, watermark_text):

        overlay = Image.new('RGBA', self.input_image.size, color=(255,255,255,0)) # create overlay image - white and transparent

        draw = ImageDraw.Draw(overlay) # creating an object to draw on the new overlay image

        watermark_color_pattern = (255, 255, 255, 30)
        # draw a line from top left to bottom right
        for i in range(0,self.width + self.height, 50):
            draw.line([(0, self.height -i ),(i, self.height)], fill=watermark_color_pattern, width=5)

        w, h = self.input_image.size
        x, y = int(w / 2), int(h / 2)
        if x > y:
            font_size = y
        else:
            font_size = x

        font = ImageFont.truetype('arial.ttf', int(font_size / 2))

        text_width , text_height = draw.textlength(watermark_text, font=font), font_size

        # getting the center of the image
        x = (self.width - text_width) //2
        y = (self.height - text_height) // 2

        watermark_color_text = (255, 255, 255, 80)

        draw.text((x,y), watermark_text, fill=watermark_color_text,font=font)

        self.watermarked_image = Image.alpha_composite(self.input_image, overlay)




