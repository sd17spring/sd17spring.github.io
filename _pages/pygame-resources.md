---
title: PyGame Resources with less <span style="color:green">green</span>
date: 2017-02-22 00:00:00 -05:00
permalink: resources/pygame/
description: ''
---

## Foreword

This was written by **Serena Chen** in Spring 2017. If anything is unclear or should be added or changed, feel free to reach out to me over email or
slack.

## Example application:

```python
import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # window size, as a tuple
    pygame.display.set_caption('PyGame App!')

    # change this block of code to do what you want
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user presses the x-button
                running = False

        screen.fill((0,0,0)) # RGB tuple for black
        pygame.display.update()

    pygame.quit()
```

## Pygame Events

* The above example application has this code to read in events

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT: # user presses the x-button
        running = False
```

* `pygame.event.get()` will get you an `EventList`, which you can just treat as
    a list of pygame `Event`
* Each event has a type, which is represented by a constant in pygame.

### Pygame Event Types

*The following bullets assume you have an `Event` called `event`*

* `pygame.QUIT`
    * When the user presses the 'x' button
* `pygame.KEYDOWN`
    * When a user presses a keyboard key
    * `event.key`: the name of the key pressed.
        * If you want to see if a user pressed a certain key (such as the
            letter 'a'), you can write:

            ```python
            if event.key == pygame.K_a:
            ```

        * [Here is a list of pygame key constants](https://www.pygame.org/docs/ref/key.html)
    * `event.unicode`: gets you the actual character that was pressed
    * `event.mod`: state of keyboard modifiers (ex. shift, alt, ctrl, etc).
        Interpreting the number you get requires bitwise ands.
        * There is a list of constants that represent all the modifiers,
            under the list of key constants on
            [this page](https://www.pygame.org/docs/ref/key.html)
        * To check if, for example, 'a' and 'ctrl' are held down, use

            ```python
            if (event.key == pygame.K_a) and (event.mod & pygame.KMOD_CTRL):
            ```

        * I won't get into bitwise operations, but if you really want to
            know, [here is a resource](http://stackoverflow.com/questions/31575691/what-is-a-bitmask-and-a-mask).
* `pygame.KEYUP`
    * When a user lets go of a keyboard key
    * `event.KEY`
    * `event.mod`
    * Those descriptions are the same as above
* `pygame.MOUSEMOTION`
    * When the user moves the mouse in the window
    * `event.pos`: The ending position of the mouse as a tuple, where (0, 0) is
        the top left corner of the screen
    * `event.rel`: Amount of pixels moved, as a tuple (dx, dy)
    * `event.buttons`: The mouse buttons that were held down. It is a tuple like
        (left, middle, right), where each element is 1 if it was held, and 0
        otherwise
* `pygame.MOUSEBUTTONUP` and `pygame.MOUSEBUTTONDOWN`
    * Pressing and letting go of the mouse button
    * They have the same parameters
    * `event.pos`: The position of the mouse as a tuple, where (0, 0) is the top
        left corner of the screen
    * `event.button`: A number that corresponds to the button pressed
        * 1: left mouse button
        * 2: middle mouse button
        * 3: right mouse button
        * 4: scroll up
        * 5: scroll down
* There are lots of other pygame events, but they won't be used as much
    (especially in SofDes).
* [Official Pygame event documentation](https://www.pygame.org/docs/ref/event.html)
* [Pygame's official input handling tutorial](http://pygame.org/ftp/contrib/input.html)

## Commonly used graphics functions:

*All functions assume that you have defined:*
* `screen = pygame.display.set_mode((800, 600))`
* `color = (0,0,0)` -- color is an RGB tuple/list; each element is from 0-255

### Representing a rectangle object:

* `box = pygame.Rect(x, y, width, height)`
    * `x` and `y` are the int coordinates (as pixels) of the **top left
        coordinate**
    * `width` and `height` are integers; width/height in pixels
    * Rectangle objects are used for the `draw_rect` function; they are also
        good for storing the dimensions of a bounding box.
    * Get the dimensions of a rectangle by using
        `rect.x`, `rect.y`, `rect.width`, `rect.height`

### Drawing shapes:

* Line
    * `pygame.draw.line(screen, color, start_pos, end_pos, width=1)`
    * `start_pos` and `end_pos` are tuples like `(x, y)`; they are the pixel
        coordinates
    * `width` is optional; it is the number of pixels thick the line should be
* Rectangle
    * `pygame.draw.rect(screen, color, rect, width=0)`
    * `rect` is a rectangle object; described above
    * `width` is optional; it is the number of pixels thick the line should be
* Ellipse
    * `pygame.draw.ellipse(screen, color, rect, width=0)`
    * `rect` is a rectangle object; described above
    * `width` is optional; it is the number of pixels thick the line should be
* Circle
    * `pygame.draw.circle(screen, color, pos, radius, width=0)`
    * `pos` is the center coordinate, as a tuples
    * `radius` is the radius in pixels
    * `width` is optional; it is the number of pixels thick the line should be
* [Pygame draw documentation](https://www.pygame.org/docs/ref/draw.html)

### On the `blit` function

* The following section will use `screen.blit()`
* This function is used for drawing images, text, and other things
* The official purpose of `blit` is to draw one `Surface` onto another
* A `Surface` is an object that represents some sort of image.
    * `screen`, images, and text are all types of `Surface`

### How to put an image onto the screen:

```python
x = 0, y = 0 # top left x and y
width = 100, height = 100 # desired image width and height

img = pygame.image.load('image.png')
scaled_img = pygame.transform.scale(img, (width, height))
screen.blit(scaled_img, (x, y))
```

[Pygame documentation for transforming images.](https://www.pygame.org/docs/ref/transform.html)
Most of the functions you will need are relatively straightforward.

### How to put text on the screen

```python
x = 0, y = 0 # top left x and y

font = pygame.font.SysFont("monospace", 15) #font name, font size
label = font.render("text", 1, color) # see below
screen.blit(label, (x, y))
```

* Creating a label, given a pygame font named `font`
    * `font.render(text, antialias, color, background=None)`
    * `text` is a string, like above
    * `antialias`: This is a 1 or 0. Simply, this will alter how pixel-y your
        text looks. Either option should be ok; feel free to play with this.
        * If you want to know more about aliasing, see this
            [Wikipedia article](https://en.wikipedia.org/wiki/Aliasing) and this
            [Wikipedia article](https://en.wikipedia.org/wiki/Font_rasterization)
            for information.
    * `background` is optional; you can specify a background color for the text
* If you don't care what font you use, you can replace `"monospace"` above with
    `pygame.font.get_default_font()`
* To see the list of fonts available to you, you can run
    `print(pygame.font.get_fonts())`.
* You can also download a font as a file, and then use that by saying
    `font = pygame.font.Font(filename, size)` where `size` is the font size
