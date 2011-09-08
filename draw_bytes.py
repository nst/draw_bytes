#!/usr/bin/python

import Image, ImageDraw # http://pypi.python.org/pypi/PIL
import struct
import os
import sys

def image_with_file_at_path(path):
    nb_bytes = os.path.getsize(path)
    nb_points = nb_bytes / 3
    
    if nb_bytes < 3:
        print "%d bytes found, at least 3 bytes needed" % nb_bytes
        return None
    
    W = 256
    H = nb_points / W
    if (nb_points % W != 0):
        H += 1
    
    print "%d Bytes" % nb_bytes
    print "%d x %d pixels" % (W, H)
    
    img = Image.new("RGB", (W, H), "black")
    draw = ImageDraw.Draw(img)
    
    f = open(path, "rb")
    
    while(nb_bytes - f.tell() >= 3):
    
        r,g,b = struct.unpack("BBB", f.read(3))
    
        pixels_count = f.tell() / 3 - 1
        x = pixels_count % W
        y = pixels_count / W
        
        draw.point((x,y), (r,g,b))
        
    f.close()
    
    return img

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "USAGE:", sys.argv[0], "IN_FILE OUT_FILE && open OUTFILE"
        sys.exit(1)

    img = image_with_file_at_path(sys.argv[1])

    if not img:
        sys.exit(1)
    
    img.save(sys.argv[2], "PNG")
