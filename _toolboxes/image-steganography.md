---
title: Image Steganography
date: 2017-02-14 00:00:00 -05:00
description: ''
---

{% include toc %}

In this toolbox exercise you will delve a bit deeper into the specifics of how images are created in addition to learning more about bits and binary math. This exercise was modified from [Interactive Python](http://interactivepython.org/runestone/static/everyday/2013/03/1_steganography.html), though this version encodes an image into another image instead of ASCII text.

To complete this toolbox, you will need to write two functions. The first is a decoding function that can extract secret information from an image file, while the second is a function that can encode secret messages into images.

Grab the starter code for this toolbox exercise via the normal fork-and-clone method from <https://github.com//{{site.data.course.github_owner}}/ToolBox-ImageSteganography>. The starter code
is in `steganography.py`.

## Get Set

This toolbox uses the [Python Pillow library](https://pillow.readthedocs.io/en/4.0.x/reference/Image.html). You should already have this installed on your system from the Computational Art mini-project, but go ahead and install it using pip3 if it's missing.

## What is steganography?

In a nutshell, the main goal of [steganography](https://en.wikipedia.org/wiki/Steganography) is to hide information within data that doesn't appear to be secret at a glance. For example, this sentence:

`Since everyone can read, encoding text in neutral sentences is definitely effective`

turns into

`Secret inside`

if you take the first letter of every word. Steganography is really handy to use, because people won't even suspect that they're looking at a secret message--making it less likely that they'll want to try to crack your code. In the past, you may have tried to accomplish this kind of subterfuge using invisible inks or using special keywords with your friends. However, as fearless coders we have access to fancier ways to sneak data around.

## The value of one pixel

There are multiple ways to hide things within other things, but today we will be working with images. A black and white image (not greyscale) is an easy thing to conceptualize, where a black pixel has a value of 1 and a white pixel as a value of 0.

Color images have three color channels (RGB), with pixel values of 0-255 for each pixel. So a pixel with the value (255,255,255) would be entirely white while (0,0,0) would be black. The upper range is 255 because it is the largest value that can be represented by an 8 bit binary number. Binary is a base-two paradigm, in contrast to decimal which is in base-ten, which means you calculate the value of a binary number by summing the 2s exponent of each place where a 1 appears.

So if we wanted to convert the number `10001011` from binary into decimal, it would look something like:

`2^8 + 2^4 + 2^2 + 2^1 = 139`

You can also test this out in your Python interpreter. Binary numbers are automatically converted to integers so you don't actually need to have a print statement. (It's just there for clarity.)

```python
>>> print(0b10001011)
139
>>> type(0b10001011)
<class 'int'>
>>> 0b00001011
11
>>> 0b10001010
138
```

From our quick tests above, you can see that the leftmost bit place matters a lot more than rightmost bit because the rightmost bit only modifies the value of the number by 1. We saw that:

`10001011 = 139` while `00001011 = 11`
`10001011 = 139` while `10001010 = 138`

Because of this, we describe the leftmost bit as the "most significant bit" (MSB) while the rightmost bit is the "least significant bit" (LSB).

We can observe that its entirely possible to hide a black and white image inside an RGB image by changing the LSB of a pixel in a single color channel to correspond to the value of the image we want to hide.

Additionally, since changing the LSB doesn't drastically change the overall value of the of 8 bit number, we can hide our data without modifying a source image in any detectable sort of way. You can test this out with any [RGB color wheel](http://www.colorspire.com/rgb-color-wheel/) to get a sense of how little difference there is between a color like (150, 50, 50) and (151, 50, 50)

**Aside**

The concept of MSB and LSB occurs in other contexts as well. For example, [parity bits](https://en.wikipedia.org/wiki/Parity_bit) are used as a basic form of error checking. Additionally, because the LSBs will change rapidly even if the value of the bit changes a little, they are very useful for use in [hash functions](https://en.wikipedia.org/wiki/Hash_function) and [checksums](https://en.wikipedia.org/wiki/Checksum) for validation purposes.

## Decoding the sample image

Provided in this toolbox is a picture of a cute dog. However, this dog is hiding a very secret message... can you decode it? This image is also included in the toolbox under images/encoded_sample.png.

![]({% link images/toolboxes/image-steganography/encoded_sample.png %}){:width="400px" height="351px"}

Provided in the starter code is a function called `decode_image()`. The secret image was hidden in the LSB of the pixels in the red channel of the image. That is, the value of the LSB of each red pixel is 1 if the hidden image was 1 at that location, and 0 if the hidden image was also 0. Your task is to iterate though each pixel in the encoded image and set the decode_image pixel to be (0, 0, 0) or (255, 255, 255) depending on the value of that LSB.

You may want to look at the Python [bin](https://docs.python.org/3/library/functions.html#bin) function as you convert between integer and binary. Remember that bin will convert an integer to a *binary string*. Also, remember that you have to isolate the red_channel from the original RGB image. You can do this using the .split() function that PIL provides.

```python
def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    #TODO: Fill in decoding functionality

    decoded_image.save("images/decoded_image.png")
```

* Note that files in this example are .png files. We recommend that you avoid working with .jpg files so that file compression does not make your task more difficult.

## Encoding a secret message

Now that we can decode secret messages, it's only natural that we want to encode some too! Provided in the starter code are a pair of functions called `write_text()` and `encode_image()`. `write_text()` will take a string and convert it to a black and white image of the string. You may use it as a helper function in completing your implementation of `encode_image()`.

## Completing the Toolbox Exercise

You will need three things to complete this assignment:

1. Completed steganography.py code
2. Decoded image obtained from encoded_sample.png
3. A sample image with some encoded message in it from your encode_image() function

Commit all three things to your GitHub repo and submit a pull request to turn in this toolbox.
