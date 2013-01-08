#!/usr/bin/python

import Image, ImageDraw # http://pypi.python.org/pypi/PIL
import struct
import os
import sys

def image_with_file_at_path(path, img_mode):

    chunks_length = None

    if img_mode == "RGB":
        chunks_length = 3
    elif img_mode == "CMYK":
        chunks_length = 4
    else:
        return None

    nb_bytes = os.path.getsize(path)
    nb_points = nb_bytes / chunks_length
    
    if nb_bytes < chunks_length:
        print "%d bytes found, at least %d bytes needed" % (nb_bytes, chunks_length)
        return None
    
    W = 256
    H = nb_points / W
    if (nb_points % W != 0):
        H += 1
    
    print "%d Bytes" % nb_bytes
    print "%d x %d pixels" % (W, H)

    img = Image.new(img_mode, (W, H), "black")
    draw = ImageDraw.Draw(img)
    
    f = open(path, "rb")
    
    s = "B" * chunks_length
    
    while(nb_bytes - f.tell() >= chunks_length):
        
        values = struct.unpack(s, f.read(chunks_length))
    
        pixels_count = f.tell() / chunks_length - 1
        x = pixels_count % W
        y = pixels_count / W
        
        draw.point((x,y), values)
        
    f.close()
    
    return img

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "USAGE:", sys.argv[0], "IN_FILE OUT_FILE && open OUTFILE"
        sys.exit(1)

#    img = image_with_file_at_path(sys.argv[1], "RGB")
    img = image_with_file_at_path(sys.argv[1], "CMYK")

    if not img:
        sys.exit(1)
    
    img = img.convert('RGB')
    img.save(sys.argv[2], "PNG")
