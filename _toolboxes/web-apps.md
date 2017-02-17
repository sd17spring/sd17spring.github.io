---
date: 2017-02-17
description: ''
title: Web Apps
---

{% include toc %}

## Introduction

Flask is a lightweight and powerful web framework for Python. It's easy to
learn and simple to use, allowing you to build your web app in a short amount
of time.

In this toolbox, you'll how to build a simple website, containing two static
pages with a small amount of dynamic content. While Flask can be used for
building complex, database-driven websites, starting with mostly static pages
will be useful to introduce a workflow, which you can then generalize to make
more complex pages in the future. Upon completion, you'll be able to use this
sequence of steps to jumpstart your next Flask app.

## Get Set

In this toolbox, you'll be learning Flask. To do this, you'll first need to
install Flask. Run the following command:

    sudo pip3 install Flask

Grab the starter code for this toolbox exercise via the normal fork-and-clone
method from <https://github.com//{{site.course.github_owner}}/Toolbox-Flask>.

This toolbox exercise was developed by Patrick Huston. Let him know if you
decide to complete it; he can help with any questions that arise.

## What is Flask, really?

In the introduction, we defined Flask as a "web framework", but what does that
actually mean? Let's dig deeper. Before this, let's develop a better
understanding of how the internet works.

When you open up a web page in your browser (e.g. Chrome, Firefox, etc.), it
makes an HTTP request to a server somewhere in the world. This could be
something like `GET me the home page`. This server handles this request,
sending back data (this can be in the form of HTML, JSON, XML, etc.), which is
rendered by your browser.

This is where Flask comes in - it allows you to create the logic to make a web
server quickly in Python. You can write logic that will execute when a request
is made for one of your routes (e.g. `www.mycoolwebsite.com/home`)

## Hello World in Flask

Let's write some Flask. A simple Hello World application written in Flask can
be as simple as this:

``` python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

Write this, save it as something like `hello.py`, and run it in terminal. Make
sure to not call your application flask.py because this would conflict with
Flask itself.

    $ python3 hello.py
     * Running on http://127.0.0.1:5000/

Now head over to <http://127.0.0.1:5000/>, and you should see your hello world
greeting.

In case you're curious `127.0.0.1` points to your local computer, and `5000`
is the port it's listening on.

What did that actually do? Let's walk through the steps.

1. First we imported the Flask class.
2. Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use `__name__` because depending on if it’s started as application or imported as module the name will be different ('`__main__'` versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on.
3. We then use the `route()` [decorator](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators) to tell Flask what URL should trigger our function. In this case our route is `/`, commonly referred to as the `index` of a page.
4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
5. Finally we use the `run()` function to run the local server with our application. The `if __name__== '__main__'` makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module.

To stop the server, hit `ctrl+c`.

## What's this routing business?

In our hello world, example, we had one route denoted by the decorator
`@app.route('/')`. Again, this 'decorator' tells the Flask app that any
incoming requests for `GET /` will run the function we called
`hello_world()`.

Here are a couple more quick examples -

``` python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```

Pretty simple, right? What happens when we want to do something _useful_ \-
*e.g.* display something other than text?

## Let's serve some HTML!

HTML (HyperText Markup Language) is the standard markup language used to
create web pages. In addition to sending back strings, Flask can send back
HTML files to the client, which will be rendered in the browser. Let's get to
work creating a basic HTML document.

Let's start by creating a file called `index.html`:

``` html
<!DOCTYPE html>
<html>
    <head>
        <title>
            A Small Hello
        </title>
    </head>
<body>
    <h1>Hi</h1>
    <p>This is very minimal "hello world" HTML document.</p>
</body>
</html>
```

Create a new directory called `templates`, and save this new document as
`index.html` there.

Let's figure out how to show this document now.

## Rendering pages

To render a template you can use the `render_template()` method. All you have
to do is provide the name of the template and the variables you want to pass
to the template engine as keyword arguments. Here’s a simple example of how to
render a template:

``` python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

And here is an example template that will work with the above snippet:

``` html
<!doctype html>
<title>Hello from Flask</title>
 if name
    <h1>Hello {{ name }}!</h1>
 else
    <h1>Hello World!</h1>
 endif
```

You may have noticed something really cool that happened here. In our route
`/hello/<name>`, we're allowing someone to make a request with an additional
'name' parameter that can be anything. We can then use this `name` and render
it in our html template `hello.html`. We use the `{___}` syntax to insert
outside variables into the template. Additionally, we can insert pythonic flow
logic directly into our HTML page – see `{% raw %}{% if name %}{% endraw %}`. We could go on for
years about all of the power of jinja templating, but I'll leave that joy to
this [wonderful article](http://jinja.pocoo.org/docs/dev/templates/).

Getting back to our simple Hello World app, let's add in a route to display
our `index.html` we created above.

``` python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```

And that's it! Again, follow the instructions

    $ python3 hello.py
     * Running on http://127.0.0.1:5000/

to run the application, and head over to <http://127.0.0.1:5000/>, and you
should see your hello world greeting. It might not look very different, but
you're now working with a much more powerful format of representing
information through HTML.

## Build your own app: getting input from the user

What use is a web application if you can't get any data back from the user?
Let's set up a simple app. Here are our end specifications:

1. Upon visiting the index page at <http://127.0.0.1:5000/>, the user will be greeted by a page that says hello, and includes an input form that requests their name, age, and favorite SoftDes Ninja.
2. Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route `POST /login`.
3. The Flask backend will handle the request to `POST /login` and perform some simple validation on the user input - simply check to see if they exist.
4. If all the information is present, the app will render a 'profile' page for the user - presenting their name and age. Regardless of their input for final question, their favorite SoftDes ninja, the app will display `Patrick Huston`.
5. If all the information is not present, the app will render a simple error page, which will include some indication that they didn't include all the required information, in addition to a button that will redirect the user back to the home page.

It will be up to you to make this happen. If you feel confident in your
ability to implement this, go for it! If you'd like more scaffolding, continue
reading.

## Tips and tricks

To complete this exercise, the official Flask documentation will get you
pretty far. There is the [full
documentation](http://flask.pocoo.org/docs/0.10/#user-s-guide) and the
[quickstart guide](http://flask.pocoo.org/docs/0.10/quickstart/), both of
should be pretty helpful.

1. _HTML Forms_ To make forms in HTML, check out [this resource](http://www.w3schools.com/html/html_forms.asp). For even more information, check [this](http://tinyurl.com/htmlforms) out.
2. _Sending POST Requests_ To send the data from the form in a POST request, use an input with type `submit`, and set the action of the form to reflect the destination in your routes.
3. _Handling POST Requests_ To learn more about handling post requests in Flask, check this resource from the [Flask documentation](http://flask.pocoo.org/docs/0.10/quickstart/#http-methods) out.
4. \+ 5. _Accessing the Form Data_ To access the form data, check out [this documentation](http://flask.pocoo.org/docs/0.10/quickstart/#the-request-object) on using the Flask `request` utility.

## What to turn in

Push the web app you developed in the previous section to GitHub and submit a
pull request to get checked off.

## Going further

1. **Learn more about [Django](https://www.djangoproject.com/)**  \- an alternative to Flask. They don't have many major differences other than some small quirks in conventions and style. See [here](https://wakatime.com/blog/25-pirates-use-flask-the-navy-uses-django) for more analysis.
2. **Want to keep track of some data in your web app?**  Instead of using a .txt file or a pickle file, it's common practice in nearly any web app to use a database. A few especially well-known database choices are MySql, SQLite, or PostgreSQL (which all use [Structured Query Language](https://www.codecademy.com/learn/learn-sql) to manipulate all stored, as do many other common [relational databases](https://en.wikipedia.org/wiki/Relational_database)). You also may have heard some buzz about MongoDb, which uses an unstructured data format in "documents" similar to JSON. Mongo is stupidly easy to set up and use, but I'd stop and think first before jumping right in. It may be the easy choice, but representing your data intellengently in a relational table can be much more effective and less of a headache later on.
3. **But HTML is so ugly!**  HTML alone *is*  very ugly. That's why we use CSS (Cascading Style Sheets) to add some extra flair and style to our HTML. You can change pretty much anything about HTML - colors, shapes, sizes, placement, etc. with CSS rules. It's also pretty simple to write. Check [this resource](http://www.w3schools.com/css/css_intro.asp) out to learn more about CSS.
4. **What about making my website dynamic?**  SoftDes may be a class in Python, but we can venture out a little and use some [jQuery](http://www.w3schools.com/jquery/jquery_intro.asp). jQuery might seem scary, but you use it in a way similar to adding / linking CSS styling to your HTML. You write scripts in JavaScript (which isn't too difficult), which can allow you to add beautiful responsive and dynamic content to your web app.
