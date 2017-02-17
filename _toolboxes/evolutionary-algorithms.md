---
date: 2017-02-17
description: ''
title: Evolutionary Algorithms
---

{% include toc %}

## Background

**WARNING:** This background section is way too much fun. The SoftDes
teaching team cannot be held responsible for lost productivity that may
result. You might want to grab a comfy chair and a frosty beverage before
proceeding.

[Evolutionary algorithms](http://en.wikipedia.org/wiki/Evolutionary_algorithm)
use techniques inspired by biological evolution to find approximate solutions
to complex optimization problems. In brief, these
[heuristic](http://en.wikipedia.org/wiki/Heuristic_%28computer_science%29)
algorithms represent potential solutions as individuals within a population.
New solutions are generated from the population via mutation and reproduction,
and the fittest survive to form the next generation.

### Example 1: Evolving biped gaits

### Flexible Muscle-Based Locomotion for Bipedal Creatures

The gaits shown in this video were not designed: they were evolved. The
researchers provided an environment with constraints (physics) plus a "fitness
function" for evaluating individuals (able to walk the farthest without
falling), and "natural selection" did the rest without human intervention.

Notice how the same algorithm is able to flexibly adapt to different
constraints (walking on uneven terrain or on the moon). It is also fascinating
to watch it rediscover many efficient gaits found in nature.

### Example 2: Evolving cars

  1. Go to <http://boxcar2d.com>.
  2. Don't forget to close your browser at some point to eat and sleep.

This physics simulation attempts to evolve cars to successfully negotiate
randomly generated terrain. Each car is represented by a simple "genotype" — a
vector describing the polygons and wheels that comprise the car's body. The
[BoxCar 2D algorithm description](http://boxcar2d.com/about.html) has more
details about how new cars are generated and selected.

### Example 3: Evolving FPGAs

Read: [On the Origin of Circuits](http://www.damninteresting.com/on-the-origin-of-circuits/) (1500 words)

This example brings evolutionary algorithms into the hardware world: a
researcher was able to evolve a [Field Programmable Gate
Array](http://en.wikipedia.org/wiki/Field-programmable_gate_array) (a type of
reprogrammable logic chip) to distinguish between two audio tones. The
resulting circuits were radically different from anything a human designer
would ever come up with.

## Get set

Grab the starter code for this toolbox exercise via the normal fork-and-clone
method from <https://github.com//{{site.course.github_owner}}/ToolBox-EvolutionaryAlgorithms>

You should see `evolve_text.py` within the toolbox folder.

For this exercise, we will be using the [Distributed Evolutionary Algorithms
in Python](http://deap.readthedocs.org/) (DEAP) framework, as well as
[NumPy](http://www.numpy.org/) for collecting some statistics. Install them
both by running:

    $ sudo pip3 install deap
    $ sudo pip3 install numpy

**Note:**  The problem we will tackle in this exercise is simple enough that
we could implement it from scratch with no framework, but DEAP is a powerful
set of tools that you might find useful in the future.

## Let's talk about all the good things and the bad things that may be

In this toolbox exercise, you will implement a [genetic
algorithm](http://en.wikipedia.org/wiki/Genetic_algorithm) (GA) to evolve an
initial population of random strings into a specified string.

**Caveat**: Although it's a good learning exercise, this problem is not
a particularly appropriate application for evolutionary algorithms, since the
exact solution and the shape of the search space are known in advance. For
more, check out ["When are Evolutionary Algorithms
Useful?"](http://watchmaker.uncommons.org/manual/ch01s02.html) and this list
of [Applications of Genetic
Algorithms](http://www.lcc.uma.es/~ccottap/semEC/cap03/cap_3.html).

In general, genetic algorithms follow these basic steps:

1. Create an "genotype" encoding of problem solutions
2. Generate an initial population of individuals with random genotypes
3. Using a problem-specific "fitness function", select the best individuals from the population and kill off the rest
4. Mate the selected individuals to create a new generation of individuals
5. Randomly mutate the genotypes of some individuals
6. Repeat 3-5 for as many generations as required

## Implementing genetic operators

Let's take a deeper look at each of these steps, and implement each in turn.

**First, look through the provided starter code and try to identify the components of the genetic algorithm.**

### Genotype representation

The individuals in our population are represented as `Message` objects, each
of which hold a text string.

**Design decision:**  Why is this implemented with a list of characters
instead of a string?

### Evaluating fitness

The fitness function is usually the most problem-specific component of any GA.
For this exercise, Messages that are closer to the target text are more fit.
Unlike most problems GAs tackle, the optimal solution is known — when the
Message is identical to the target text. To make this more precise, the goal
for this GA is to minimize the [Levenshtein
distance](http://en.wikipedia.org/wiki/Levenshtein_distance) between the
Message and the target text.

**Implement the `levenshtein_distance` function.**

**Note:**  Check out the [Day
8]({% link _days/day-8.md %})
exercises. You will need the memoized version to get any reasonable
performance.

### Mating

Mating combines pieces of the genotypes of two parent Messages to produce
offspring. For this exercise we will use a [two point
crossover](http://deap.readthedocs.org/en/master/api/tools.html#deap.tools.cxTwoPoint)
technique, which has the following (pseudocode) behavior:

      >>> parent1 = "ABCDEF"
      >>> parent2 = "UVWXYZ"
      >>> print(TwoPointCrossover(parent1, parent2))
      ("ABWXYF", "UVCDEZ")

This crossover is intended to model [homologous
recombination](http://en.wikipedia.org/wiki/Homologous_recombination) of
chromosomes that occurs during sexual reproduction.

**Skills check:**  We are using the
[`tools.cxTwoPoints`](http://deap.readthedocs.org/en/master/api/tools.html#deap.tools.cxTwoPoint)
function built into DEAP. Implement your own crossover function, and update
the "mate" alias in `get_toolbox` to use your version.

### Mutation

Mutation modifies the genotype of a single individual, and is intended to
model chromosome [mutation](http://en.wikipedia.org/wiki/Mutation). The types
of mutation possible in this exercise are:

* Insertion of a single Message character
* Deletion of a single Message character
* Substitution of a single Message character for another random character

**Implement the `mutate_text` function, with independent probabilities for each mutation type.**

## Evolving text

Once you've made the modifications in the previous section, it's time to
evolve some text! To call your program, run:

    $ python3 evolve_text.py [goal_message]

where `goal_message` is an optional argument specifying the target text.
Excerpts from a sample execution of the program are given below.

    [Generation 0]
    Message('VVFIQTXXCQSNEMCZXOIYPXWNLQLEIVBBQHOMJ FLFR') [Distance: 37]
    Message('JUPN') [Distance: 33]
    Message('STZMIIIIIFNHJRIXVIWEC AAXARPGG KGLTHCVCBA LTP JJS') [Distance: 42]
    ...
    [Generation 10]
    Message('NDAEOS OIDEAN YWIZESU') [Distance: 25]
    Message('RBA HAQSKYFWHYWPWNTFEBT') [Distance: 25]
    ...
    [Generation 20]
    Message('IUEBTS MKYBWH YWITETRS') [Distance: 17]
    ...
    [Generation 100]
    Message('IUMBATS MNKFYS WIH TYWSITERS')  [Distance: 11]
    ...
    [Generation 200]
    Message('SUE BATS MONKYS WH TYPEWRITERS') [Distance: 5]
    ...
    [Generation 500]
    Message('SURE BEATS MONKEYS WITH TYPEWRITERS') [Distance: 0]

## Experimentation

The performance of a genetic algorithm on a particular problem depends on the
genetic operators used, as well as the parameters selected. A few suggestions
for things to try:

* Change the population size or number or generations to run (in `evolve_string`)
* Change the probabilities for crossover and mating (`evolve_string`) or the various mutation probabilities (alter when you register the "mutate" toolbox alias in `get_toolbox`)
* Rather than randomizing the population, start with a monoculture of individuals with the same initial string
* Modify your distance function to account for the distance between letters, e.g. A -&gt; B is closer than A -&gt; Z (use `ord` function)
* Try a different [evolutionary algorithm](http://deap.readthedocs.org/en/master/api/algo.html#module-deap.algorithms) from DEAP, e.g. `eaMuPlusLambda` instead of `eaSimple`
* Try another [selection operator](http://deap.readthedocs.org/en/master/api/tools.html#selection) from DEAP, e.g. `selBest` instead of `selTournament`

**Choose at least one of these experiments (or a different one of your own design) and study how it changes the genetic algorithm's performance (e.g. number of generations to converge to the target text).**

## What to turn in

Push both your `evolve_text.py `and a `results.txt` with the findings from
your experimentation to GitHub and submit a pull request to get checked off.

## Going beyond

* [**Genetic Programming** ](http://deap.readthedocs.org/en/master/tutorials/advanced/gp.html) \- programs that evolve other programs. Challenge problem: write a program to take Software Design for you, kick back for the rest of the semester (as always, the challenge will be the fitness function)
* **Evolve Artwork -** Someone has written a [genetic algorithm to evolve famous artwork](http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/) using only 50 transparent polygons. Challenge problem: modify your [computational art project](/assignments/mini-project-2-computational-art) to evolve a given image using function composition.
* **D is for [Distributed](http://deap.readthedocs.org/en/master/tutorials/basic/part4.html)**  \- If you have access to a cluster or multiprocessor system, try running a large scale evolutionary algorithm to solve a non-trivial problem.

## Further reading

* _Evolutionary Computation_ , by David Fogel, Thomas Bèack, and Zbigniew Michalewicz [[Olin College library ebook]](http://web.b.ebscohost.com/ehost/detail/detail?sid=3086a330-6951-4213-8e0b-b4ccc62f3035%40sessionmgr110&vid=1&hid=109&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#db=nlebk&AN=32720)
* [Rosetta Code](http://rosettacode.org/wiki/Evolutionary_algorithm) \- Evolving strings in every programming language you can think of
