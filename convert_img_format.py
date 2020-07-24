from PIL import Image
import glob

CITY = 'benut'
TYPE = 'restaurant'

# convert JPEG (.jpg) to JPEG 2000 (.jp2) and WebP (.webp)
for image in glob.glob(f'./static/image/{CITY}/{TYPE}/*.jpg'):
    im = Image.open(image).convert("RGB")
    im.save(image[:-3] + 'webp', "webp")
    # print(image[:-3])

# # for a single images
# im = Image.open('./static/image/altImg.png').convert("RGB")
# im.save('./static/image/altImg.webp', 'webp')