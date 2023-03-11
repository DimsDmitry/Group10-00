from PIL import Image

with Image.open('ufo.png') as file:
    print('Размер:', file.size)
    print('Формат:', file.format)
    print('Тип:', file.mode)
    file.show()
