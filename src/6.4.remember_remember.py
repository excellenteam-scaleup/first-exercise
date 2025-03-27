from PIL import Image


def remember_remember(img_path):
    with Image.open(img_path) as img:
        width, height = img.size
        blackThresh = 10
        for y in range(height):
            for x in range(width):
                if img.getpixel((x, y)) < blackThresh:
                    print(chr(y), end="")


remember_remember('code.png')
