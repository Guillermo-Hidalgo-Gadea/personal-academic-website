# Restless Raterality

This section of the course handbook has been provided as part of the final group project for the Seminar on Tracking Animal Behavior at the Ruhr-University Bochum in WS21/22.

```{admonition} Project Authors
Patrick, `PhD student`, and Sevim, `PhD student`.
```

## Abstract

Asymmetry is one key component of neural organization. Changes in asymmetry are associated with a variety of developmental and psychiatric disorders, such as autism and schizophrenia. Understanding the way asymmetry arises during development therefore promises important insides and possible targets to prevent illness and help patients. Offspring of dams, which were exposed to restraining stress during pregnancy, were therefore tested for behavioral asymmetries during development. Head turning asymmetries during a sucrose-drinking task were tracked using DEEPLABCUT. 20 different video clips, about 10 minutes of length, were extracted from 10 testing sessions of different rats of both sexes. 17 Marker points were placed on the nose, both eyes, both ears, the front paws, the top of the head, the neck, 4 on the back, the tailbase, middle of the tail and end of the tail, as well as 1 reference point on the drinking bottle. 7 frames from each video were extracted for manual marking. The resnet_50 model was then trained for 10000000 iterations."

## Results

Within the scope of the third block seminar, firstly we checked the accuracy of the DLC fort he labelling by looking the labeled pictures and videos (figure 1). The accurancy might be improved by performing another training session.

```{figure} content/Rateralityfig0.svg
---
width: 900px
name: rateralityfig0
---
Sample of test and training frames from `deeplabcut.evaluate_network()`
```

On the second day, we could successfully open and read our data by using different libraries such as pandas, numpy and matplotlib.plyplot. We defined the bottle (the first body part) as a reference point for our analysis. Since we do not have any 3d model/tracking we just ignored z axis for all the steps. To check position in steps by creating a graph, as a initial step we have defined some of the body parts such as bottle, left ear, head. – We only used the first 500 frames since our overall frame numbers are too high for the graphs. According to position of the left ear and head in the graphs that we have, we could estimate the backside and/or frontside of the animal agains to the bottle/camera. For example: If the left ear and head are in the same side (higher than 0) the animals might be standing towards the bottle.

```{figure} content/Rateralityfig2.png
---
width: 800px
name: rateralityfig2
---
Movement towards the bottle on x-Levels
```

```{figure} content/Rateralityfig3.png
---
width: 800px
name: rateralityfig3
---
Movement towards the bottle on y-Levels
```

To ensure improved tracking, we are planning to label front and backside (spin) of the animal by using different body part points for further analysis. For this purpose, we will also define threshholds to determine the back and front sides of the animals for head tilting behavior during the drinking.
