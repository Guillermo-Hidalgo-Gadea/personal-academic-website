# Hugging Humans

This section of the course handbook has been provided as part of the final group project for the Seminar on Tracking Animal Behavior at the Ruhr-University Bochum in WS21/22.

```{admonition} Project Authors
Petunia, `M.Sc. Psychology`
```

## Abstract

Human embraces are an interesting research topic since the behavior does not only need the coordinated movement of multiple body parts within one person but coordinated movement between individuals.

## Method

```{figure} content/Hugginghumansfig0.svg
---
width: 900px
name: Hugginghumansfig0
---
Labeling Scheme for multi animal DeepLabCut model
```

### Recording

To get the data, multiple videos oft two people hugging were recorded from different angles.

### Labeling

```{figure} content/Hugginghumansfig1.svg
---
width: 900px
name: Hugginghumansfig1
---
Resulting skeletons after the labeling process
```

Above you can see the skeleton after the labeling process. Labels were placed on 25 different body parts starting on the top of the head and going all the way down to the toes. A detailed list of all markers can be found in Appendix A.

During labeling some problems arose, making the process difficult. On many pictures only a few markers could be placed since the others were occluded by the other person or not captured by the cameras. Skipping most markers on the different body parts took a lot of time and led to very different amounts of labeled data regarding the different body parts. While faces could be seen in many of the frames, the hips and knees were often hidden. Another problem was that the dark and long clothes made it hard to precisely estimate the intended location. Deciding whether a certain body part could be seen in a specific frame or if it was simply due to prior knowledge of „where the body part should be“ was not always simple. Figure 1 shows some of the resulting skeletons after the labeling process was done.

## Results

### Labeled Images

The model was trained over the Christmas holidays. The results can be seen in Figure 2. The left part of the figure shows the accuracy on the trainings-data. Here we can see, that DeepLabCut performed very well, even though there were many problems during the labeling process. The right part of the figure shows the performance on previously unseen test-data. Here the model performs slightly worse, but still the accuracy seems very high.

```{figure} content/Hugginghumansfig2.svg
---
width: 900px
name: Hugginghumansfig2
---
Left: Model performance on previously seen trainings-data. Right: Model-performance on previously unseen test-data.
```

### Labeled Videos

The tracking of the different body parts in the videos was problematic. This problem was most likely due to many factors, one of them being a mistake in the config.yamel file. The identity was not set to „True“ – which resulted in confusion of the body parts of the hugging people. As can be seen in Figure 3, the labels are in 2 different colors. Those colors are to separate the humans from each other. My (Petunia) color should be black and that of Marius is supposed to be yellow in all frames. But as can be seen below, I seem to have my own face, but the leg of Marius. Next to this body part-confusion, many points weren’t labeled at all, even though they can be clearly seen in the frame (e.g., my right shoulder, Marius left shoulder, …).

```{figure} content/Hugginghumansfig3.svg
---
width: 600px
name: Hugginghumansfig3
---
Labeled videos after the model was trained. One frequent problem can be seen through the different colored labeling. The colors should separate the individuals from one another, but body parts got confused in many frames. Here I (Petunia) have my own face but Marius' leg. 
```

replace with short video?

## Appendix

List of labeld Keypoints for each individual in the maDLC project
|           |           |           |           |           |           |
| --------  | --------- | --------- | --------- | --------- | --------- |
| - TopHead | - Eyes    | - Chin    | - Neck    | - LeftEar | - RightEar|
| - MiddleChest | - MiddleHighBack | - LeftShoulder | - LeftElbow | - LeftHand | - LeftThumb |
| - RightShoulder | - RightElbow | - RightHand | - RightThumb | - MiddleHip | - MiddleLowBack |
| - LeftHip | - LeftKnee | - LeftHeel | - LeftToes | - RightHip | - RightKnee |
| - RightHeel | - RightToes | | | | |
|           |           |           |           |           |           |
