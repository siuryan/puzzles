from PIL import Image, ImageDraw
import glob, os, statistics

im = Image.new('1', (200,200))
with open("coordinates.txt") as coords_fp:
    coords = [(int(coord.split(',')[0].strip('(')), int(coord.split(',')[1].strip(' )\n'))) for coord in coords_fp.readlines()]
    
    lego_ims = sorted(glob.glob("archive/legos/*.jpg"))
    for i, infile in enumerate(lego_ims):
        with Image.open(infile) as lego_im:
            if lego_im.getchannel("R").getdata()[0] == 0:
                im.putpixel(coords[i], 1)
            else:
                im.putpixel(coords[i], 0)
                
with open("generated_qr.jpg", 'w') as qr_fp:
    im.save(qr_fp)
    


    
