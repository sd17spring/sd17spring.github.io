---
title: Web Deployment
date: 2017-03-26 21:03:00 -04:00
description: Use Heroku to run a web application at a publically accessible URL.
---

{% include toc %}

## Introduction

In this toolbox, you will deploy a Flask application to the cloud, so that users can visit it at a public
URL.

You will learn how to use `git push` to deploy to the Heroku hosting service, how to configure a Flask application to accept external requests, and how and why to configure a Flask application to listen on different TCP/IP ports.

## Prerequisites

To start, you will need a Flask application that runs on your laptop. If you don't have such an application, complete the [Web Apps Toolbox]({% link _toolboxes/web-apps.md %}) and then return to this toolbox.

## Get Set

1. Follow the instructions [here](https://signup.heroku.com) to sign up for
   a (free) account Heroku cloud platform. Heroku manages servers that will
   run your app.

2. Follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) to download the Heroku command-line interface.

3. Run `heroku login` with the credentials you created in step 1:

    Enter your Heroku credentials.
    Email: frankly.olin@olin.edu
    Password (typing will be hidden):

## Create a Heroku application

Run `heroku apps:create` to create a Heroku **application**:

```bash
$ heroku apps:create web-app
Creating app... done, boiling-brushlands-71788
https://boiling-brushlands-71788.herokuapp.com/ | https://git.heroku.com/boiling-brushlands-71788.git
```

`heroku apps:create` selects a random name (above, `boiling-brushlands-71788`)
for your application. You can also *specify* a name, so long as it is unique
among all Heroku applications (for all users).
For example, `heroku app:create osteele-toolbox` makes my application available at `https://osteele-toolbox.herokuapp.com`.

## Publish Your Application to Heroku

```bash
$ cd /path/to/web-app
$ heroku git:remote -a my-heroku-app-name
$ git push heroku master
```

where `my-heroku-app-name` is the name of your Heroku application.

You should see an error message:

    Total 0 (delta 0), reused 0 (delta 0)
    remote: Compressing source files... done.
    remote: Building source:
    remote:
    remote: -----> Failed to detect set buildpack https://codon-buildpacks.s3.amazonaws.com/buildpacks/heroku/python.tgz
    remote: More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
    remote:
    remote:  !     Push failed
    remote: Verifying deploy....
    remote:
    remote: !  Push rejected to my-heroku-app-name.
    remote:
    To https://git.heroku.com/my-heroku-app-name.git
    ! [remote rejected] 7039fff -> master (pre-receive hook declined)
    error: failed to push some refs to 'https://git.heroku.com/my-heroku-app-name.git'

## Why Doesn't it Work (pt. 1 of 2)? – Setting Your Repo Up for Heroku

If you Google around and spend some time learning what a "buildpack" is
(not required for this toolbox), you will eventually learn that Heroku
can't figure out what programming language your application is written in, and
therefore doesn't know how to run it.

You need to add three files to your repository in order to tell Heroku
how to [provision a server](https://en.wikipedia.org/wiki/Provisioning#Server_provisioning):

`requirements.txt`
: is a list of Python packages. This tells Heroku that your application is a Python
  program, and which packages to install.

`Procfile`
: lists the command and arguments that starts your program.

`runtime.txt`
: specifies the Python version. Without this file, Heroku will use Python 2.7.
The toolboxes use Python 3, so it is necessary to override this.

Here's what to do:

1. Create the following three files, with these contents:

    **`Procfile`**

        web: python3 hello.py

    **`runtime.txt`**

        python-3.6.1

    **`requirements.txt`**

        Flask

2. Use `git add` to add the new files to the repository. `git commit` them.

3. Test the `Procfile` on your laptop:

    ```bash
    $ heroku local web
    ```

    Running `heroku local` has the same effect as running `python3 hello.py`, but it uses the same `Procfile` that Heroku will use.
    Running therefore `herokku local` tests more of what will happen “in production” than running `python3 hello.py` does.
    (See [The Twelve-Factor App: Dev/prod parity](https://12factor.net/dev-prod-parity).

4. Now `git push heroku master` again. This time the deploy should succeed:

    ```bash
    $ git push heroku master
    […]
    remote: -----> Launching...
    remote:        Released v18
    remote:        https://my-heroku-app-name.com/ deployed to Heroku
    remote: Verifying deploy.... done.
    To https://git.heroku.com/my-heroku-app-name.git
    ```

## Open Your App in a Browser

Do you do this in one two ways:

1. Find the line `https://my-heroku-app-name.herokuapp.com/ deployed to Heroku`
   in the `git push` output above. Open `https://my-heroku-app-name.herokuapp.com/`
   in a browser. Or:

2. `heroku apps:open` does this automatically.

You should see an “Application Error” page.

## Why Doesn't it Work (pt. 2 of 2)? Configuring Your Server to Accept Remote Connections

By default, your application only accepts HTTP requests from the same machine.
This is because it uses `127.0.0.1` as the host.

This is appropriate for local development, but does not make for a web server in the cloud. You need to run your application with `0.0.0.0` as the host. This allows it to accept requests from anywhere on the web.

A second issue is that your application currently accepts connections to [TCP/IP port](http://www.bullguard.com/bullguard-security-center/pc-security/computer-security-resources/tcp-ip-ports.aspx) #5000.

From the outside, Heroku accepts HTTPS connections to port #443. This is the default port for an `https:` URL, and is why you (eventually) will get to  use `https://my-heroku-app-name.herokuapp.com/`, instead of `https://my-heroku-app-name.herokuapp.com:5000/`.

Internally, Heroku expects your app to accept an HTTP connection on some port that depends on your application, maybe where it's running, and maybe the time of day – you don't know what the port number is when you write your code. Heroku communicates the port number to your application by setting an [environment variable](https://en.wikipedia.org/wiki/Environment_variable).

Fix these two problems (using `0.0.0.0`, and reading the port number from an environment variable) as follows:

1. Add this line to the top of your file:

    ```python
    import os.environ
    ```

2. Define `HOST` and `PORT` as below. Then add `host` and `port` arguments to the `app.run` function. Commit the change, `git push` to Heroku again, and test again. You should see your web page.

    ```python
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000)))
    app.run(host=HOST, port=PORT)
    ```

## Whitelist the Domain

**Problem:** Olin's [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) provider blocks some new sites from the Olin network after a 1-3 day grace period.
Your app may work for a while, and then stop working with the message below:

![]({% link images/toolboxes/heroku/it_security_message.png %})

**Solution:** Send a message to <helpdesk@olin.edu>: “I am using the domain name myapp.herokuapp.com for a class project, and need access to it from within the Olin network. Please configure DNS so that it does not block this site.”

## What to Turn In

1. Add more functionality to the application. For example, another of the items from the "Going further" section of the [Web App]({% link _toolboxes/web-apps.md %}) toolbox.

2. Add a link from your GitHub repo to your (Heroku) application URL.

   Here's how to add the link:

   1. Open your repo page on GitHub.

      Near the top of the page is an Edit button;
      this discloses text entry fields for a project Description and Website.

   2. Paste your application URL into the Website field, and Save.

3. Show your work to a NINJA.

4. You should be prepared to explain the motivation for the `HOST =` and `PORT =` lines that you added, and how they work.

## Going Beyond

Some things you can do to learn more and/or have more fun:

* Add an `app.json` file, and a ![](https://www.herokucdn.com/deploy/button.svg) button. The instructions are [here](https://devcenter.heroku.com/articles/heroku-button).
* Learn about [Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn). Use this to deploy a web application that can serve more than one HTTP request at a time.
