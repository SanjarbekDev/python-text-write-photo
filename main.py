from PIL import Image, ImageFont, ImageDraw 

newphoto="yangifoto"

def editor():
    my_image = Image.open("image_temp.jpg")
    title_font = ImageFont.truetype('Mulish_wght.ttf', 50)
    title_text = "Hello my photo editor"
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
    my_image.save(f'{newphoto}.jpg')

def main():
   editor()
       
main()    

    
    