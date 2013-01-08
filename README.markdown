### Drawing Files

You can draw a picture of any file by reading chunks of 3 bytes and using them as RGB values.

Or you can read 4 bytes and use them as CMYK values.

The resulting pictures can be used to detect structures in the file and speed up browsing with a [hexadecimal editor](http://ridiculousfish.com/hexfiend/).

### Usage

    $ python draw_bytes.py test.doc test.doc.png && open test.doc.png

### Sample Result

Here is the result for the [RuntimeBrowser](https://github.com/nst/RuntimeBrowser) executable file.

In RGB `00 00 00` is black, `FF FF FF` is white. ASCII text is mostly betwen 40 and 120 and so gets drawn with clear colors.

In CMYK, `00 00 00 00` is white `FF FF FF FF` is black. ASCII text tend to appear in dark.

![RuntimeBrowser RGB visualization](https://raw.github.com/nst/draw_bytes/master/images/RuntimeBrowser_RGB.png)

![RuntimeBrowser CMYK visualization](https://raw.github.com/nst/draw_bytes/master/images/RuntimeBrowser_CMYK.png)
