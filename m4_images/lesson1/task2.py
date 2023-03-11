from PIL import Image, ImageFilter


with Image.open('ufo.png') as file:
    file_gray = file.convert('L')
    file_gray.show()

    file_blured = file.filter(ImageFilter.BLUR)
    file_blured.show()

    pic_up = file.transpose(Image.ROTATE_90)
    pic_up.show()

    file_gray.save('gray.jpg')