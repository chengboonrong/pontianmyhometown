from PIL import Image
import glob

# convert JPEG (.jpg) to JPEG 2000 (.jp2) and WebP (.webp)
# for image in glob.glob('./static/image/atm/*.jpg'):
#     im = Image.open(image).convert("RGB")
#     im.save(image[:-3] + 'webp', "webp")
#     # print(image[:-3])

im = Image.open('./static/image/altImg.png').convert("RGB")
im.save('./static/image/altImg.webp', 'webp')