"""
We need to 
1. read in qr and determine black pixel coordinates
2. read in dataset images
3. for each image, randomly assign coordinate and save new image
   a. if black, make image "fake"
   b. if white, leave image
4. output list of coordinates
"""

from PIL import Image, ImageDraw
import glob, os, random

QR_IMAGE_FILE = "qr.png"
QR_IMAGE_SIZE = (200, 200)
DATASET_DIR = "archive/dataset"
IMAGE_OUTPUT_DIR = "archive/legos"

# step 1
def get_qr_coordinates_color_map():
    qr_image = Image.open(QR_IMAGE_FILE)
    coordinates_color_map = {}  # (x, y): True if black, False if white
    for x in range(QR_IMAGE_SIZE[0]):
        for y in range(QR_IMAGE_SIZE[1]):
            pixel_data = qr_image.getpixel((x, y))
            if pixel_data[0] == 0 and pixel_data[1] == 0 and pixel_data[2] == 0:
                coordinates_color_map[(x,y)] = True
            elif pixel_data[0] == 255 and pixel_data[1] == 255 and pixel_data[2] == 255:
                coordinates_color_map[(x,y)] = False
            else:
                raise Exception("Color is not white or black")
    return coordinates_color_map

# steps 2-4
def process_images(qr_coordinates_color_map):
    coords_list = []
    shuffled_map = list(qr_coordinates_color_map.items())
    random.shuffle(shuffled_map)
    for i, infile in enumerate(glob.glob(os.path.join(DATASET_DIR, "*.png"))):
        with Image.open(infile) as im:
            coords, is_black = shuffled_map.pop()
            if is_black:
                draw = ImageDraw.Draw(im)
                draw.line((0, 0) + im.size, fill=128, width=5)
                draw.line((0, im.size[1], im.size[0], 0), fill=128, width=5)
            new_filename = os.path.join(IMAGE_OUTPUT_DIR, stringify(i) + ".jpg")
            with open(new_filename, 'w') as new_f:
                im.save(new_filename, 'JPEG')
            coords_list.append(coords)
    return coords_list

def stringify(i):
    i = str(i)
    while len(i) < len(str(QR_IMAGE_SIZE[0] * QR_IMAGE_SIZE[1])):
        i = '0' + i
    return i

if __name__ == "__main__":
    coords = process_images(get_qr_coordinates_color_map())
    for coord in coords:
        print (coord)
