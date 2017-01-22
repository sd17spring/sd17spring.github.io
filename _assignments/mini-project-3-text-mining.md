---
date: 2017-01-18 08:44:07 -0500
description: ''
due_date: '2017-02-22'
title: 'Mini Project 3: Text Mining and Analysis'
toc: true
---

{% include toc %}

## Introduction

In this assignment you will learn how to use computational techniques to
analyze text. Specifically, you will access text from the web and social media
(such as Twitter and Facebook), run some sort of computational analysis on it,
and create some sort of deliverable (either some interesting results from a
text analysis, a visualization of some kind, or perhaps a computer program
that manipulates language in some interesting way).

## Skills Emphasized:

* Accessing information on the Internet programmatically
* Parsing text and storing it in relevant data structures
* Choosing task-appropriate data structures (e.g. dictionaries versus lists)
* Computational methods for characterizing and comparing text

## How to proceed

In order to get started on the assignment, you should fork the [base
repository](https://github.com//{{site.course.github_owner}}/TextMining) for the text mining and
analysis mini-project. Once you've forked the repository, clone the repository
on your computer.

You should read this document in a somewhat non-linear/spiral fashion:

1. Scan through [Part 1\]({% link _assignments/mini-project-3-text-mining.md %}#part-1-harvesting-text-from-the-internet) to get a sense of what data sources are available. Try grabbing text from one of the sources that interests you. You **do not**  need to try all the data sources.
2. Scan through [Part 2\]({% link _assignments/mini-project-3-text-mining.md %}#part-2-analyzing-your-text) to see a bunch of cool examples for what you can do with your text.
3. Choose (at least) one data source from Part 1 or elsewhere and analyze/manipulate/transform that text using technique(s) from Part 2 or elsewhere.
4. Write a brief document about what you did ([Part 3\]({% link _assignments/mini-project-3-text-mining.md %}#part-3-project-writeup-and-reflection))

## Part 1: Harvesting text from the Internet

The goal for Part 1 is for you to get some text from the Internet with the aim
of doing something interesting with it down the line. As you approach the
assignment, I recommend that you get a feel for the types of text that you can
grab using Pattern. However, before spending too much time going down a
particular path on the text acquisition component, you should look ahead to
Part 2 to understand some of the things you can do with text you are
harvesting. The strength of your mini project will be in combining a source of
text with an appropriate technique for language analysis (see Part 2).

### Preliminaries

You are not required to use any particular Python package to complete this
assignment, however, there is one framework which I will strongly suggest that
you utilize. This is the fantastic web-mining tool called
[Pattern](http://www.clips.ua.ac.be/pattern) by Tom de Smedt. To get the
package, run:

`$ sudo pip3 install pattern`

To make sure that Pattern is installed correctly, try these commands in
Python:

    >>> from pattern.web import *
    >>> print URL('http://google.com').download()


If Pattern is installed correctly, you should see the HTML from Google's front
page. If you'd like to learn more about what is going on behind the scenes,
check out the [Web APIs Project Toolbox\]({% link _toolboxes/geocoding-and-web-apis.md %}) assignment.

By default, Pattern uses a common license key for every user. If you use the
common license keys, then you will be subject to service denials if the a
particular search engine gets hit with the same license key too many times.

After you have chosen which data source you would like to use, follow the
directions [here](http://www.clips.ua.ac.be/pages/pattern-web#license) to get
personal license keys. When you make a Pattern query you can provide your
personal key as an argument, e.g. `license='123ABC_MY_ LICENCE...'`. To default
to using your personal keys, you can edit `/usr/local/lib/python2.7/dist-
packages/pattern/web/api.py` (assuming you installed with `pip`). Make sure to
start a new Python interpreter for your changes to take effect.

### Data Source: Project Gutenberg

[Project Gutenberg](http://www.gutenberg.org/) is a website that has 42,000
freely available e-books. In contrast to some sites (sorry no link), this site
is 100% legal since all of these texts are no longer under copyright
protection. For example, the website boasts 171 works by Charles Dickens.
Perhaps the best thing about the texts on this site is that they are available
in plain text format, rather than PDF which would require some additional
computational processing to process in Python.

In order to download a book from Project Gutenberg you should first use their
search engine to find a link to a book that you are interested in analyzing.
For instance, if I decide that I want to analyze _Oliver Twist_  I would click
on this [link](http://www.gutenberg.org/ebooks/730) from the Gutenberg search
engine. Next, I would copy the link from the portion of the page that says
"Plain Text UTF-8". It turns out that the link to the text of _Oliver Twist_
is `http://www.gutenberg.org/ebooks/730.txt.utf-8`. To download the text
inside Python, I would use the following code:

``` python
from pattern.web import *
oliver_twist_ full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
print oliver_ twist_full_ text
```

Note, that there is a preamble (boiler plate on Project Gutenberg, table of
contents, etc.) that has been added to the text that you might want to strip
out (potentially using Python code) when you do your analysis (there is
similar material at the end of the file). The one complication with using
Project Gutenberg is that they impose a limit on how many texts you can
download in a 24-hour period (which lead to me getting banned the other day).
So, if you are analyzing say 10 texts, you might want to download them once
and load them off disk rather than fetching them off of Project Gutenberg's
servers every time you run your program (see the [Pickling Data\]({% link _assignments/mini-project-3-text-mining.md %}#pickling-data) section for some relevant
information on doing this). However, there are
[many](http://www.gutenberg.org/MIRRORS.ALL)
[mirrors](http://onlinebooks.library.upenn.edu/) of the Project Gutenberg site
if you want to get around the download restriction.

### Data Source: Google

Another source of data that you can easily download using Pattern is Google.
Here is an example of searching for Olin College using Google:

``` python
from pattern.web import *
g = Google()
for result in g.search('Olin College'):
print result.url
print result.text
```

The first two lines printed out by this Python program are:

```
http://www.olin.edu/
Official site provides news and information about the campus, academics,
<br>admissions, scholarships, faculty, and student life.
```

Notice that the second line of output has an HTML tag (in this case `<br>`)
mixed in (if you don't know what an HTML tag is, don't worry). If you want to
remove HTML from any string with Pattern you can use the `plaintext` function.
For instance, if you change the line of code `print result.text` to `print
plaintext(result.text)` you will get:

```
http://www.olin.edu/
Official site provides news and information about the campus, academics,
admissions, scholarships, faculty, and student life.
```

Besides `url` and `text`, there are some other fields you might want to
utilize. Check out the Pattern documentation for more information. If you now
wanted to follow the links retrieved from this Google search, you could use
the `URL().download()` function on `result.url`.

### Data Source: Wikipedia

The support in Pattern for Wikipedia is quite extensive. I won't try to
rewrite the [official documentation on Pattern's Wikipedia
capabilities](http://www.clips.ua.ac.be/pages/pattern-web#wikipedia), however,
I will provide a few examples that might get your creative juices going.

Here is a Python program to print out the title of every Wikipedia article:

``` python
from pattern.web import *
w = Wikipedia()
for article_title in w.index():
    print article_ title`
```

Given that you know the particular title of the article you would like to
access, you can fetch the article and then print out its sections using the
following Python program:

``` python
from pattern.web import *
w = Wikipedia()
olin_article = w.search('Olin College')
print olin_ article.sections
```

Which yields the output:

```
[WikipediaSection(title=u'Franklin W. Olin College of Engineering'),
WikipediaSection(title=u'History'), WikipediaSection(title=u'The Olin
experiment'), WikipediaSection(title=u'Academics'),
WikipediaSection(title=u'Accreditation'), WikipediaSection(title=u'Culture'),
WikipediaSection(title=u'Residential life'), WikipediaSection(title=u'Honor
Code'), WikipediaSection(title=u'Changing the Honor Code'),
WikipediaSection(title=u'Honor Board'),
WikipediaSection(title=u'Extracurricular activities'),
WikipediaSection(title=u'Spontaneity and student happiness'),
WikipediaSection(title=u'Rankings'), WikipediaSection(title=u'Mascot'),
WikipediaSection(title=u'See also'), WikipediaSection(title=u'References'),
WikipediaSection(title=u'Further reading')]
```

The great thing about the Wikipedia API is that it returns the article in a
highly structured format. This quality makes Wikipedia articles retrieved from
the API very amenable to processing using Python.

### Data Source: Twitter

You can both search Twitter and listen to Twitter streams (that is print out
Tweets in real-time that match a particular query). Here is a program that
runs for 10 seconds and prints out any tweets that are made during those 10
seconds that mention the hashtag `#fail`:

``` python
from pattern.web import *
s = Twitter().stream('#fail')
for i in range(10):
    time.sleep(1)
    s.update(bytes=1024)
    print s[-1].text if s else ''
```

When I ran this program the other day I got the following output:

```
RT @MrRichardPena3: "@KayRockkette: @MrRichardPena3 Good vibes &amp; pizza
after the gym. #fail #healthyeating" that's what im talking about ;)
RT @MrRichardPena3: "@KayRockkette: @MrRichardPena3 Good vibes &amp; pizza
after the gym. #fail #healthyeating" that's what im talking about ;)
RT @MrRichardPena3: "@KayRockkette: @MrRichardPena3 Good vibes &amp; pizza
after the gym. #fail #healthyeating" that's what im talking about ;)
What a ridiculous ad! stating the benefit of buying a home as toa chance of
meeting one of the leading bollywood celebs #fail
What a ridiculous ad! stating the benefit of buying a home as toa chance of
meeting one of the leading bollywood celebs #fail
613 #wtf #fail #fails #nowplaying #youtube #funny ----
http://t.co/Z554Ux1cZT
```

In addition to reading Twitter streams, you can check out the topics that are
currently trending on twitter using this Python program:

``` python
from pattern.web import *
print Twitter().trends()
```

Which produced the following output when I tried running the code:

```
[u'#PerfectoSeria', u'#PorUnMundo', u'#AbelEnCalafate', u'#ResistenciaVzla',
u'#CumaSimSimi', u'Justin Bieber Kecelakaan', u'Kike Acu\xf1a', u'This
Christmas', u'Ad\xe3o e Eva', u'G\xe9nesis Carmona']
```

### Data Source: Facebook

**Edit 2016: Pattern doesn't work with Facebook anymore.**

The interaction between Pattern and Facebook is a bit more complex since you
actually have to use an access key to allow Pattern to access your Facebook
data through Python. Use [this link](http://www.clips.ua.ac.be/pattern-facebook) to authorize Pattern to access your Facebook account. Once you have
your access key (I won't include mine here to maintain my privacy!). You can
start digging through your and your friend's Facebook content. This program
examines my profile and prints out my basic information:

``` python
from pattern.web import *
f = Facebook(license='CAAE...S9o8bFK8ZAOTD4')
me = f.profile()
print me
```

Which generates the output:

`(u'3321475', u'Paul Ruvolo', u'04/20/1981', u'm', u'en_US', 0)`

Alternatively, I could print out the number of friends that I have on
Facebook:

``` python
from pattern.web import *
f = Facebook(license='CAAE...S9o8bFK8ZAOTD4')
me = f.profile()
print len(f.search(me[0], type=FRIENDS, count=10000))
```

Note that `count = 10000` simply specifies the maximum number of results that
the search can return. The results returned by `f.search` can be processed
further. For instance, the following Python program reads through the news
feeds of all of my friends and prints them out.

``` python
from pattern.web import *
f = Facebook(license='CAAE...S9o8bFK8ZAOTD4')
me = f.profile()
my_friends = f.search(me[0], type=FRIENDS, count=10000)
for friend in my_ friends:
    friend_news = f.search(friend.id, type=NEWS, count=10000)
    for news in friend_ news:
        print news.text
        print news.author
```

You can also check out your friends' comments and likes.


### Data Source: Reddit

At the terminal command line, install the Python
[PRAW](https://pypi.python.org/pypi/praw) package:

``` bash
sudo pip3 install praw
````

Here's an example from the [PRAW docs page](https://praw.readthedocs.org/en/stable/):

``` python
import praw
r = praw.Reddit(user_agent='my_ cool_application')
submissions = r.get_ subreddit('opensource').get_hot(limit=5)
[str(x) for x in submissions]
```

Disclaimer: The instructors have run the example above, but haven't explored
this package any more deeply. It's possible that you will run into a roadblock
with it.


### More Data Sources

There are many other data sources that can be mined using Pattern:

  * Google translate
  * Bing
  * Flickr image search
  * DBPedia
  * Newsfeed
  * ...

Check the [Pattern documentation](http://www.clips.ua.ac.be/pages/pattern-web)
for a full list.

### Pickling Data

For several of these data sources you might find that the API calls take a
pretty long time to return, or that you run into various API limits. To deal
with this, you will want to save the data that you collect from these services
so that the data can be loaded back at a later point in time. Suppose you have
a bunch of Project Gutenberg texts in a list called `charles_dickens_ texts`.
You can save this list to disk and then reload it using the following code:


``` python
import pickle

# Save data to a file (will be part of your data fetching script)
f = open('dickens_texts.pickle','w')
pickle.dump(charles_ dickens_texts,f)
f.close()

# Load data from a file (will be part of your data processing script)
input_ file = open('dickens_texts.pickle','r')
reloaded_ copy_of_ texts = pickle.load(input_file)
```

The result of running this code is that all of the texts in the list variable
`charles_ dickens_texts` will now be in the list variable
`reloaded_ copy_of_ texts`. In the code that you write for this project you
won't want to pickle and then unpickle in the same Python script. Instead, you
might want to have a script that pulls data from the web using Pattern's APIs
and then pickles them to disk. You can then create another program for
processing the data that will read the pickle file to get the data loaded into
Python so you can perform some analysis on it.

For more details and practice, check out the [Pickling Project
Toolbox\]({% link _toolboxes/pickling.md %}) assignment.


### Troubleshooting Pattern

_**Problem** _: I am able to execute Pattern API calls, however, when I execute
a lot of them in sequence I sometimes run into errors (e.g. SSLError).

**_Solution 1_** : Try reducing the throttle (for instance `f = Facebook(license="YOUR_LICENSE_ HERE", throttle=0.5))`. If that doesn't work try solution 2.

**_Solution 2_** : I have found that simply retrying the API call often works. You can make your Python code execute the API call repeatedly until you achieve success using the following code (in this example we will get all of my Facebook friends and then print out all of their news feeds):

``` python
from pattern.web import *
import time


f = Facebook(license='CAAE...S9o8bFK8ZAOTD4')
me = f.profile()
retry = True
while retry:
    try:
        my_friends = f.search(me[0], type=FRIENDS, count=10000)
        retry = False # we have achieved success, don't retry
    except:
        time.sleep(5) # sleep a little bit before retry

for friend in my_ friends:
    retry = True
    while retry:
    try:
        friend_news = f.search(friend.id, type=NEWS, count=10000)
        retry = False # we have achieved success, don't retry
    except:
        time.sleep(5) # sleep a little bit before retry
    for news in friend_ news:
        print news.text
        print news.author
```


## Part 2: Analyzing Your Text

### Characterizing by Word Frequencies

One way to begin to process your text is to take each unit of text (for
instance a book from Project Gutenberg, or perhaps a collection of Facebook
posts by one of your friends) and summarize it by counting the number of times
a particular word appears in the text. A natural way to approach this in
Python would be to use a dictionary where the keys are words that appear and
the values are frequencies of words in the text (if you want to do something
fancier look into using [TF-IDF features](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)).


### Computing Summary Statistics

Beyond simply calculating word frequencies there are some other ways to
summarize the words in a text. For instance, what are the top 10 words in each
text? What are the words that appear the most in each text that don't appear
in other texts? For some other ideas see [Chapter 13 of Think Python](http://greenteapress.com/thinkpython/html/thinkpython014.html).


#### Doing Linguistic Post-processing

Pattern provides some really cool [natural language processing
capabilities](http://www.clips.ua.ac.be/pages/pattern-en). Some examples of
this include: part of speech tagging, sentiment analysis, and full sentence
parsing. Here is an example of doing [sentiment
analysis](http://en.wikipedia.org/wiki/Sentiment_analysis):

``` python
from pattern.en import *
print sentiment('Software Design is my favorite class!')
```

This program will print out:

```
(0.625, 1.0)
```

The first part of the output indicates that the sentence has positive
sentiment polarity and the second part of the output indicates that the
sentiment analyzer views this as a purely subjective statement.

If you perform some linguistic post processing, you may be able to say
something interesting about the text you harvested from the web. For instance,
which of your friends on Facebook is the most negative? Which is the most
subjective? If you listen to a particular Twitter hashtag on a political
topic, can you gauge the mood of the country by looking at the sentiment of
each tweet that comes by in the stream? There are tons of cool options here!


### Text Similarity

It is potentially quite useful to be able to compute the similarity of two
texts. Suppose that we have characterized some texts from Project Gutenberg
using [word frequency analysis\]({% link _assignments/mini-project-3-text-mining.md %}#characterizing-by-word-frequencies). One way to compute the
similarity of two texts is to test to what extent when one text has a high
count for a particular word the other text also a high count for a particular
word. Specifically, we can compute the [cosine
similarity](http://en.wikipedia.org/wiki/Cosine_similarity) between the two
texts. This strategy involves thinking of the word counts for each text as
being high-dimensional vectors where the number of dimensions is equal to the
total number of unique words in your text dataset and the entry in a
particular element of the vector is the count of how frequently the
corresponding word appears in a specific document (if this is a bit vague and
you want to try this approach, send Paul an e-mail).

I tried this on some Project Gutenberg texts from two authors: Charles Dickens
and Charles Darwin. The table below shows the pair-wise similarities between
the Charles Dickens texts (note that 1 is perfect similarity):

```
[[ 1. 0.90850572 0.96451312 0.97905034]
 [ 0.90850572 1. 0.95769915 0.95030073]
 [ 0.96451312 0.95769915 1. 0.98230284]
 [ 0.97905034 0.95030073 0.98230284 1. ]]
```

The pairwise similarities between Dickens and Darwin (I just used one Darwin
text) are:

```
[[ 0.78340575]
 [ 0.87322494]
 [ 0.83381607]
 [ 0.82953109]]
```

Notice that all of the similarities between Dickens and Darwin are lower than
for Dickens novels to other Dickens novels. This suggests that this technique
can be used for author identification (for instance in the case of a work of
unknown authorship). You could also use it to try and guess which of your
friends has authored a particular post!

These similarity values can be assembled into a similarity matrix that
compares each work with all other works.

```
[[ 1., 0.90850572, 0.96451312, 0.97905034, 0.78340575],
 [ 0.90850572, 1., 0.95769915, 0.95030073, 0.87322494],
 [ 0.96451312, 0.95769915, 1., 0.98230284, 0.83381607],
 [ 0.97905034, 0.95030073, 0.98230284, 1., 0.82953109],
 [ 0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.]])
```

#### Text Clustering

If you can generate pairwise similarities (say using the technique above), you
can Metric Multi-dimensional Scaling
([MDS](http://en.wikipedia.org/wiki/Multidimensional_ scaling)) to visualize
the texts in a two dimensional space. This can help identify clusters of
similar texts (for instance, which of your friends on Facebook are most
similar to each other). Here is a particularly inspiring example by Matthew
Jockers (check out the University of Nebraska's [press
release](http://newsroom.unl.edu/releases/2012/08/28/By+text-mining+the+classics,+UNL+professor+unearths+new+literary+insights) on the
paper).

![](http://newsroom.unl.edu/releases/downloadables/photo/20120828macro-american.jpg)

In order to apply MDS to your data, you can use the machine learning toolkit
scikit-learn (to install it consult the [machine learning toolbox)\]({% link _toolboxes/machine-learning.md %}).

Here is some code that uses the similarity matrix defined in the previous
section to create a 2-dimensional embedding of the four Charles Dickens and 1
Charles Darwin texts.

``` python
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[ 1., 0.90850572, 0.96451312, 0.97905034, 0.78340575],
    [ 0.90850572, 1., 0.95769915, 0.95030073, 0.87322494],
    [ 0.96451312, 0.95769915, 1., 0.98230284, 0.83381607],
    [ 0.97905034, 0.95030073, 0.98230284, 1., 0.82953109],
    [ 0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.]])

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:,0],coord[:,1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i),(coord[i,:]))

plt.show()
```

This will generate the following plot. The coordinates don't have any special
meaning, but the embedding tries to maintain the similarity relationships that
we computed via comparing word frequencies. Keep in mind that the point
labeled 4 is the work by Charles Darwin.

![]({% link images/assignments/text-mining/figure_1.png %}{:width="400px" height="300px"}


### Markov Text Synthesis

You can use [Markov](http://en.wikipedia.org/wiki/Markov_ chain) analysis to
learn a generative model of the text that you collect from the web and use it
to generate new texts. You can even use it to create mashups of multiple
texts. Two possibilities in this space would be to imitate Facebook posts by
each of your friends, or to create literary mashups automatically. [Think
Python chapter 13](http://greenteapress.com/thinkpython/html/thinkpython014.html) section 8
called "Markov Analysis" has some detail on how to do this. Again, let the
teaching team know if you go this route and we can provide more guidance.


## Part 3: Project Writeup and Reflection

Please prepare a short (suggested lengths given below) document with the
following sections:

**Project Overview** _[Maximum 100 words]_

What data source(s) did you use and what technique(s) did you use
analyze/process them? What did you hope to learn/create?

**Implementation**  _[~2-3 paragraphs]_

Describe your implementation at a system architecture level. You should
**NOT**  walk through your code line by line, or explain every function (we can
get that from your docstrings). Instead, talk about the major components,
algorithms, data structures and how they fit together. You should also discuss
at least one design decision where you had to choose between multiple
alternatives, and explain why you made the choice you did.

**Results**  _[~2-3 paragraphs + figures/examples]_

Present what you accomplished:

* If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
* If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program's output.

**Reflection** _[~1 paragraph]_

From a process point of view, what went well? What could you improve? Other
possible reflection topics: Was your project appropriately scoped? Did you
have a good plan for unit testing? How will you use what you learned going
forward? What do you wish you knew before you started that would have helped
you succeed?

## Turning in your assignment

* Push your code to GitHub
* Submit your Project Writeup/Reflection. This can be in the form of either:
  * a PDF document pushed to GitHub, or
  * a [project webpage](https://pages.github.com/) (in this case make sure to include a link to this webpage in the README.md file in your repository (otherwise, we won't be able to find your website).
* Create a pull request to the upstream repository
