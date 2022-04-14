# Data Analysis Tutorial

## What is Data? A dramatic introduction

<iframe width="875" height="492" src="https://www.youtube.com/embed/2X9pv7FUrOk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Getting started

Want to learn some data science? Because you should... Math and Statistics are only half of the story. Coding and data management are at least as important, and will probably be an easier start. Get some data, plan a project and start learning by doing. I can only encourage you to learn [Python](https://www.python.org/) and [R](https://www.r-project.org/), maybe even [julia](https://julialang.org/).

## Data Analysis with Python

This is going to be a very short crash course. The main goal is to get you started with python and make some sense of your DeepLabCut data from the previous exercise. You are encouraged to keep playing with the data and the notebooks provided above and beyond the scope of this seminar. If you are interested in a deeper understanding of the matter feel free to [get in touch](contactform.md).

Before you start applying some of the following tips and tricks to your own data, we will learn a little about how to manage data, read data in python, check the data structure and explore some descriptive statistics and plots. Next, we will see basic functions to analyze kinematic features in DeepLabCut time series data, and last but not least, we will take a look at some beginner friendly machine learning algorithms to classify and predict data.

Dummy data for the following exercises is provided from the seminar cloud [here](https://ruhr-uni-bochum.sciebo.de/f/1324685625). Please also download the following notebooks from this book as .ipynb file and follow along on your computer.

### [What does data look like](datainspection.ipynb)

* Data management tips
* How to read data
* How is my data structured
* What does my data tell me
* How could my data look like

### [Kinematic analysis](kinematicanalysis.ipynb)

* Position in space
* Velocity as difference between positions in dt
* Acceleration as difference in velocity in dt

### [Machine learning](machinelearning.ipynb)

* Time segmentation with Hidden Markov Models
* Gaussian Mixture Models
* Decision Trees
* UMAP dimensionality reduction
