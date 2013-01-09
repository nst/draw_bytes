#!/usr/bin/python

import Image, ImageDraw # http://pypi.python.org/pypi/PIL
import struct
import os
import sys
import string
import argparse

def image_with_file_at_path(path, nb_bytes):

    if nb_bytes in [1, 3]:
        img_mode = "RGB"
    elif nb_bytes == 4:
        img_mode = "CMYK"
    else:
        return
    
    nb_total_bytes = os.path.getsize(path)
    nb_points = nb_total_bytes / nb_bytes
    
    if nb_total_bytes < nb_bytes:
        print "%d bytes found, at least %d bytes needed" % (nb_total_bytes, nb_bytes)
        return None
    
    W = 256
    H = nb_points / W
    if (nb_points % W != 0):
        H += 1
    
    print "%d Bytes" % nb_total_bytes
    print "%d x %d pixels" % (W, H)

    img = Image.new(img_mode, (W, H), "black")
    draw = ImageDraw.Draw(img)
    
    f = open(path, "rb")
    
    s = "B" * nb_bytes
        
    while(nb_total_bytes - f.tell() >= nb_bytes):
        
        values = struct.unpack(s, f.read(nb_bytes))
        
        if nb_bytes == 1:
            c = "%c" % values[0]
            values = (0, 128, 0) if c in string.printable else values*3
        
        pixels_count = f.tell() / nb_bytes - 1
        x = pixels_count % W
        y = pixels_count / W
        
        draw.point((x,y), values)
        
    f.close()
    
    return img

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Draw any file as an image.')
    parser.add_argument('-n','--nb_bytes', help='Number of bytes per pixel', choices=[1,3,4], default=3, required=False, type=int)
    parser.add_argument('src', help='Path of the source file')
    parser.add_argument('dst', help='Path of the destination PNG image')
    args = vars(parser.parse_args())

    #print args

    img = image_with_file_at_path(args['src'], args['nb_bytes'])

    if not img:
        print "-- can't build image, exit"
        sys.exit(1)
    
    img = img.convert('RGB')
    img.save(args['dst'], "PNG")
