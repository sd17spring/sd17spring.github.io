# Spring 2017 SoftDes Web Site

[![Build Status](https://travis-ci.org/sd17spring/sd17spring.github.io.svg?branch=master)](https://travis-ci.org/sd17spring/sd17spring.github.io)

Home page for Olin College Software Design Spring 2017

The source to <https://sd17spring.github.io>.

## Setup

1. [Install Jekyll](https://jekyllrb.com/docs/installation/)
2. `bundle install`

Alternative: Install [Docker Compose](https://docs.docker.com/compose/install/)

## Develop

1. `bundle exec jekyll serve`
2. Browse to [localhost:4000](http://localhost:4000)

Alternative:

1. `docker-compose up`
2. Browse to [localhost:4000](http://localhost:4000)

## Testing

Lint Markdown files:

```bash
$ mdl .
```

Check HTML and Links:

```bash
$ ./scripts/check-html
```

## Publish

1. `git push` to GitHub
2. Browse to <https://sd17spring.github.io>

## Acknowledgements

The course was created by Olin faculty Paul Ruvalo, Ben Hill, and Amon Millner, with contributions from
Oliver Steele, and from Olin NINJAs (teaching assistants) some of whom are credited in the Toolbox pages.

The Gene Finder project assignment was originally created by Professors Ran Libeskind-Hadas, Eliot C. Bush, and their [collaborators](https://www.cs.hmc.edu/twiki/bin/view/CS6/GreenAcknowledgements) at Harvey Mudd.

The Computational Art project was adapted from Harvey Mudd Professor Chris Stone's assignment posted at the
[Stanford Nifty Assignments ](http://nifty.stanford.edu/) collection.

This site is hosted on the GitHub Pages, using the [Jekyll](http://jekyllrb.com) blogging platform, the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme,
and [Font Awesome](http://fontawesome.io).
