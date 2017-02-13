---
date: 2017-01-22
description: ''
title: Geocoding and Web APIs
---

{% include toc %}

{% include construction %}

The Pattern library does not work with Python 3.

## Introduction

In Mini Project 3, you used the Python data mining package
[Pattern](http://www.clips.ua.ac.be/pattern) to access information on the
Internet. Pattern gets that information by interacting with various web
application programming interfaces (APIs) on your behalf. In this toolbox
exercise, you will access web APIs directly and begin to write your own
package to connect with new data sources.

This toolbox exercise will focus on dealing with geographical data. You will
write a tool that takes an address or place name and prints the closest MBTA
stop and the distance from the given place to that stop. For example:

    >>> import mbta_finder
    >>> mbta_finder.find_stop_near("Fenway Park")
    Yawkey is 0.13 miles from Fenway Park

**Note** : There are already [a few Python packages](https://wiki.python.org/moin/GIS/Web_services) that interface with mapping services, but part of this exercise is seeing how you might write your own such package from scratch.

## Get Set

Grab the starter code for this toolbox exercise via the normal fork-and-clone
method from _<https://github.com//{{site.course.github_owner}}/ToolBox-Geocoding>_

You should see `mbta_finder.py` within the toolbox folder, which has some
optional scaffolding for this exercise.

## Getting data from the web

Let's grab some data from the Internet!

    >>> from urllib.request import urlopen
    >>> f = urlopen("http://www.olin.edu")
    >>> print(f.read(400))
    <!DOCTYPE html>
    <html>
    <head profile="http://www.w3.org/1999/xhtml/vocab">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="shortcut icon" href="http://www.olin.edu/favicon.ico"
    type="image/vnd.microsoft.icon" />
    <link rel="alternate" type="application/rss+xml" title="Front page feed"
    href="http://www.olin.edu/rss.xml" />
    <title>Olin College</title>

Here we're using [urllib.request](https://docs.python.org/3.0/library/urllib.request.html) to
open a [URL](http://en.wikipedia.org/wiki/Uniform_resource_locator) and get
its contents over
[HTTP](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). For a nice
introduction to how HTTP works, check out this [olin.js
lesson](https://github.com/olinjs/olinjs/tree/master/classes/class01#http).

The [urlopen](https://docs.python.org/3.0/library/urllib.request.html)
method returns a [file-like
object](https://docs.python.org/3/glossary.html#term-file-object), from
which we read and print the first 400 bytes. The result is the HTML code that
your browser uses to display the `olin.edu` homepage.

What if we want to get a specific piece of information, e.g. Olin's mailing
address? As you can see from the snippet above, the HTML website code includes
lots of extraneous information used to display the page in your browser. We
could of course wade through this (using Python!) to find what we're looking
for, but for many web services there's an easier way to ask for what we want
directly.

## Accessing web data programmatically

That more direct method is application programming interfaces. APIs let you
make requests using specifically constructed URLs and return data in a nicely
structured format.

There are three main steps to using any web API:

**1\. Read the API documentation**

You should specifically look out for whether the API can provide the data you
want, how to request that data, and what the return format will be.

**2\. Request an API developer key**

Web services generally limit the number of requests you can make by requiring
a unique user key to be sent with each request. In order to get a key you'll
need to agree to their terms, which restrict how you can use the service. In
this class we will never ask you to agree to terms you aren't comfortable with
- contact the teaching team if you have an issue.

**3\. Test out your application and launch to users**

A.K.A. the fun part.

The first API we will use is the [Google Maps Geocoding
API](https://developers.google.com/maps/documentation/geocoding/). This tool
(among other things) allows you to specify a place name or address and receive
its latitude and longitude. Take a few minutes to read the documentation (it's
quite good) through "Geocoding Responses".

## Structured data responses (JSON)

Back? Ok cool, let's try it out in Python. We're going to request the response
in JSON format, which we can decode using Python's
[json](https://docs.python.org/3/library/json.html) module.

    >>> from urllib.request import urlopen
    >>> import json
    >>> from pprint import pprint
    >>> url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
    >>> f = urlopen(url)
    >>> response_text = f.read()
    >>> response_data = json.loads(str(response_text, "utf-8"))
    >>> pprint(response_data)

We used the [pprint](https://docs.python.org/3/library/pprint.html) module to
"pretty print" the response data structure with indentation so it's easier to
visualize. You should see something similar to the JSON response from the
documentation, except built from Python data types. The response data structure is built from nested dictionaries and lists, and you can step through it to access the fields you want.

      >>> print(response_data["results"][0]["formatted_address"])
      4 Yawkey Way, Boston, MA 02215, USA


**Note** : You might notice that I didn't provide an API key with the request. For the Google Maps API, you can actually get away without one for a small number or requests. Be sure to limit your requests (don't repeatedly make requests in a loop, or rate-limit using [time.sleep](https://docs.python.org/3/library/time.html#time.sleep)) so that Olin's IP range is not blocked.

**Write a function to extract the latitude and longitude from the JSON response.**

## Speaking URL

In the above example we passed a hard-coded URL to the `urlopen` function, but
in your code you will need to generate the parameters based on user input.
Check out [Understanding URLs and their
structure](https://developer.mozilla.org/en-US/Learn/Understanding_URLs) for a
helpful guide to URL components and encoding.

You can build up the URL string manually, but it's probably helpful to check
out
[urlencode](https://docs.python.org/3.0/library/urllib.parse.html#urllib.parse.urlencode)

**Write a function that takes an address or place name as input and returns a properly encoded URL to make a Google Maps geocode request.**

## Getting local

Now that we can find the coordinates of a given place, let's take things one
step further and find the closest public transportation stop to that location.

To accomplish this, we will use the [MBTA-realtime
API](http://realtime.mbta.com/Portal/Home/Documents). Read through the API
quickstart guide, and check out the details for `stopsbylocation` in the API
v2 documentation.

**Note**: The MBTA documentation provides a testing API key that you can use for small numbers of requests, so you may not need to register

**Write a function that takes a latitude and longitude and returns the name of the closest MBTA stop and its distance from the given coordinates.**

## What to turn in

Combine your work from the previous sections to create a tool that takes a
place name or address as input, finds its latitude/longitude, and returns the
nearest MBTA and its distance from the starting point.

**Note**: Sadly there are no MBTA stops close enough to Olin College - you have to get out into the city!

## Making it cooler

* Try out some other [Google Maps web services](https://developers.google.com/maps/documentation/webservices/) \- this is a really rich space and we have barely scratched the surface
* Create and publish a Python module for accessing MBTA data
* By default `stopsbylocation` gives all types of transportation, including buses and commuter rail. Allow the user to specify how they'd like to travel (e.g. T only)
* Add in the MBTA realtime arrival data to help choose what station you should walk to
* Connect with other local services. Example: the City of Boston has [an app](http://www.cityofboston.gov/DoIT/apps/streetbump.asp) that uses a phone's GPS and accelerometer to automatically report potholes to be fixed.
