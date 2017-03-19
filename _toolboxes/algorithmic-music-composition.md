---
date: 2017-03-18
description: ''
title: Algorithmic Music Composition
---

{% include toc %}

For this toolbox exercise you will be creating a computer program that
composes music! This type of programming is also known as "algorithmic music
composition". You may think that this idea is relatively new, but the history
of algorithmic music composition actually [goes back
to](http://en.wikipedia.org/wiki/Musikalisches_W%C3%BCrfelspiel) Mozart! For a
more recent discussion of algorithmic composition, check out ["The Triumph of
the Cyborg Composer"](http://www.psmag.com/books-and-culture/triumph-of-the-cyborg-composer-8507).

For this exercise you will create a computer program that improvises a blues
solo! You will also be able to experiment with adding a backing track to your
blues solo. Here is an example by one of the best (humans) in the biz:

<iframe class="youtube-player" width="560" height="315" src="https://www.youtube.com/embed/MpRIYi721WE" frameborder="0" allowfullscreen></iframe>


## Get Set

Before you can get started with this exercise, you will need to download
(1) the
[Sonic Pi](http://sonic-pi.net) music synthesis program, and
(2) a [Python library](https://github.com/gkvoelkl/python-sonic) that lets you control **Sonic Pi** from Python.

First, open up a terminal and execute the following commands:

    $ sudo apt-get install sonic-pi
    $ sudo pip3 install python-sonic

Grab the starter code for this toolbox via the normal fork-and-clone method
from <https://github.com//{{site.course.github_owner}}/ToolBox-AlgorithmicMusic>.

## Synthesizing Your First Note

Open up the file `blues_solo.py` in your editor. Take a minute to read
through the file and make sure you understand the basic steps that are
happening.

When you are comfortable with the given starter code, go ahead and run the
Python script. Launch **Sonic Pi**, and then open a terminal and execute:

    $ python3 blues_solo.py

You should hear a _very_ short blues "solo" that consists of one very low note
held for 1 beat. (By default we are playing at 45 beats per minute, so the
duration in seconds is 1 1/3 seconds.)

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

    licks = [[(1, 0.5), (1, 0.5), (1, 0.5), (1, 0.5)]]

Let's modify our code to repeat this lick four times by changing `blues_solo.py`
in the following way:

``` python
curr_note = 0
play_note(blues_scale[curr_note], 1, beats_per_minute)
licks = [[(1, 0.5), (1, 0.5), (1, 0.5), (1, 0.5)]]
for _ in range(4):
    lick = licks[0]
    for note in lick:
        curr_note += note[0]
        add_note(blues_scale[curr_note], note[1], beats_per_minute)
```

Go ahead and try it! You will hear part of a blues scale!

## Add Some Randomness

In order to make things more interesting, you shouldn't always execute the
same lick over and over. First, add at least one more lick to the list (*e.g.*
you might want to replicate the example lick, but instead descend the blues
scale: `[(-1, 0.5), (-1, 0.5), (-1, 0.5), (-1, 0.5)]`). One potentially
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

_Make it [swing](http://en.wikipedia.org/wiki/Swing_%28jazz_performance_style%29#Rhythm):_
alternate slightly longer and slightly shorter notes in your blues lick to
give it a swing feel (*e.g.*
`[(1, 0.5 * 1.1), (1, 0.5 * 0.9), (1, 0.5 * 1.1), (1, 0.5 * 0.9)]`)

_Avoid hammering the lowest or highest note:_ the code we added to avoid going
out of bounds of the list `blues_scale` has the effect of sometimes hammering
the notes at the boundaries repeatedly. The solo may sound better if you
simply hold the note to the end of the lick if you reach the beginning or end
of the list `blues_scale`.

_Add a backing track_: **Sonic Pi** can mix together various audio streams.
In order to add a backing track to your solo, add this to the beginning of
your program:

``` python
BACKING_TRACK = os.path.join(SAMPLES_DIR, "backing.wav")
sample(BACKING_TRACK, amp=2)
sleep(2.25)  # delay the solo to match up with backing track
```

The solo should stay on the beat of the backing track, but won't really do a
good job tracking chord changes.

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
