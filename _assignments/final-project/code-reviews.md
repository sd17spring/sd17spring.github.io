---
date: 2017-01-14 10:36:07 -0500
description: ''
parent: final-project
title: Code Reviews
---

{% include toc %}

## Overview

> I believe that peer code reviews are the single biggest thing you can do to
improve your code.
>
> Jeff Atwood, Co-Founder of Stack Overflow (source: <http://blog.codinghorror.com/code-reviews-just-do-it/>)

Code Review day will be divided into three review periods. During one period,
you will present code from your project for classmates to review. During the
other two periods, you will review code from other projects in your [team
group](/assignments/final-project/technical-reviews#team-groupings-and-schedule). Each team member (or, in some cases, _pair_ of
members) will present code separately from the rest of their team.

Code review has many benefits, and is broadly used in the software industry.
The benefits we are hoping for in this class are:

1. Learning from, and teaching, your peers
2. Additional practice thinking about your code from the perspective of someone who hasn't seen it
3. First-hand experience with a software review process itself
4. Finding bugs

## Before the Code Review

**_1._** Your GitHub repository should contain a README that follows the [README rubric](/assignments/final-project/readme-rubric).

**_2._** Your team should select _three_ code sections for code review. Each section will be presented by a different team member or members.

Each code section should be a function, class, or set of functions, that sum
to 50 to 200 lines of code. If the code is complex, Bias towards the shorter
length.

Some ideas for choosing code sections: code that you have questions about;
code that you want to show off; code that you suspect may be fragile or buggy;
code that is particularly complicated.

**_3._**  Assure that each code section has sufficient documentation for a reviewer to figure out when it's called, what it does, and how it does it. Documentation can include comments, unit tests, and descriptive function and variable names. If there is global information about the program's operation that doesn't make sense here, you may want to add it the README instead.

**_4._**  For each code section, prepare a **_Review URL_** . We are giving you a choice of review mechanisms:

_Option 1_ : Take a screenshot of your code, and upload it to
<http://bounceapp.com>.

_Option 2_: Create a whole-project GitHub Pull Request for your entire
project. (The instructions for this will be posted in Piazza.) The Pull
Request should describe the code section that is being submitted for review;
for example, “file recursive_art.py, functions build_ random_function and
evaluate_random_function”.

In either case, paste the Pull Request URL into the [SoftDes Code Review URL
spreadsheet](https://docs.google.com/spreadsheets/d/1wMGPpfNCHD_PmlquK3ffDJjZdtsxi49nz0BCG-bJapA/edit?usp=sharing).

**_5._** Decide which team member(s) are presenting which code segments. Each team member should be prepared to introduce the code segment to the reviewers. (See below.)

## Day of the Code Review

The day of the review will be divided into 25-minute blocks, with individuals
taking turns as Presenter and Reviewer. Both roles are equally important and
you are expected to contribute fully to each.

### Presenter

* Give a brief description of your project. Your audience has seen your presentation during the Technical Review and has access to the README; this is a quick verbal reminder of what your project is and update on its implementation status.
* Verify that your reviewers have access to your project's README, and to the Review URL.
* Optional: GitHub Pull Request, direct the reviewers to the appropriate section of the Review URL.
* Optional: If you are looking for particular kinds of feedback, tell the reviewers. For example, if you are unsure whether code is correct, or robust, or if you would like stylistic advice.
* Be available to answer questions about the project or code.
* Thank your audience when time is up.

### Reviewer

* Do you understand what the code is for, and how it works? Do you have enough information to test, debug, or extend this code? Add comments to the Review URL where the answer is “no”. You can also then ask the Presenter for more information, in order to proceed.
* Don't comment on stylistic decisions – whitespace, names – unless they affect readability.
* Be respectful and constructive in your feedback.
* Don't be playing on your phone or using your laptop for non-class activities during the code review. If you feel you've thoroughly covered the selected code section, begin to look at the rest of the repository.

## After the Code Review

After the code review, we will reflect on the activity as a group to talk
about what went well and what could be improved. You may want to independently
run another code review with one of your peer teams before the end of the
semester.

## Grading rubric

The technical review is worth 10% of your project grade.

You must attend your scheduled code review session. If you will be absent on
the day of the technical review, you must contact the teaching team
beforehand.

For full marks:

Presenters:

* README is pushed to GitHub prior to class; includes all required sections.
* Review URLs are added to [SoftDes Code Review URL spreadsheet](https://docs.google.com/spreadsheets/d/1wMGPpfNCHD_PmlquK3ffDJjZdtsxi49nz0BCG-bJapA/edit?usp=sharing) prior to class.
* GitHub Pull Request descriptions includes the file names and classes or functions selected for review.
* The README and code give sufficient context for reviewers to review the code effectively.
* Presenters are available to reviewers, and undistracted, during review.

Reviewers:

* Demonstrate an earnest attempt to understand the code.
* You don't have to add a comment if you don't have anything to say.

Everyone:

* Undistracted attention on classroom activity.
* Participate in reflection afterward.

## Team groupings and schedule

### Schedule

Also posted on the [course calendar](/calendar).


**Technical Review #1**

  * Updated README pushed to GitHub: before class April 14
  * Review URL added to shared document: before class April 14
  * Code Review: in class April 14

### Team groupings

Logistics details are fully explained on the [Day 22 page](/in-class-exercises/day-22)
