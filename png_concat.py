from PIL import Image
import time

start = time.time()

image00 = Image.open('../demo/heights00-1.png')
image01 = Image.open('../demo/heights01-1.png')
image10 = Image.open('../demo/heights10-1.png')
image11 = Image.open('../demo/heights11-1.png')

blank_image = Image.new("RGB", (1000, 1000))

blank_image.paste(image00, (0, 500))
blank_image.paste(image01, (0, 0))
blank_image.paste(image10, (500, 500))
blank_image.paste(image11, (500, 0))

blank_image.save('../demo/heights1.png')

end = time.time()
print(end - start)
