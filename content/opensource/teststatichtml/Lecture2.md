# How can we measure animal behavior?

## Measuring Behavior

The study of behavior started with rich, naturalistic observations of animals in their natural environments. But these observations were mostly qualitative and anecdotal descriptions, rather than quantitative measurements of behavior (see [George Romanes' *Animal Intelligence*](https://dl.tufts.edu/concern/pdfs/47429n35w) and [Desmond Morris' *The Naked Ape*](https://en.wikipedia.org/wiki/The_Naked_Ape) for such examples).  

A more systematic approach to measuring behavior was achieved by using scoring sheets of pre-defined behaviors of interest, and manually logging the occurrence and duration of these behaviors at a given temporal resolution in specific time intervals. This allowed the quantification of behavior with simple statistics such as the frequency, latency and duration of given behaviors, as well as the relative proportion of several behaviors in given environments.

These observations and manual coding techniques are still popular today, although video recording techniques allow to store data, and score behavior from the lab, instead of in the field. Furthermore, computer-assisted tools allow to score behavior frame-by-frame. More on this will be covered in the Hands on exercise with BORIS later today.

These methods have some obvious **downsides**:

* slow, time consuming and dull
* subjective, limited to human vision and language
* low-dimensional

Specifically, one of the main problems for Psychology and Neuroscience is that the measurement of behavior is by far **not as accurate as advances in neural recording techniques** such as electroencephalography, optogenetics, pharmacogenetics or optical imaging. How are we then supposed to match cognitive and neural processes to the animals behavioral output?

## Computational Ethology

Computational ethology is a new interdisciplinary field using modern advances in machine learning and machine vision (*computational*) for measuring, describing and analyzing natural behavior in freely moving animals (*ethology*).

```{figure} content/stepsince.png
---
width: 800px
name: steps
---
Steps in typical computational ethology systems, from Anderson & Perona (2014).
```

By successfully and skillfully applying machine learning methods the study of behavior will profit from a more accurate quantification of behavior, while outsourcing the painstaking manual labor of video coding. Computational models will increase the throughput of behavioral experiments by tracking multiple subjects at once, measuring over prolonged time windows, or even in real time. Real time measurements, in turn, pose new possibilities to design closed-loop experiments reactive to subjects' behavior.  

Computational methods will also increase the dimensionality of behavior, differentiating between short actions and large-scale behavioral patterns, and setting time-accurate context to subjects behavior in the environment.  
Lastly, specific advances in computer vision revolutionize the way we operationalize the behavior of subjects. See {numref}`levelsofdetail` for an overview of different levels of detail in the tracking of subjects movement.

```{figure} content/levelsofdetail.png
---
width: 800px
name: levelsofdetail
---
Levels of detail in Computational Ethology, from Pereira et al (2020).
```

## External Quantification of Behavior

In specific cases, specially in experiments with controlled environments, researchers are not interested in the overall behavioral pattern of the animal but rather on specific behavioral responses given to certain stimuli. This can be done programatically by recording activity of mechanical switches installed as keys or levers, e.g., in Skinner boxes.  

Key presses are certainly a great solution to outsource manual logging of behavior, but animals need to be trained and incentivized. Therefore, such experiments record learned behavior rather than spontaneous natural behavioral patterns.

This seminar will focus on the first two techniques to quantify broader classes behavior, but automated solutions are indeed essential to most controlled experiments.

## Literature

Anderson, D. J., & Perona, P. (2014). Toward a Science of Computational Ethology. Neuron, 84(1), 18–31. <https://doi.org/10.1016/j.neuron.2014.09.005>

Pereira, T. D., Shaevitz, J. W., & Murthy, M. (2020). Quantifying behavior to understand the brain. Nature Neuroscience, 23(12), 1537–1549. <https://doi.org/10.1038/s41593-020-00734-z>
