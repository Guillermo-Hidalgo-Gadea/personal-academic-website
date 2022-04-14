# Introduction to DeepLabCut

## What is DeepLabCut

DeepLabCut is an open source **toolbox** for **markerless** **pose estimation** based on **transfer learning** with deep **neural networks** ([Mathis et al., 2018](https://www.nature.com/articles/s41593-018-0209-y)). It uses algorithms from [DeeperCut](https://link.springer.com/chapter/10.1007/978-3-319-46466-4_3), and an extremely deep neural network pretrained on a dataset for object detection ([ImageNet](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html)). DeepLabCut was originally developed for animal pose estimation, which does not exclude humans, see [Namba et al. (2021)](https://www.nature.com/articles/s41598-021-83077-4), and can also be used to track inanimate objects.

* **What exactly is a toolbox?**

While most of us will probably be most comfortable with end user software with shiny graphical user interfaces, most of the work runs in background processes. Programs or apps are usually compiled (i.e., translated from code to computer instructions) and depend on the operating system. Alternatively, and specifically for open source, software can be distributed as a loose set of instructions, functions of packages. This is more flexible but requires some programming skills or basic software development experience by the user.

A *toolbox* then is a set of pre-existing routines for a specific purpose, a compilation of functions but not necessarily a finished piece of software. In python we will differentiate between instructions or commands, functions, classes, modules and packages.

* **What do we mean by markerless?**

Markerless tracking refers to the fact that DeepLabCut can be used to track animal behavior from videos of behaving animals without id tags or retro-reflective markers attached or pierced to the body. Thus offering a non-invasive and highly flexible way of tracking motion.

During model training, we will have to decide on specific body parts to track, and these will have to be marked (i.e., labeled), but this is done during post-processing and not during *markerless* data collection.

**Note:** There are alternatives to DeepLabCut that work really markerless by analyzing frame-to-frame differences in body shape and calculating motion energy rather than tracking poses.

* **What is pose estimation?**

The difference between pose and position, or better location, is the frame of reference. With location we refer to the position of an object in the environment (e.g., near the feeder) and its movement and orientation over time. With *pose* we refer to the position of body parts relative to each other (e.g., arms extended, sitting in upright position) regardless of where in space the pose is happening.

* **Transfer learning?**  

*Transfer learning* refers to the ability of machine learning models to apply previously learned experiences to new learning tasks. The *generalizability* of a model on the other hand refers to the ability to apply the learned parameters to a wide range of data. *Active learning* refers to the strategy of learning in cycles by trial and error. For instance, a model may be trained with data X, applied to data Y, and after manual correction of Y vs. Y' training the model specifically with errors made in Y'.

* **Neural networks?**  

Machine learning is a discipline concerned with enabling machines to 'learn', instead of being programmed explicitly, to perform appropriate functions. A simple linear regression is the easiest example of a model 'learning' to predict an outcome based on the input and specific regression parameters. This idea is enlarged in bigger neural networks that allow for deeper layers of processing. A typical **artificial neural network** (ANN) takes scalar data as input (i.e., numbers) and gives scalar predictions. **Convolution neural networks** (CNN) are specifically tailored to take images as input (e.g., video frames).

## How does it work

```{figure} content/dlcworkflow.png
---
width: 800px
name: dlcworkflow
---
DeepLabCut workflow from Nath et al. 2019.
```

```{admonition} Note: Tracking is not Behavior
:class: tip
"[...] particular techniques in an academic field can lead to methodological bias which itself delineates the meaning of *behavior*."  -  Calhoun & Hady (2021)
```

## Literature

Mathis, A., Mamidanna, P., Cury, K. M., Abe, T., Murthy, V. N., Mathis, M. W., & Bethge, M. (2018). DeepLabCut: Markerless pose estimation of user-defined body parts with deep learning. Nature Neuroscience, 21(9), 1281–1289. <https://doi.org/10.1038/s41593-018-0209-y>

Nath, T., Mathis, A., Chen, A. C., Patel, A., Bethge, M., & Mathis, M. W. (2019). Using DeepLabCut for 3D markerless pose estimation across species and behaviors. Nature Protocols, 14(7), 2152–2176. <https://doi.org/10.1038/s41596-019-0176-0>
