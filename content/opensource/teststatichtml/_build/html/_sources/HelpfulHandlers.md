# Helpful Handlers

This section of the course handbook has been provided as part of the final group project for the Seminar on Tracking Animal Behavior at the Ruhr-University Bochum in WS21/22.

```{admonition} Project Authors
Sarah, `B.Sc. Psychology`, and Sarah, `B.Sc. Psychology`.
```

## Abstract

In our project we wanted to train a DeepLabCut model to recognize the human right hand and track several hand movements. Therefore, we collected our own video data using a smartphone camera. To reduce the complexity of the model, we decided to focus only on the right hand.
We defined specific movements and different actions that we wanted to track and gathered five different types of video footage:

1. Basic hand movement: Simple turning movements of the right hand around its own axis (left, right, up and down). Some grabbing movements and movement of individual fingers.

2. Playing piano: Movements of the right hand when playing some accords/ melody on the keyboard of a piano.

3. Typing on keyboard: Movements of the right hand when typing on the keyboard of a laptop.

4. Writing by hand: Movement of the right hand when writing a text.

5. Waving: Waving and some grabbing movements of the right hand.

We collected two videos per hand per movement type. This resulted in a total collection of 10 videos. For tracking the hand, we decided to set 20 markers. For manual video labeling we decided to extract 10 frames per video.

For our final analysis we were interested in comparing the trajectories of the tracking points of the fingers in the three video types "Waving", "Playing piano" and "typing". We also compared the changes in position of the index finger tip by time in these three different video types.

## Model Evaluation

```{figure} content/helpfulhandlersfig0.svg
---
width: 900px
name: helpfulhandlersfig0
---
Sample of test and training frames from `deeplabcut.evaluate_network()`
```

## Data Analysis

Depicted below are the trajectory plots as they are outputted by DeepLabCut plus a similar trajectory plot for a single label (IT(IndesTip)) that was manually created using matplotlib for three exemplary videos.

```{figure} content/helpfulhandlersfig1.svg
---
width: 600px
name: helpfulhandlersfig1
---
```

```{figure} content/helpfulhandlersfig2.svg
---
width: 600px
name: helpfulhandlersfig2
---
```

```{figure} content/helpfulhandlersfig3.svg
---
width: 600px
name: helpfulhandlersfig3
---
```

Comparing the trajectory plots as they are outputted by DeepLabCut, one can see that the plots for “Playing piano” and “Typing” look very similar, whereas the plot for “Waving” looks a bit different in comparison to these two plots. In the „Waving“ plot the points tracking the centre of the palm are indeed very centred, whereas the points tracking the different parts of the fingers are very scattered. In the plots for “Playing piano” and “Typing” the points tracking the centre of the palm are more scattered like the points for tracking the different parts of the fingers. Interestingly, there seems to be some kind of structure in the plots for “Playing piano” and “Typing”, indicating that the hand as a whole doesn’t move around much, but there are some movements of the fingers. Comparing “Playing piano” and “Typing” one can see, that there are more finger movements in the “Playing piano” video than in the “Typing” video, as the points tracking the fingers are more scattered in the “Playing piano” plot.

Comparing the three plots created with matplotlib, one can see that all three differ from another. The “Playing piano” plot suggests that from the beginning to the middle of the video there is much movement of the right index finger tip, whereas at the end of the video the movements decrease. In the “Typing" plot it can be seen that there is a lot of movement of the right index finger tip throughout the whole video. The ”Waving” plot also shows a lot of movement of the right index finger tip through the whole video. Interestingly, in the middle of the video there seems to be no movement, which could be due to the fact that at one point there were no waving but grabbing movements filmed in the “Waving” video. In comparison to the “Typing” video the movements seem to be wider, whereas in the “Typing” video they are more centred.

## Conclusion

First of all we were impressed by how good DeepLabCut recognized the model of the hand and was able to label the model with a greater accuracy than we had anticipated.

We found that DeepLabCut can be used to do some very interesting analyses and so could be useful for further research questions. Of course there were also some issues, e.g. when we tried to save the manually labelled frames, but nonetheless DeepLabCut is a powerful tool which seems to be of great use for research investigating and analyzing behavior.
