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
    bytes = f.read()
    f.close()
    
    i = 0
    
    s = "B" * nb_bytes

    while((i + nb_bytes) <= nb_total_bytes):
        
        values = struct.unpack(s, bytes[i:i+nb_bytes])
        
        if nb_bytes == 1:
            c = "%c" % values[0]
            values = (0, 128, 0) if c in string.printable else values*3
        
        pixels_count = i / nb_bytes
        
        x = pixels_count % W
        y = pixels_count / W
        
        draw.point((x,y), values)

        i += nb_bytes
    
    return img

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Draw any file as an image.')
    parser.add_argument('-n','--nb_bytes', help='number of bytes per pixel', choices=[1,3,4], default=3, required=False, type=int)
    parser.add_argument('src', help='path of the source file')
    parser.add_argument('dst', help='path of the destination PNG image')
    args = vars(parser.parse_args())

    #print args

    img = image_with_file_at_path(args['src'], args['nb_bytes'])

    if not img:
        print "-- can't build image, exit"
        sys.exit(1)
    
    img = img.convert('RGB')
    img.save(args['dst'], "PNG")
