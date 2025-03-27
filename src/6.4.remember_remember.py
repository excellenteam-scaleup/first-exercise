from PIL import Image


def remember_remember(img_path):
    with Image.open(img_path) as img:
        width, height = img.size
        blackThresh = 10
        message = ""
        for x in range(width):
            for y in range(height):
                if img.getpixel((x, y)) < blackThresh:
                    message += chr(y)
                    break  # Only one black pixel per column
        return message
