---
date: 2017-01-30
description: ''
permalink: /git-help/
title: Git Help
---

{% include toc %}


## Git Resources From Around the Web

* A [fantastic visual introduction](http://pcottle.github.io/learnGitBranching/) to the high-level concepts around Git and branching. If you are at all interested in using branches, this is one is not to be missed.
* [Great visualization](http://www.ndpsoftware.com/git-cheatsheet.html#loc=workspace;) of basic Git commands for moving source around
* [Why is Git so hard?](http://merrigrove.blogspot.com/2014/02/why-heck-is-git-so-hard-places-model-ok.html) (it's not just you!)


## Git Tutorials From Past Semesters

[Git &amp; GitHub
presentation](https://docs.google.com/presentation/d/1NpeHiQKs-y2PKp_XrUgzhSSXXBrhTv5DHU4vjQoF99Y/edit?usp=sharing)
(thanks: Chris)

[One-page cheat sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf) (PDF, thanks: Celine)

## How to get the stuff from my computer to GitHub

``` bash
$ git add <filename>
$ git commit -m "<commit-message>"
$ git push
```

You can alternatively use`“git commit -am ‘<commit-message’` to both add all
of the files in your folder and put a message on them, all in one command!

If you forget to include -m in your commit, git will open a text-editor called
vim so that you can enter a commit message there. To write your commit message
in vim, first press “i”, then write your message, then type “:wq” for write-
quit. Alternatively, if you just want to escape from vim’s interface without
saving a message, just enter “:q” for quit.


## Pulling reading journal notebook files from class repository

When the instructors have uploaded new reading assignments, you can pull them into your repository if the upstream repository is the one you originally forked from.

``` bash
$ git remote add upstream https://github.com/{{ site.data.course.github_owner }}/ReadingJournal
$ git fetch upstream
$ git merge upstream
```

This will fetch files from the remote “upstream” which is set to the original
course repository, and will merge the changes in upstream to your own
repository.


## How to pull changes from GitHub

`$ git pull`

-or-

`$ git pull origin master`

If you get merging errors telling you that you need to merge or ‘stash’ before
you can pull, see the ‘stashing’ section below. Also, a quick note on pulling,
what pulling means is that you’re taking the code that others have pushed to
your repository and matching what you have on your computer with that, so it
incorporates their changes.


## How to stash (and what is stashing?)

`$ git stash`

Stashing stores the copy of your current version of the repository on your
computer, so you can keep that copy there before you pull changes that others
have made. Often, you’ll be prompted to stash before pulling or merging with
others. Now that you’ve stashed, how do you get your stuff back? You’ll
probably do the following:

`$ git stash`

`$ git pull`

`$ git stash pop`

Git stash will store your changes locally, git pull will download the changes
other have made to the repository, and git stash pop puts the changes that you
made locally that conflict directly in the code. If there’s anything to merge,
do it in the file and then commit and push your changes.


## How to fix a Git detached head

`$ git checkout master`

If this doesn’t work, try:

`$ git checkout origin/master`


## What is branching on Git?

Branches on Git are very similar to branches on trees. The tree trunk is
represented as the ‘master’ branch and the branches that come off of the
master branch you can name whatever you want. These branches will start at
whatever state master was at the time you made the branch. The master branch
can continue changing independently of the branch that you created. You can
combine the changes that you make in separate branches by ‘merging’ them
together. For more on merging, look at the sections that will follow. Also,
you can view all of the branches in your repository by doing:

`$ git branch -a`

And you can tell what branch you’re on by doing the command:

`$ git branch`


## How to make a new branch

`$ git fetch origin`

`$ git checkout -b <your-branch-name> origin/master`

This branch will exist on your computer, in order to push it to git and have
it be visible by others, you’ll have to push your local branch to be a remote
branch (see below)


## How to push your local branch to be a remote branch

`$ git push -u origin <your-branch-name>`


## How to checkout a branch

‘Checking out’ a branch is when you pull another person’s branch (or teleport
to another branch), you do it by doing:

``` bash
$ git fetch origin
$ git checkout <branch-name>
```


## How to merge changes

If you get to a point where you are merging changes, you’ll see something in
your code like the following:

```
<<<<<<<HEAD
sarah_strohkorb = pick_the_coolest_ninja(input_1, input_2)
=======
sarah_strohkorb = pick_the_coolest_ninja()
>>>>>>><my-branch-name>
```

The `sarah_strohkorb = pick_the_coolest_ninja(input_1, input_2)` line is what
is represented on the ‘master’ branch and`sarah_strohkorb = pick_the_coolest_ninja()` line is what is represented on the ‘<my-branch-name>’ branch. You’ll have to pick one of them and then delete the rest of
the information. So if I want `sarah_strohkorb = pick_the_coolest_ninja()`,
I’ll rearrange the code to get the following:

```
sarah_strohkorb = pick_the_coolest_ninja()
```


## How to merge one branch into another

Let’s say that you’ve been working on a branch called ‘dev’ and you have also
been modifying the ‘master’ branch. You want to merge your changes in the
‘master’ branch into the ‘dev’ branch, so that your ‘dev’ branch is up to
date. What you want to do is first get into the ‘dev’ branch, then:

```
$ git fetch origin
$ git merge origin/master
```

If you have any conflicts, deal with them, commit and push your changes, and
you’re good to go!
