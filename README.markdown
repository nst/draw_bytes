### Drawing Files

You can draw a picture of any file by reading chunks of 3 bytes and using them as RGB values.

The resulting pictures can be used to detect structures in the file and speed up browsing with a [hexadecimal editor](http://ridiculousfish.com/hexfiend/).

### Usage

    $ python draw_bytes.py test.doc test.doc.png && open test.doc.png

### Sample Result

Here is the result for the [RuntimeBrowser](https://github.com/nst/RuntimeBrowser) executable file.

`000000` is white, `FFFFFF` is black. ASCII text is mostly betwen 40 and 120 and so gets drawn with clear colors.

![RuntimeBrowser binary file](https://raw.github.com/nst/draw_bytes/master/images/RuntimeBrowser.png)

