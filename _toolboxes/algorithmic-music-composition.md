---
date: 2017-01-22
description: ''
title: Algorithmic Music Composition
---

{% include toc %}

{% include construction %}

For this toolbox exercise you will be creating a computer program that
composes music! This type of programming is also known as "algorithmic music
composition". You may think that this idea is relatively new, but the history
of algorithmic music composition actually [goes back
to](http://en.wikipedia.org/wiki/Musikalisches_W%C3%BCrfelspiel) Mozart! For a
more recent discussion of algorithmic composition, check out ["The Triumph of
the Cyborg Composer"](http://www.psmag.com/books-and-culture/triumph-of-the-cyborg-composer-8507).

For this exercise you will create a computer program that improvises a blues
solo! You will also be able to experiment with adding a backing track to your
blues solo. Here is an example by one of the best (humans) in the biz

## Get Set

Before you can get started with this exercise, you will need to download a
musical synthesis library for Python. We are going to be using the freely
available library NSound.

First, open up a terminal and execute the following commands to download some
packages that [NSound](http://nsound.sourceforge.net/) requires

    $ sudo apt-get install scons swig portaudio19-dev python2.7-dev python-pygame
vlc

Next, execute the following commands to download, extract, build, and then
install NSound

    $ cd ~/Downloads
    $ wget -O nsound.tar.gz http://downloads.sourceforge.net/project/nsound/nsound/nsound-0.9.2/nsound-0.9.2.tar.gz?r=&ts=1422392088&use_mirror=superb-
    dca2
    $ tar -xvzf nsound.tar.gz
    $ cd nsound-0.9.2
    $ scons setup.py
    $ sudo python setup.py install

Grab the starter code for this toolbox via the normal fork-and-clone method
from <https://github.com//{{site.course.github_owner}}/ToolBox-AlgorithmicMusic>

## Synthesizing Your First Note

Open up the file `blues_solo.py` in your editor. Take a minute to read
through the file and make sure you understand the basic steps that are
happening. Likely, you will want to consult the [NSound
documentation](http://nsound.sourceforge.net/users_guide/basics.html). When
you are comfortable with the given starter code, go ahead and run the Python
script. To playback your composition, open a terminal and execute:

    $ python3 blues_solo.py
    $ cvlc blues_solo.wav

You should hear a _very_  short blues "solo" that consists of one very low note
held for 1 beat (by default we are playing at 45 beats per minute, so the
duration in seconds is 1 1/3 seconds). In order to quit `cvlc`, you should hit
`ctrl-c`.

## Blues Licks

Okay, that wasn't all that impressive, but on the other hand we actually
synthesized a musical note using Python. That's pretty cool! To make our blues
solo more impressive, we need to randomly string together some blues
[licks](http://en.wikipedia.org/wiki/Lick_%28music%29). The basic idea will be
to move up and down the blues scale according to these licks (or musical note
patterns). Here is an example to get you started. We will create a list of
licks. Each lick will contain a list of notes where each note is a list
consisting of an interval (meaning the change in notes on the blues scale from
the previous note) and a duration in beats. For example, the following line
represents a blues lick that consists of four notes. Each note ascends the
blues scale one note and lasts for half a beat:

    licks = [ [ [1,0.5], [1,0.5], [1, 0.5], [1, 0.5] ] ]

Let's modify our code to repeat this lick four times by changing blues_solo.py
in the following way:

``` python
curr_note = 0
add_note(solo, bass, blues_scale[curr_note], 1.0, beats_per_minute, 1.0)
licks = [ [ [1,0.5], [1,0.5], [1, 0.5], [1, 0.5] ] ]
for i in range(4):
    lick = licks[0]
for note in lick:
    curr_note += note[0]
    add_note(solo, bass, blues_scale[curr_note], note[1], beats_per_minute,
1.0)
solo >> "blues_solo.wav"
```

Go ahead and try it! If you then listen to the resultant file **blues_solo.wav** using **cvlc**  you will hear part of a blues scale!

## Add Some Randomness

In order to make things more interesting, you shouldn't always execute the
same lick over and over. First, add at least one more lick to the list (e.g.
you might want to replicate the example lick, but instead descend the blues
scale: `[ [-1, 0.5], [-1, 0.5], [-1, 0.5], [-1, 0.5] ]`). One potentially
helpful guideline (that you should feel free to deviate from!) is to make sure
the duration of the sum of all notes in a lick adds up to 2 (this will keep
the solo "on the beat" and make it sound better when we add a backing track
later).

Once you have added a new lick, modify the line of code `lick = licks[0]` to
choose the lick at random using the function `random.choice` (note that the
function random.choice has already been imported for you in the starter code
as `choice`). Before running your code, you will want to make sure that the
variable `curr_note` doesn't get too high or too low. Make sure you create a
series of if statements to keep the variable from getting less than `0` or
greater than `len(blues_scale) - 1`.

Once you have made these changes, you should make the number of licks larger
(if you followed the code above this number will be at 4) so you can get a
longer solo.

## Tips to Make it Cooler

_Make it
[swing](http://en.wikipedia.org/wiki/Swing_%28jazz_performance_style%29#Rhythm):_
alternate slightly longer and slightly shorter notes in your blues lick to
give it a swing feel (e.g. `[ [1, 0.5*1.1], [1, 0.5*0.9], [1, 0.5*1.1], [1,
0.5*0.9] ]` )

_Avoid hammering the lowest or highest note:_ the code we added to avoid going
out of bounds of the list `blues_scale` has the effect of sometimes hammering
the notes at the boundaries repeatedly. The solo may sound better if you
simply hold the note to the end of the lick if you reach the beginning or end
of the list `blues_scale`.

_Add a backing track_: **NSound** can mix together various audio streams.
In order to add a backing track to your solo, replace the line of your program
that writes the solo to a WAV file (`solo >> "blues_solo.wav"`) with:

``` python
backing_track = AudioStream(sampling_rate, 1)
Wavefile.read('backing.wav', backing_track)

m = Mixer()

solo *= 0.4 # adjust relative volumes to taste
backing_track *= 2.0

m.add(2.25, 0, solo) # delay the solo to match up with backing track
m.add(0, 0, backing_track)

m.getStream(500.0) >> "slow_blues.wav"
```

The solo should stay on the beat of the backing track, but won't really do a
good job tracking chord changes. Note that the name of the output has been
changed from `blues_solo.wav` to `slow_blues.wav`.

_Add some dynamics:_ in the basic version of the code, we always use the same
volume. You may want to play around with adding licks with increasing or
decreasing volume (known as crescendo and decrescendo respectively).

_Move beyond simple intervals:_ in the basic version of the code, the lick is
always defined in terms of changes from the previous note. It may sound good
to start the lick from a specific note on the blues scale. For instance, you
may define a lick that starts on note 6 of the list `blues_scale`. Notes 0, 6,
12, and 18 are special in that they are the root or (tonic note) of the blues
scale. It may sound cool for the lick to start on these notes.

## Completing the Toolbox Exercise

To complete the toolbox exercise, you should complete all of the steps up to
**Make it Cooler**, and then at least one of the extensions suggested in the
**Make it Cooler** section. When you are done, push your code to your repo and
submit a pull request. You should schedule a quick meeting to play your sweet
tunes for a NINJA and get checked off.
