# The Cheeky Cheetahs

This section of the course handbook has been provided as part of the final group project for the Seminar on Tracking Animal Behavior at the Ruhr-University Bochum in WS21/22.

```{admonition} Project Authors
Janna, `B.Sc. Psychology`, and Beyza, `B.Sc. Psychology`.
```

## Abstract

In this project, we decided to do a kinematic analysis of cheetahs in their natural environment and chose to concentrate on the (body-) movement of the animals. In order to do this we compared video footage of actively running/hunting cheetahs and cheetahs walking normally. With this analysis, we were planning to enable a closer look at the differences of the body movements during the different circumstances.

In general, we were interested in detecting how exactly the body movements differ and if we can conclude a general pattern that we can use for other hunting animals as well (tigers, lions, panthers etc.).
The video footage was taken from many YouTube-clips of documentaries and similar videos, which were edited together. They show the animals attacking their prey, walking around in normal speed as well as different angels and perspectives. This is important for the labelling process, so we can get a model, which is trained in detail and able to recognize all the necessary body parts as well.
For labelling, we chose marks on the following parts: at the head (left and right ear, forehead, nose and neck) at the back (neck, the two parts of the spine and the behind), three points at the tail, and we also marked each leg in three parts.

## Labeling and Analysis

```{figure} content/cheekycheetahsfig0.svg
---
width: 900px
name: cheekycheetahsfig0.svg
---
Overview of some test and training frames during DLC evaluation.
```

As we can see here in the figure below, the trained labels fit our own labelling quite well. In general, our DeepLabCut model was easily able to adapt to all our previous labels. However, the third part of the left front leg is marked with a red X, probably because it was hard to separate it from the ground. The calm movements and clear shots allow an easy labelling and evaluation process.

```{figure} content/cheekycheetahsfig1.png
---
width: 400px
name: cheekycheetahsfig1.png
---
Evaluation frame of a walking cheetah.
```

This labelled frame from a running clip is a very good example to show the trouble of labelling body parts of the running cheetah. Because it is able to blend perfectly into the environment due to its natural camouflage, it is very hard to distinguish its limbs and label them correctly. The bad video quality also adds to troubled labelling.

```{figure} content/cheekycheetahsfig2.png
---
width: 400px
name: cheekycheetahsfig2.png
---
Evaluation frame of a running cheetah.
```



## Troubleshooting

The first analysis of the trained data showed us that we have to be more precise in labelling and connecting the skeleton so we can have a good and representative model. Since we build the first skeleton based on an already chosen picture, it was hard to find all the points and label and connect them as we wish.

```{figure} content/cheekycheetahsfig3.png
---
width: 400px
name: cheekycheetahsfig3.png
---
Build-Skeleton GUI in DeepLabCut.
```

Therefore, we chose to build another skeleton and name the connections in the yaml-file. This allowed us to create a much more detailed and accurate skeleton that is also a lot closer to the original anatomy of  the animal.

## Evaluation

After taking a closer look at the labelled video footage, we can conclude that there is indeed a recognizable difference in the body movements of the hunting and walking animal.

The skeleton shows how the head can be connected to the tip of the tail and create a line tracing the spine. When the cheetah is walking, the tail tends to fall behind and create a small curl at the end, while the head is the highest and least moved part of the body. The limbs are calmly moved in pairs, meaning the right front leg moves forward with the right back leg and the left frond one with the left back one.

When the animal is running and hunting for prey, it is noticeable how the curl in the tail is seems to be straightened while the head is still the highest and least moved part of the body. However if we pay attention and observe the movements of the limbs we can see how they do not move similar to how when they are walking. The front and the back limbs move together and it seems as the cheetah pushes himself with every step to gain speed. With its front, it “shoves” its whole body forward and supports the movement with the back. Added to that, the hips tend to fold and make the body appear very small right after it was widely extended. This allows the body to move at very high speed and in a very efficient way to enable hunting without limitation.

## Conclusion

In conclusion, we can say that the analysis with DeepLabCut definitely allowed a closer, more precise look to compare the movements of a running and a walking cheetah. Following the labels and the skeleton helps to visualize the gradient of the hunting and walking process. It is important to orientate the labelling and the skeleton on the body anatomy so it allows an accurate and specific comparison. Furthermore, the video quality and the colours of the surrounding also adds to the preciseness of the analysis and can play a huge role in the results.
