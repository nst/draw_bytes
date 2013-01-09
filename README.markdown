### Drawing Files

You can draw any file as a picture by considering its bytes as pixel values.

draw_bytes.py can read draw a file using 1 (monochrome), 3 (RGB) or 4 (CMYK) bytes for one pixel.

In monochrome mode, draw_bytes.py will represent printable characters in green.

The resulting pictures can be used to detect structures in the file and speed up browsing with a [hexadecimal editor](http://ridiculousfish.com/hexfiend/).

### Usage

    $ python draw_bytes.py -h
    usage: draw_bytes.py [-h] [-n {1,3,4}] src dst
    
    Draw any file as an image.
    
    positional arguments:
      src                   path of the source file
      dst                   path of the destination PNG image
    
    optional arguments:
      -h, --help            show this help message and exit
      -n {1,3,4}, --nb_bytes {1,3,4}
                            number of bytes per pixel

### Typical Usage

    $ python draw_bytes.py -n 3 test.doc test.doc.png && open test.doc.png

### Sample Result

Here are the results for the [RuntimeBrowser](https://github.com/nst/RuntimeBrowser) executable file.

In monochrome, all pixels are in black (`00`), white (`FF`), some shade of gray or, for printable characters, in green (0, 128, 0).

In RGB `00 00 00` is black, `FF FF FF` is white. ASCII text is mostly betwen 40 and 120 and so gets drawn with clear colors.

In CMYK, `00 00 00 00` is white `FF FF FF FF` is black. ASCII text tend to appear in dark.

<img halign="top" src="https://raw.github.com/nst/draw_bytes/master/images/RuntimeBrowser_1.png"> <img halign="top" src="https://raw.github.com/nst/draw_bytes/master/images/RuntimeBrowser_3.png"> <img halign="top" src="https://raw.github.com/nst/draw_bytes/master/images/RuntimeBrowser_4.png">
